from agents import Runner, Agent, AsyncOpenAI, function_tool, RunConfig, OpenAIChatCompletionsModel
import asyncio
import dotenv
import os
import math


dotenv.load_dotenv()  # Load .env variables

if not (GEMINI_API_KEY := os.getenv("GEMINI_API_KEY")):
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

# Set up Gemini client
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Set up model config
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,  # type: ignore
    tracing_disabled=True,
)

# ========== TOOL FUNCTIONS ==========

@function_tool
async def add(a: float, b: float) -> float:
    """Add two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: The sum of a and b
    """
    print(f'Adding numbers: {a} + {b}')
    return a + b

@function_tool
async def subtract(a: float, b: float) -> float:
    """Subtract two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: The difference of a and b
    """
    print(f'Subtracting numbers: {a} - {b}')
    return a - b

@function_tool
async def multiply(a: float, b: float) -> float:
    """Multiply two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        float: The product of a and b
    """
    print(f'Multiplying numbers: {a} * {b}')
    return a * b

@function_tool
async def divide(a: float, b: float) -> float:
    """Divide two numbers. Returns error on divide-by-zero.
    
    Args:
        a (float): Numerator
        b (float): Denominator
    Returns:
        float: The quotient of a and b
    """
    print(f'Dividing numbers: {a} / {b}')
    if b == 0:
        raise ValueError("You can't divide by zero! Nice try tho.")
    return a / b

@function_tool
async def square(n: float) -> float:
    """Return the square of a number.
    
    Args:
        n (float): Number to square
    Returns:
        float: The square of n
    """
    print(f'Squaring number: {n}')
    return n ** 2

@function_tool
async def cube(n: float) -> float:
    """Return the cube of a number.
    
    Args:
        n (float): Number to cube
    Returns:
        float: The cube of n
    """
    print(f'Cubing number: {n}')
    return n ** 3

@function_tool
async def sqrt(n: float) -> float:
    """Return the square root of a number.
    
    Args:
        n (float): Number to find the square root of
    Returns:
        float: The square root of n
    """
    print(f'Calculating square root of: {n}')
    if n < 0:
        raise ValueError("Negative numbers can't have real square roots.")
    return math.sqrt(n)

@function_tool
async def power(base: float, exponent: float) -> float:
    """Raise a number to a power.
    
    Args:
        base (float): Base number
        exponent (float): Exponent
    Returns:
        float: Base raised to the power of exponent
    """
    print(f'Calculating power: {base} ^ {exponent}')
    return base ** exponent

# ========== MAIN AGENT ==========


async def main():
    agent = Agent(
        name="Math God Agent",
        instructions="""
            You're the Math God Agent — a savage calculator that can handle everything
            from 2 + 2 to square roots, powers, and complex arithmetic. You know when to
            call tools for calculations and when to explain results in simple language.
            also explain how you do it step by step.
        """,
        tools=[add, subtract, multiply, divide, square, cube, sqrt, power],
    )

    print("\n🤖 Math God Agent is ready to assist you with your calculations!")
    while True:
        user_prompt = input("\nAsk me anything (or type 'exit' to quit): \n")
        if user_prompt.strip().lower() == "exit":
            print("👋 Bye bye nerd 🤓")
            break

        result = await Runner.run(agent, user_prompt, run_config=config)

        print("🧠 Agent Answer:", result.final_output)
        print("🔍 Agent Thought Process:", result.new_items)


async def test_tool():
    response = await external_client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=[{"role": "user", "content": "What is 5 + 10?"}],
        tools=[{
            "type": "function",
            "function": {
                "name": "add",
                "description": "Add two numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"}
                    },
                    "required": ["a", "b"]
                }
            }
        }]
    )
    


# ========== RUN THE AGENT ==========

if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(test_tool())
