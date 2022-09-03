import statistics
from aiogram.types import (InlineQuery, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle,
                           InputTextMessageContent, ReplyKeyboardMarkup, KeyboardButton)
statistic = KeyboardButton("Статистика🛄")
funcs = KeyboardButton("Функции🎴")
start_reply_Keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(statistic, funcs)