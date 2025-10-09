from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, set_tracing_disabled
import os
from dotenv import load_dotenv 
from openai import AsyncOpenAI


load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY IS NOT SET. PLEASE MAKE SURE IT IS.")


provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)
                      

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider
)

config = RunConfig(
    model = model,
    model_provider = provider,
    tracing_disabled= True
)