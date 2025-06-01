import os
import asyncio
import requests
from dotenv import load_dotenv
from agents import Runner, Agent, AsyncOpenAI, function_tool, RunConfig, OpenAIChatCompletionsModel, ModelProvider

# Custom ModelProvider for Gemini API
class GeminiModelProvider(ModelProvider):
    def __init__(self, client):
        self.client = client

    # async def create_completion(self, model, messages, **kwargs):
    #     try:
    #         return await self.client.chat.completions.create(model=model, messages=messages, **kwargs)
    #     except Exception as e:
    #         raise ValueError(f"Error calling Gemini API: {str(e)}")

    def get_model(self, model_name: str | None) -> OpenAIChatCompletionsModel:
        """Get a model by name.

        Args:
            model_name: The name of the model to get (e.g., 'gemini-1.5-flash').

        Returns:
            The model instance.
        """
        if model_name is None:
            model_name = "gemini-2.0-flash"  # Default model
        return OpenAIChatCompletionsModel(
            model=model_name,
            openai_client=self.client
        )
# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
if not GEMINI_API_KEY or not WEATHER_API_KEY:
    raise ValueError("GEMINI_API_KEY and WEATHER_API_KEY must be set in .env file.")

# Set up Gemini client
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Set up model config
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # Verify this model ID
    openai_client=external_client
)

# Set up RunConfig
model_provider = GeminiModelProvider(external_client)
config = RunConfig(
    model=model,
    model_provider=model_provider,
    tracing_disabled=True
)
# 
# Weather tool
@function_tool
async def get_current_weather(location: str) -> dict:
    """Get the current weather for a given location.
    
    Args:
        location (str): The city and state/country, e.g., 'New York, NY' or 'London, UK'
    Returns:
        dict: Weather data including location, temperature (Celsius), and description
    """
    print(f'Fetching weather for: {location}')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "location": location,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch weather data: {str(e)}")

# Main agent
async def main():
    agent = Agent(
        name="Weather Agent",
        instructions="""
            You're a Weather Agent that fetches current weather data for any location using the provided tool.
            For weather queries, call the get_current_weather tool and explain the results clearly with emojis! 🌦️
            If the query is unrelated to weather, respond with a friendly message explaining you can only handle weather requests.
        """,
        model=model,
        tools=[get_current_weather]
    )
    
    print("\n🌞 Weather Agent is ready to fetch weather data! 🌧️")
    while True:
        user_prompt = input("\nAsk about the weather or 'exit': \n")
        if user_prompt.strip().lower() == "exit":
            print("👋 Stay dry! 😎")
            break
        try:
            print(f"Processing query...⏱️: {user_prompt}")
            result = await Runner.run(agent, user_prompt, run_config=config)
            print(f"Runner result: {result}")
            print("🌍 Agent Answer:", result.final_output)
        except Exception as e:
            print(f"🌍 Error processing query: {str(e)}")
                


if __name__ == "__main__":
    asyncio.run(main())
    print(f"Tool object: {get_current_weather}")
    print(f"Tool attributes: {dir(get_current_weather)}")
  
    
    