import asyncio
import logging
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

from setup.sender import Sender

## variable settings
token = settings.load_token()
Shelper = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(Shelper, storage=storage)
logging.basicConfig(level=logging.INFO)
gdz_plot = plot.Search_GDZ()


@dp.message_handler(commands=["start"])
async def start_message(message : types.Message):
    await message.answer("Wellcome(write later...)", reply_markup=keyBoard.start_inline_Keyboard)


@dp.callback_query_handler(lambda x: x.data == "start")
async def process_send_toMainMenu(callback_query: types.CallbackQuery):
    await Shelper.send_message(text="Бот активно тестируется, если у вас вознкнут проблемы или хотите дать пожелания, пишите @enfantc",
    chat_id=callback_query.from_user.id,
    reply_markup=keyBoard.start_reply_Keyboard)


@dp.message_handler(text=['Как использовать бота❔'])
async def process_start_solution(message: types.Message):
    await message.answer("Документации о использовании бота, на этапе написания...")


@dp.message_handler(text=['Найти решения🔍'])
async def process_start_solution(message: types.Message):
    await message.answer("Выбирете предмет", reply_markup=keyBoard.Subjects_reply_Keyboard)
    await gdz_plot.subject.set()


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Cancelled.', reply_markup=keyBoard.start_reply_Keyboard)

@dp.message_handler(state=gdz_plot.subject)
async def process_subject(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['subject'] = message.text
        startwith = await models.refactorDates.refactor_subject(data["subject"])
        if startwith == "geometria" or "fizika" or "algebra":
            await gdz_plot.next()
            await message.reply("Введите ваш класс", reply_markup=keyBoard.age7_reply_Keyboard)
        else:
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
        elif data["subject"] == "Физика📊":
            await message.answer("all ok")
            if data["class_"] == "11 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Phith11)    
            elif data["class_"] == "10 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Phith10)
            elif data["class_"] == "9 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Phith9)
            elif data["class_"] == "8 класс":
                await gdz_plot.next()
                await message.reply("Введите автора false", reply_markup=keyBoard.authors_reply_KeyBoard_geometry8)
            elif data["class_"] == "7 класс":
                await gdz_plot.next()
                await message.reply("Введите автора false", reply_markup=keyBoard.authors_reply_KeyBoard_geometry7)     
    else:
        await message.reply("Решения для предмета не были добавлены")

@dp.message_handler(state=gdz_plot.author)
async def process_author(messsage: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['author'] = messsage.text
    await gdz_plot.next()
    removeBtns = types.ReplyKeyboardRemove()
    await messsage.reply("Введите параграф\n(Если у вашего учебника нет параграфа, введите любое число, например: 0)", reply_markup=removeBtns)

@dp.message_handler(lambda message: not message.text.isdigit(), state=gdz_plot.prgh)
async def process_prgh_invalid(message: types.Message):
    return await message.reply("Вводить, нужно число")

@dp.message_handler(lambda message: message.text.isdigit(), state=gdz_plot.prgh)
async def process_prgh(messsage: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['prgh'] = messsage.text
    await gdz_plot.next()
    await messsage.answer("Введите номер")



@dp.message_handler(state=gdz_plot.number)
async def process_task_andComplte(message: types.Message, state:FSMContext):
    await Sender.send(Shelper=Shelper, message=message,  models=models, gdz_plot=gdz_plot,
     keyBoard=keyBoard, state=state, logging=logging)
                


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
