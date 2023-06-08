from io import BytesIO
import os
from aiogram.types import File
from services.converter import (
    converter_ogg_to_wav,
    converter_text_to_voice,
    converter_voice_to_text
)
from services.chat_gpt import send_data_chat_gpt, send_text_chat_gpt
from utils import chat_gpt_response_to_text



async def get_chat_gpt_voice(
    telegram_voice: File, 
    downloaded_voice: BytesIO
) -> BytesIO:
        path = converter_ogg_to_wav(telegram_voice.file_path, downloaded_voice)
        text = converter_voice_to_text(path)
        chat_gpt_response = await send_data_chat_gpt(text)
        chat_gpt_text = chat_gpt_response['choices'][0]['message']['content']
        voice = converter_text_to_voice(chat_gpt_text)
        return voice
   



