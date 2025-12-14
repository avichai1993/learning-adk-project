# import os
# import asyncio
# from google.adk.agents import Agent
# # from google.adk.agents.llm_agent import Agent
# from google.adk.models.lite_llm import LiteLlm  # For multi-model support
# from google.adk.sessions import InMemorySessionService
# from google.adk.runners import Runner
# from google.genai import types
# import litellm  # Import for proxy configuration

# # Set your API keys
# os.environ["GOOGLE_API_KEY"] = "your-google-api-key"  # For Gemini models
# os.environ["OPENAI_API_KEY"] = "your-openai-api-key"  # For OpenAI models
# os.environ["LITE_LLM_API_KEY"] = "your-anthropic-api-key"  # For Claude models

# # Define model constants for cleaner code
# MODEL_GPT_5 = "openai/gpt-5"
# MODEL_CLAUDE_SONNET = "anthropic/claude-3-sonnet-20240229"

# root_agent = Agent(
#     model=MODEL_GPT_5,
#     name='root_agent',
#     description="Tells the current time in a specified city.",
#     instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
#     tools=[get_current_time],
# )


