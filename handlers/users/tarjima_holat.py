from loader import db, bot, dp
from states.tarjimon import Translate
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from googletrans import Translator
from keyboards.inline.voice import voice
from aiogram.types import CallbackQuery
from keyboards.default.til_tan import menu

from gtts import gTTS
import os

def text_to_speech(mytext, lang):
    myobj = gTTS(text=mytext, lang=lang, slow=False)
    myobj.save("audio.mp3")



@dp.message_handler(state=Translate.trans)
async def translate_text(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    lang = data.get("lang")
    tarjimon = Translator()
    if lang == "🇺🇿 Uzb - 🇬🇧 Eng":
        tarjima = tarjimon.translate(text, dest="en")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="en")
    elif lang == "🇬🇧 Eng - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    elif lang == "🇺🇿 Uzb - 🇷🇺 Rus":
        tarjima = tarjimon.translate(text, dest="ru")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="ru")
    elif lang == "🇷🇺 Rus - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(text, dest="uz")
        await message.answer(tarjima.text, reply_markup=voice)
        text_to_speech(tarjima.text, lang="tr")
    await Translate.audio.set()
    # await state.finish()


@dp.callback_query_handler(text='voice', state=Translate.audio)
async def send_audio(call: CallbackQuery):
    await call.message.answer_audio(open("audio.mp3", 'rb'), reply_markup=menu)
    os.remove("audio.mp3")
    await Translate.lang.set()







