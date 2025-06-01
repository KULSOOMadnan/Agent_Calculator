# from main import get_current_weather ,external_client, 
# import asyncio
# async def test_gemini_tool():
#     response = await external_client.chat.completions.create(
#         model="gemini-2.0-flash",
#         messages=[{"role": "user", "content": "What's the weather in London, UK?"}],
#         tools=[{
#             "type": "function",
#             "function": {
#                 "name": "get_current_weather",
#                 "description": "Get the current weather in a given location",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "location": {"type": "string", "description": "The city and state/country, e.g., London, UK"}
#                     },
#                     "required": ["location"]
#                 }
#             }
#         }]
#     )
#     print(response.choices[0].message.tool_calls)
    
# async def test_weather_tool():
#     result = await get_current_weather("London, UK")
#     print(result)




# if __name__ == "__main__":

#     # asyncio.run(test_gemini_tool())
#     # asyncio.run(test_weather_tool())