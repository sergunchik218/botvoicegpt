import logging
from config import OPENAI_API_KEY, TELEGRAM_TOKEN, GROUP_ID
from aiogram import Bot, Dispatcher, executor, types
from services.converter import converter_text_to_voice, converter_ogg_to_wav
from services.services import get_chat_gpt_voice
from services.chat_gpt import send_text_chat_gpt
import os
import glob

API_TOKEN = TELEGRAM_TOKEN
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
 
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



#voice обработчик
@dp.message_handler(content_types=types.ContentType.VOICE)
async def handler_voice(message: types.Message):
    telegram_voice = await message.voice.get_file()
    voice_file = await bot.download_file(telegram_voice.file_path)
    voice = await get_chat_gpt_voice(telegram_voice, voice_file)
    await bot.send_voice(message.from_user.id, voice)

    file_list = glob.glob("*.wav")
    for file_path in file_list:
        os.remove(file_path)

# Словарь для хранения сессий пользователей
user_sessions = {}   
# Обработчик текстовых запросов
@dp.message_handler()
async def handler_text(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    previous_question = user_sessions.get(user_id)
    input_text = f"{previous_question} {text}" if previous_question else text
    text_response = await send_text_chat_gpt(input_text)
    response_message = text_response['choices'][0]['message']['content']
    user_sessions[user_id] = response_message
    voice = converter_text_to_voice(response_message)
    await bot.send_voice(user_id, voice)




# вывод бота
@dp.message_handler()
async def echo(message: types.Message):
    voice = converter_text_to_voice(message.text)
    await bot.send_voice(message.from_user.id, voice)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)