import asyncio
import logging
from pydoc import text
from tabnanny import check
import setup.setting as settings
import setup.keyboard as keyBoard
from admin import adminBoard as admin_board, comands 
from dates import db
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
from aiogram import Bot, Dispatcher, types
from aiogram.utils import exceptions, executor
from setup.sender import Sender

## variable settings
token = settings.load_token()
Shelper = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(Shelper, storage=storage)
logging.basicConfig(level=logging.INFO)
gdz_plot = plot.Search_GDZ()
log = logging.getLogger('broadcast')
admin_id = int(settings.load_id())

@dp.message_handler(commands=["start"])
async def start_message(message : types.Message):
    if message.from_user.id == admin_id:
        await message.answer("Добро пожаловать, в админ панель", reply_markup=admin_board.start_reply_Keyboard)
    else:
        await message.answer("Привет, жми Начать  использование скорее  ", reply_markup=keyBoard.start_inline_Keyboard)
        logging.info('Пользователь %r запустил бота %r', message.from_user.full_name, message.from_user.id)
        cheker =  db.db(message.from_user.first_name, message.from_user.id, True)
        await cheker.add()
        print("+1")
        
        

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
    
    await state.finish()
    await message.reply(f'Сценарий поиска отменен ', reply_markup=keyBoard.start_reply_Keyboard)

@dp.message_handler(state=gdz_plot.subject)
async def process_subject(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['subject'] = message.text
        startwith = await models.refactorDates.refactor_subject(data["subject"])
        logging.info("startwith: %r", startwith)
        if startwith == "russkii_yazik":
            await gdz_plot.next()
            await message.reply("Введите ваш класс", reply_markup=keyBoard.age_reply_Keyboard)
        else:
            await gdz_plot.next()   
            await message.reply("Введите ваш класс", reply_markup=keyBoard.age7_reply_Keyboard)

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
                await message.reply("Введите автора false", reply_markup=keyBoard.authors_reply_KeyBoard_Phith8)
            elif data["class_"] == "7 класс":
                await gdz_plot.next()
                await message.reply("Введите автора false", reply_markup=keyBoard.authors_reply_KeyBoard_Phith7) 
        elif data["subject"] == "Русский язык🖊":
            if data["class_"] == "11 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Russian11)    
            elif data["class_"] == "10 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Russian10)
            elif data["class_"] == "9 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Russian9)
            elif data["class_"] == "8 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Russian8)
            elif data["class_"] == "7 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Russian7)
            elif data["class_"] == "6 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Russian6)
            elif data["class_"] == "5 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_Russian5)     
        elif data["subject"] == "Английский 🇺🇸":
            if data["class_"] == "11 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_English11)    
            elif data["class_"] == "10 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_English10)
            elif data["class_"] == "9 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_English9)
            elif data["class_"] == "8 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_English8)
            elif data["class_"] == "7 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_English7)
            elif data["class_"] == "6 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_English6)
            elif data["class_"] == "5 класс":
                await gdz_plot.next()
                await message.reply("Введите автора", reply_markup=keyBoard.authors_reply_KeyBoard_English5)       
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
                










################################ADMIN##################################
@dp.message_handler(text="Статистика🛄")
async def send_stats_toAdmin(message: types.Message):
    cheker =  db.db(message.from_user.first_name, message.from_user.id, True)
    all_ = await cheker.send_all_count()
    ids = await cheker.send_all_user_id()
    await message.answer(f"Всего пользователей :  {all_}\n Id's: {ids}")


@dp.message_handler(text="Функции🎴")
async def send_stats_toAdmin(message: types.Message):
    await message.answer("...", reply_markup=admin_board.funcs_reply_keyboard)
    

def get_users(message: types.Message):
    checker =  db.db(message.from_user.first_name, message.from_user.id, True)
    ids = checker.send_all_user_id()

    print(ids)
    yield from (ids)


async def send_message(user_id: int, text: str, disable_notification: bool = False) -> bool:
    """
    Safe messages sender
    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await Shelper.send_message(user_id, text, disable_notification=disable_notification)
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        log.error(f"Target [ID:{user_id}]: Flood limit is exceeded. Sleep {e.timeout} seconds.")
        await asyncio.sleep(e.timeout)
        return await send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
    else:
        log.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def broadcaster() -> int:
    """
    Simple broadcaster
    :return: Count of messages
    """
    count = 0
    try:
        for user_id in get_users():
            if await send_message(user_id, '<b>Hello!</b>'):
                count += 1
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        logging.info(f"{count} messages successful sent.")

    return count

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
