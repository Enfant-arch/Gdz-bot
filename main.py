import asyncio
from calendar import c
import logging
import os
from sys import path_hooks
import aiogram
import setup.setting as settings
import setup.keyboard as keyBoard
import models.plot as plot
import models.Gdz as solve 
from models.handler import handler
import models.refactorDates 
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import (InlineQuery, InlineQueryResultArticle,
                           InputTextMessageContent, ParseMode)



token = settings.load_token()
Shelper = Bot(token)
#use simple MemoryStorage for Dispatcher
storage = MemoryStorage()
dp = Dispatcher(Shelper, storage=storage)
logging.basicConfig(level=logging.INFO)
gdz_plot = plot.Search_GDZ()




@dp.message_handler(commands=["start"])
async def start_message(message : types.Message):
    await message.answer("Wellcome(write later...)", reply_markup=keyBoard.start_inline_Keyboard)


@dp.callback_query_handler(lambda x: x.data == "start")
async def process_search_solution(callback_query: types.CallbackQuery):
    await Shelper.send_message(text="Выберите предмет", chat_id=callback_query.from_user.id, reply_markup=keyBoard.Subjects_reply_Keyboard)
    await gdz_plot.subject.set()


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=gdz_plot.subject)
async def process_subject(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['subject'] = message.text

    await gdz_plot.next()
    await message.reply("Введите ваш класс", reply_markup=keyBoard.age_reply_Keyboard)


@dp.message_handler(state=gdz_plot.class_)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['class_'] = message.text
    Aon = await handler.add_or_not(data["subject"], data["class_"])
    if Aon == True:
        if data["subject"] == "Алгебра➕":
            if  data["class_"] == "11 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.autors_reply_Keyboard_algebra11)
            elif data["class_"] == "10 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.autors_reply_Keyboard_algebra10)
            elif data["class_"] == "9 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.autors_reply_Keyboard_algebra9)
            elif data["class_"] == "8 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.autors_reply_Keyboard_algebra8)
            elif data["class_"] == "7 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.autors_reply_Keyboard_algebra7)
        elif data["subject"] == "Геометрия📐":
            if data["class_"] == "11 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_geometry11)    
            elif data["class_"] == "10 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_geometry10)
            elif data["class_"] == "9 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_geometry9)
            elif data["class_"] == "8 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_geometry8)
            elif data["class_"] == "7 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_geometry7)   
    else:
        await message.reply("Решения для вашего класса не были добавленны")

@dp.message_handler(state=gdz_plot.author)
async def process_author(messsage: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['author'] = messsage.text
    await gdz_plot.next()
    removeBtns = types.ReplyKeyboardRemove()
    await messsage.reply("Введите параграф\n(Если у вашего учебника нет параграфа, введите любое число, например: 0)", reply_markup=removeBtns)

@dp.message_handler(lambda message: not message.text.isdigit(), state=gdz_plot.prgh)
async def process_prgh_invalid(message: types.Message):
    return await message.reply("Вводить нужно число")

@dp.message_handler(lambda message: message.text.isdigit(), state=gdz_plot.prgh)
async def process_prgh(messsage: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['prgh'] = messsage.text
    await gdz_plot.next()
    await messsage.answer("Введите номер")


@dp.message_handler(lambda message: not message.text.isdigit(), state=gdz_plot.number)
async def process_number_invalid(message: types.Message):
    return await message.reply("Вводить нужно число")


@dp.message_handler(state=gdz_plot.number)
async def process_task_andComplte(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['taskN'] = message.text
        logging.info("Начало парсинга работает")
        subject = await models.refactorDates.refactor_subject(data["subject"])
        class_ = await models.refactorDates.refactor_class_(data["class_"])
        prgh = data["prgh"]
        taskN = data["taskN"]
        #[REGION ALGEBRA11]
        if data["subject"] == "Алгебра➕" and data["class_" ] == "11 класс":
            author = await models.refactorDates.refactor_authors_11Algebra(data["author"])
            if author == "zadachnik-mordkovich":
                links = await solve.Algebra11.connect_for_Mordkovich(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "mordkovich_2009":
                links = await solve.Algebra11.connect_for_MordkovichBase(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "alimov":
                links = await solve.Algebra11.connect_for_Alimov(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "kolmogorov_2010":
                links = await solve.Algebra11.connect_for_Kilmogorov(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
        #[REGION ALGEBRA10]
        elif data["subject"] == "Алгебра➕" and data["class_" ] == "10 класс":
            author = await models.refactorDates.refactor_authors_10Algebra(data["author"])
            if author == "mordkovich_semenov":
                links = await solve.Algebra10.connect_for_Mordkovich(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "mordkovich_2009":
                links = await solve.Algebra10.connect_for_MordkovichBase(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "alimov":
                links = await solve.Algebra10.connect_for_Alimov(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "kolmogorov_2010":
                links = await solve.Algebra10.connect_for_Kilmogorov(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
        #[REGION ALGEBRA9]
        elif data["subject"] == "Алгебра➕" and data["class_" ] == "9 класс":
            author = await models.refactorDates.refactor_authors_9Algebra(data["author"])
            if author == "makarychev":
                links = await solve.Algebra9.connect_for_Makrichev(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "makarichev-uglublennoe-izuchenie":
                links = await solve.Algebra9.connect_for_Makrichev_uglubleniy(subject=subject, class_=class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "morodkovich":
                links = await solve.Algebra9.connect_for_Mordkovich(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "mordkovich-uglublennoe-izuchenie":
                links = await solve.Algebra9.connect_for_Mordkovich(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "merzlyak":
                links = await solve.Algebra9.connect_for_Merzlyak(subject=subject, class_=class_, author=author, taskN=taskN) 
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "merzlyak-polyakov":
                links = await solve.Algebra9.connect_for_Merzlyakublennoe(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
        #[REGION ALGEBRA8]
        elif data["subject"] == "Алгебра➕" and data["class_" ] == "8 класс":
            author = await models.refactorDates.refactor_authors_8Algebra(data["author"])
            if author == "makarychev_2012":
                links = await solve.Algebra8.connect_for_Makrichev(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "macarichev-uglublennij-uroven":
                links = await solve.Algebra8.connect_for_Makrichev_uglubleniy(subject=subject, class_=class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "morodkovich":
                links = await solve.Algebra8.connect_for_Mordkovich(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "mordkovich-uglublennyj-zadachnik":
                links = await solve.Algebra8.connect_for_mordkovichuglublennoe(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "merzlyak":
                links = await solve.Algebra8.connect_for_Merzlyak(subject=subject, class_=class_, author=author, taskN=taskN) 
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "merzlyak-polyakov":
                links = await solve.Algebra8.connect_for_Merzlyakublennoe(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "alimov_2012":
                links = await solve.Algebra8.connect_for_Alimov(subject=subject, class_=class_, author=author, taskN=taskN) 
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )

            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
        #[REGION ALGEBRA7]
        elif data["subject"] == "Алгебра➕" and data["class_" ] == "7 класс":
            author = await models.refactorDates.refactor_authors_7Algebra(data["author"])
            if author == "makarychev_2012":
                links = await solve.Algebra7.connect_for_Makrichev(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "dorofeev":
                links = await solve.Algebra7.connect_for_dorofeev(subject=subject, class_=class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "morodkovich":
                links = await solve.Algebra7.connect_for_Mordkovich(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "kolyagin-tkacheva":
                links = await solve.Algebra7.connect_for_kolyagin(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "merzlyak-polonskij-yakir":
                links = await solve.Algebra7.connect_for_Merzlyak(subject=subject, class_=class_, author=author, taskN=taskN) 
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "nikolskij":
                links = await solve.Algebra7.connect_for_nikolskij(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
         #[REGION GEOMETRIYA11]
        elif data["subject"] == "Геометрия📐" and data["class_" ] == "11 класс":
            author = await models.refactorDates.refactor_authors_11Geometry(data["author"])
            if author == "atanasjan":
                links = await solve.Geometry11.connect_to_atasyan(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "pogorelov":
                links = await solve.Geometry11.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
        
          #[REGION GEOMETRIYA10]
        elif data["subject"] == "Геометрия📐" and data["class_" ] == "10 класс":
            author = await models.refactorDates.refactor_authors_10Geometry(data["author"])
            if author == "atanasjan":
                links = await solve.Geometry10.connect_to_atasyan(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "pogorelov":
                links = await solve.Geometry10.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
         #[REGION GEOMETRIYA9]
        elif data["subject"] == "Геометрия📐" and data["class_" ] == "9 класс":
            author = await models.refactorDates.refactor_authors_9Geometry(data["author"])
            if author == "atanasjan":
                links = await solve.Geometry9.connect_to_atasyan(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                await send_PRGHsolution(links=links, subject=subject, class_=class_,prgh=prgh, author=author,taskN=taskN, message=message )
            elif author == "merzljak-polonskij":
                links = await solve.Geometry9.connect_to_polonskij(subject=subject, class_=class_, author=author,  taskN=taskN) 
                await send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message )
            elif author == "atanasyan":
                links = await solve.Geometry9.connect_to_atasyan_workNote(subject=subject, class_=class_, author=author,  taskN=taskN) 
                await send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message )
            elif author == "pogorelov":
                links = await solve.Geometry9.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
        elif data["subject"] == "Геометрия📐" and data["class_" ] == "8 класс":
            author = await models.refactorDates.refactor_authors_8Geometry(data["author"])
            if author == "atanasjan":
                links = await solve.Geometry8.connect_to_atasyan(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "merzlyak":
                links = await solve.Geometry8.connect_to_Mezlyak(subject=subject, class_=class_, author=author, taskN=taskN) 
                await send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message )
            elif author == "atanasyanWN":
                links = await solve.Geometry8.connect_to_atasyan_workNotek(subject=subject, class_=class_, author=author,  taskN=taskN) 
                await send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message )
            elif author == "pogorelov":
                links = await solve.Geometry8.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
        elif data["subject"] == "Геометрия📐" and data["class_" ] == "7 класс":
            author = await models.refactorDates.refactor_authors_11Geometry(data["author"])
            if author == "atanasjan":
                links = await solve.Geometry7.connect_to_atasyan(subject=subject, class_ = class_, author=author, taskN=taskN)
                await send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message )
            elif author == "merzljak-polonskij":
                links = await solve.Geometry7.connect_to_polonskij(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "atanasyan":
                links = await solve.Geometry7.connect_to_atasyan_workNote(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            elif author == "pogorelov":
                links = await solve.Geometry7.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                await send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message )
            else:
                await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")


        await state.finish()




@dp.message_handler(commands=["test"])
async def testring(message:types.Message):
    photo = open(r"models\file\task.jpg", 'rb')
    await Shelper.send_photo(chat_id=message.from_user.id,  photo=photo)



async def send_solution(links, subject, class_, author, taskN, message):
    for i in links:
        with open(f"models\\file\\{subject}\\{class_}\\{author}\\{taskN}\\{i}", 'rb') as photo:
            await Shelper.send_photo(
                chat_id= message.from_user.id,
                photo=photo,
                disable_notification = True
                )
    logging.info("Photos: %r", links)

async def send_PRGHsolution(links, subject, class_, author, prgh, taskN, message):
    for i in links:
        with open(f"models\\file\\{subject}\\{class_}\\{author}\\{prgh}\\{taskN}\\{i}", 'rb') as photo:
            await Shelper.send_photo(
                chat_id= message.from_user.id,
                photo=photo,
                disable_notification = True
                )
    logging.info("Photos: %r", links)
    return True

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
