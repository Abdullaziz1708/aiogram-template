from aiogram import Dispatcher, Bot, types, executor
import logging
from config import token
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import requests
import wikipedia
from bs4 import BeautifulSoup as x
from kril import to_cyrillic, to_latin
from set import ketma_ket
from buttons import main, back, knopka, back1, shahar
from set import ketma_ket
from botlar import bottttt
from sayt import saytlar
from kanal import kanallar
from googletrans import Translator
translate1 = Translator()
wikipedia.set_lang("uz")
logging.basicConfig(level=logging.INFO)
bot=Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"], state='*')
async def start_send(message: types.Message,state: FSMContext):
    name = message.from_user.first_name
    familiya=message.from_user.last_name
    id=message.from_user.id
    usname=message.from_user.username
    await message.answer(f"Ismingiz:{name}\nFamiliyangiz:{familiya}\nID:{id}\nUsername:{usname}\nBotimizga xush kelibsiz!", reply_markup=main)
    await message.delete()
@dp.callback_query_handler(text='val',state='*')
async def dollar(call: types.CallbackQuery):
    urs=requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/uzs.json")
    data=urs.json()
    dol=data['uzs']
    kun=data['date']
    urs1=requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/uzs.json")
    data1=urs1.json()
    dol1=data1['uzs']
    urs2=requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/rub/uzs.json")
    data2=urs2.json()
    dol2=data2['uzs']
    urs3=requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/aed/uzs.json")
    data3=urs3.json()
    dol3=data3['uzs']
    urs4=requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/cny/uzs.json")
    data4=urs4.json()
    dol4=data4['uzs']
    urs5=requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/krw/uzs.json")
    data5=urs5.json()
    dol5=data5['uzs']  
    await call.message.answer(f"{kun} kuni bo'yicha:\n1 $ ={dol} sum\n1 € = {dol1} sum\n1 £ = {dol2} sum\n1 dirham = {dol3} sum\n1 yuan = {dol4} sum\n1 von = {dol5} sum",reply_markup=back)
    await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu(call: types.CallbackQuery, state=FSMContext):
    ism = call.message.from_user.first_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main) 
    await call.message.delete()

@dp.callback_query_handler(text='mal',state='*')
async def info_send(call: types.CallbackQuery):
    await call.message.answer(f"Qaysi mavzudan ma'lumot olishni istaysiz?")
    await ketma_ket.davomi.set()
    await call.message.delete()
    
