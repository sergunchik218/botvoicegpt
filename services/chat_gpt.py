import aiohttp
from config import OPENAI_API_KEY


AITOKEN = OPENAI_API_KEY





async def send_data_chat_gpt(data: str):
    async with aiohttp.ClientSession() as session:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AITOKEN}"
        }
        body = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": data}]
        }
        async with session.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=body
        ) as response:
            return await response.json()

async def send_text_chat_gpt(text: str):
    async with aiohttp.ClientSession() as session:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AITOKEN}"
        }
        body = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": text}]
        }
        async with session.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=body
        ) as response:
            return await response.json()
        