@dp.message_handler(state=ketma_ket.davomi)
async def malumot(message: types.Message):
    xabar=message.text
    try:
        maqola=wikipedia.summary(xabar)
        await message.reply(f"Siz izlagan ma\'lumot\n{maqola}",reply_markup=back)
        await message.delete()
    except:
        await message.reply("Siz so'ragan ma'lumot topilmadi!",reply_markup=back)
        await ketma_ket.finish()
        await message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu2(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()
    
    
    
    
@dp.callback_query_handler(text='kl',state='*')
async def pogoda(call: types.CallbackQuery):
    await call.message.answer(f"Qaysi hududning ob-havosi kerak?",reply_markup=shahar)
    await call.message.delete()
    
@dp.callback_query_handler(text='tosh')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-ташкент")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data=i.select(".date")[0].text
        month=i.select(".month")[0].text
        min=i.select(".min")[0].text
        max=i.select(".max")[0].text
        xabar = call.message.text
        if month.isascii() and min.isascii() and max.isascii():
            text1 = to_cyrillic(month)
            text2 = to_cyrillic(min)
            text3 = to_cyrillic(max)
            await call.message.answer(f"mana:{data}{text1}{text2}{text3}",reply_markup=back)
            await call.message.delete()
        else:
            text4 = to_latin(month)
            text5 = to_latin(min)
            text6 = to_latin(max)
            await call.message.answer(f"Sana: {data} {text4} \n{text5}\n{text6}",reply_markup=back)
            await call.message.delete()
        
@dp.callback_query_handler(text='ortga',state='*')
async def menyu3(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='andi')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-андижан")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data1=i.select(".date")[0].text
        month1=i.select(".month")[0].text
        min1=i.select(".min")[0].text
        max1=i.select(".max")[0].text
        if month1.isascii() and min1.isascii() and max1.isascii():
            text11 = to_cyrillic(month1)
            text21 = to_cyrillic(min1)
            text31 = to_cyrillic(max1)
            await call.message.answer(f"mana:{data1}{text11}{text21}{text31}",reply_markup=back)
        else:
            text41 = to_latin(month1)
            text51 = to_latin(min1)
            text61 = to_latin(max1)
            await call.message.answer(f"Sana: {data1} {text41} \n{text51}\n{text61}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu4(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='sam')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-самарканд")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data2=i.select(".date")[0].text
        month2=i.select(".month")[0].text
        min2=i.select(".min")[0].text
        max2=i.select(".max")[0].text
        if month2.isascii() and min2.isascii() and max2.isascii():
            text12 = to_cyrillic(month2)
            text22 = to_cyrillic(min2)
            text32 = to_cyrillic(max2)
            await call.message.answer(f"mana:{data2}{text12}{text22}{text32}",reply_markup=back)
        else:
            text42 = to_latin(month2)
            text52 = to_latin(min2)
            text62 = to_latin(max2)
            await call.message.answer(f"Sana: {data2} {text42} \n{text52}\n{text62}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu5(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='sir')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-сырдарья")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data3=i.select(".date")[0].text
        month23=i.select(".month")[0].text
        min23=i.select(".min")[0].text
        max23=i.select(".max")[0].text
        if month23.isascii() and min23.isascii() and max23.isascii():
            text13 = to_cyrillic(month23)
            text23 = to_cyrillic(min23)
            text33 = to_cyrillic(max23)
            await call.message.answer(f"mana:{data3}{text13}{text23}{text33}",reply_markup=back)
        else:
            text43 = to_latin(month23)
            text53 = to_latin(min23)
            text63 = to_latin(max23)
            await call.message.answer(f"Sana: {data3} {text43} \n{text53}\n{text63}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu6(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='nuk')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-нукус")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data4=i.select(".date")[0].text
        month24=i.select(".month")[0].text
        min24=i.select(".min")[0].text
        max24=i.select(".max")[0].text
        if month24.isascii() and min24.isascii() and max24.isascii():
            text14 = to_cyrillic(month24)
            text24 = to_cyrillic(min24)
            text34 = to_cyrillic(max24)
            await call.message.answer(f"mana:{data4}{text14}{text24}{text34}",reply_markup=back)
        else:
            text44 = to_latin(month24)
            text54 = to_latin(min24)
            text64 = to_latin(max24)
            await call.message.answer(f"Sana: {data4} {text44} \n{text54}\n{text64}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu7(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='nam')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-наманган")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data5=i.select(".date")[0].text
        month25=i.select(".month")[0].text
        min25=i.select(".min")[0].text
        max25=i.select(".max")[0].text
        if month25.isascii() and min25.isascii() and max25.isascii():
            text15 = to_cyrillic(month25)
            text25 = to_cyrillic(min25)
            text35 = to_cyrillic(max25)
            await call.message.answer(f"mana:{data5}{text15}{text25}{text35}",reply_markup=back)
        else:
            text45 = to_latin(month25)
            text55 = to_latin(min25)
            text65 = to_latin(max25)
            await call.message.answer(f"Sana: {data5} {text45} \n{text55}\n{text65}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu8(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='ur')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-ургенч")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data6=i.select(".date")[0].text
        month26=i.select(".month")[0].text
        min26=i.select(".min")[0].text
        max26=i.select(".max")[0].text
        if month26.isascii() and min26.isascii() and max26.isascii():
            text16 = to_cyrillic(month26)
            text26 = to_cyrillic(min26)
            text36 = to_cyrillic(max26)
            await call.message.answer(f"Sana: {data6}{text16} \n{text26}\n{text36}",reply_markup=back)
        else:
            text46 = to_latin(month26)
            text56 = to_latin(min26)
            text66 = to_latin(max26)
            await call.message.answer(f"Sana: {data6} {text46} \n{text56}\n{text66}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu9(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='gul')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-гулистан")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data7=i.select(".date")[0].text
        month27=i.select(".month")[0].text
        min27=i.select(".min")[0].text
        max27=i.select(".max")[0].text
        if month27.isascii() and min27.isascii() and max27.isascii():
            text17 = to_cyrillic(month27)
            text27 = to_cyrillic(min27)
            text37 = to_cyrillic(max27)
            await call.message.answer(f"Sana: {data7}{text17} \n{text27}\n{text37}",reply_markup=back)
        else:
            text47 = to_latin(month27)
            text57 = to_latin(min27)
            text67 = to_latin(max27)
            await call.message.answer(f"Sana: {data7} {text47} \n{text57}\n{text67}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu10(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='jiz')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-джизак")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data8=i.select(".date")[0].text
        month28=i.select(".month")[0].text
        min28=i.select(".min")[0].text
        max28=i.select(".max")[0].text
        if month28.isascii() and min28.isascii() and max28.isascii():
            text18 = to_cyrillic(month28)
            text28 = to_cyrillic(min28)
            text38 = to_cyrillic(max28)
            await call.message.answer(f"Sana: {data8}{text18} \n{text28}\n{text38}",reply_markup=back)
        else:
            text48 = to_latin(month28)
            text58 = to_latin(min28)
            text68 = to_latin(max28)
            await call.message.answer(f"Sana: {data8} {text48} \n{text58}\n{text68}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu11(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()



@dp.callback_query_handler(text='qon')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-кунград")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data9=i.select(".date")[0].text
        month9=i.select(".month")[0].text
        min9=i.select(".min")[0].text
        max9=i.select(".max")[0].text

        if month9.isascii() and min9.isascii() and max9.isascii():
            text9 = to_cyrillic(month9)
            text29 = to_cyrillic(min9)
            text39 = to_cyrillic(max9)
            await call.message.answer(f"mana:{data9}{text9}{text29}{text39}",reply_markup=back)
        else:
            text49 = to_latin(month9)
            text59 = to_latin(min9)
            text69 = to_latin(max9)
            await call.message.answer(f"Sana: {data9} {text49} \n{text59}\n{text69}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu12(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='tem')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-термез")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data0=i.select(".date")[0].text
        month0=i.select(".month")[0].text
        min0=i.select(".min")[0].text
        max0=i.select(".max")[0].text
        if month0.isascii() and min0.isascii() and max0.isascii():
            texta = to_cyrillic(month0)
            text2a = to_cyrillic(min0)
            text3a = to_cyrillic(max0)
            await call.message.answer(f"mana:{data0}{texta}{text2a}{text3a}",reply_markup=back)
        else:
            text4a = to_latin(month0)
            text5a = to_latin(min0)
            text6a = to_latin(max0)
            await call.message.answer(f"Sana: {data0} {text4a} \n{text5a}\n{text6a}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu13(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()


@dp.callback_query_handler(text='qar')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-карши")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data5q=i.select(".date")[0].text
        month25q=i.select(".month")[0].text
        min25q=i.select(".min")[0].text
        max25q=i.select(".max")[0].text
        if month25q.isascii() and min25q.isascii() and max25q.isascii():
            text15q = to_cyrillic(month25q)
            text25q = to_cyrillic(min25q)
            text35q = to_cyrillic(max25q)
            await call.message.answer(f"mana:{data5q}{text15q}{text25q}{text35q}",reply_markup=back)
        else:
            text45q = to_latin(month25q)
            text55q = to_latin(min25q)
            text65q = to_latin(max25q)
            await call.message.answer(f"Sana: {data5q} {text45q} \n{text55q}\n{text65q}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu14(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='nav')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-навои")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        dataq=i.select(".date")[0].text
        monthq=i.select(".month")[0].text
        minq=i.select(".min")[0].text
        maxq=i.select(".max")[0].text
        if monthq.isascii() and minq.isascii() and maxq.isascii():
            textq1 = to_cyrillic(monthq)
            textq2 = to_cyrillic(minq)
            textq3 = to_cyrillic(maxq)
            await call.message.answer(f"mana:{dataq}{textq1}{textq2}{textq3}",reply_markup=back)
        else:
            textq4 = to_latin(monthq)
            textq5 = to_latin(minq)
            textq6 = to_latin(maxq)
            await call.message.answer(f"Sana: {dataq} {textq4} \n{textq5}\n{textq6}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu15(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='sha')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-шахрисабз")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data3q=i.select(".date")[0].text
        month2q3=i.select(".month")[0].text
        min2q3=i.select(".min")[0].text
        max2q3=i.select(".max")[0].text
        if month2q3.isascii() and min2q3.isascii() and max2q3.isascii():
            text1q3 = to_cyrillic(month2q3)
            text2q3 = to_cyrillic(min2q3)
            text3q3 = to_cyrillic(max2q3)
            await call.message.answer(f"mana:{data3q}{text1q3}{text2q3}{text3q3}",reply_markup=back)
        else:
            text43q = to_latin(month2q3)
            text53q = to_latin(min2q3)
            text63q = to_latin(max2q3)
            await call.message.answer(f"Sana: {data3q} {text43q} \n{text53q}\n{text63q}",reply_markup=back)
            await call.message.delete()
@dp.callback_query_handler(text='ortga',state='*')
async def menyu16(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()

@dp.callback_query_handler(text='yan')
async def toshk(call: types.CallbackQuery):
    url=requests.get("https://sinoptik.ua/погода-янги-маргилан")
    html_t=x(url.content, "html.parser")
    for i in html_t.select("#content"):
        data4q=i.select(".date")[0].text
        month24q=i.select(".month")[0].text
        min24q=i.select(".min")[0].text
        max24q=i.select(".max")[0].text
        if month24q.isascii() and min24q.isascii() and max24q.isascii():
            text14q = to_cyrillic(month24q)
            text24q = to_cyrillic(min24q)
            text34q = to_cyrillic(max24q)
            await call.message.answer(f"mana:{data4q}{text14q}{text24q}{text34q}",reply_markup=back)
        else:
            text44q = to_latin(month24q)
            text54q = to_latin(min24q)
            text64q = to_latin(max24q)
            await call.message.answer(f"Sana: {data4q} {text44q} \n{text54q}\n{text64q}",reply_markup=back)
            await call.message.delete()
            
@dp.callback_query_handler(text='ortga',state='*')
async def menyu17(call: types.CallbackQuery):
    ism = call.message.from_user.full_name
    await call.message.answer(f"Salom👋.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()









@dp.callback_query_handler(text='fsah',state='*')
async def sah(call: types.CallbackQuery):
    await call.message.answer("Iltimos tanlang",reply_markup=knopka)
    await call.message.delete()
@dp.callback_query_handler(text='backkk',state='*')
async def oq(call: types.CallbackQuery):
    await call.message.answer(f"Salom.\nBotimizga xush kelibsiz!",reply_markup=main)
    await call.message.delete()
@dp.callback_query_handler(text='bottt',state='*')
async def bttt(call: types.CallbackQuery):
    bottob=bottttt
    await call.message.answer(f"Mana marhamat:\n{bottob}",reply_markup=back1)
    await call.message.delete()
@dp.callback_query_handler(text='orqaga',state='*')
async def oq1(call: types.CallbackQuery):
    await call.message.answer("Iltimos tanlang",reply_markup=knopka)
    await call.message.delete()
@dp.callback_query_handler(text='kanal',state='*')
async def knll(call: types.CallbackQuery):
    kanal=kanallar
    await call.message.answer(f"Mana marhamat:\n{kanal}",reply_markup=back1)
    await call.message.delete()
    
@dp.callback_query_handler(text='orqaga',state='*')
async def oq2(call: types.CallbackQuery):
    await call.message.answer("Iltimos tanlang",reply_markup=knopka)
    await call.message.delete()
    
@dp.callback_query_handler(text='sayt',state='*')
async def syttt(call: types.CallbackQuery):
    sayt=saytlar
    await call.message.answer(f"Mana marhamat:\n{sayt}",reply_markup=back1)
    await call.message.delete()
@dp.callback_query_handler(text='orqaga',state='*')
async def oq3(call: types.CallbackQuery):
    await call.message.answer("Iltimos tanlang",reply_markup=knopka)
    await call.message.delete()













































































if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
    
    
    
    
