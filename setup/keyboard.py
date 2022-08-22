from ctypes import resize
from aiogram.types import (InlineQuery, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle,
                           InputTextMessageContent, ReplyKeyboardMarkup, KeyboardButton)


###****************Start BTN-s ***************###
start_inline_aboutbtn = InlineKeyboardButton("О боте🌐 ", url="https://google.com")
start_inline_support_author = InlineKeyboardButton("Поддержать 💸", url="http://qiwi.com/n/CLUME911")
start_inline_LetUsingBot = InlineKeyboardButton("Начать использование▶️", callback_data="start")
start_inline_Keyboard = InlineKeyboardMarkup(row_width=3).add(start_inline_aboutbtn,
                                                             start_inline_support_author,
                                                            start_inline_LetUsingBot)
start_reply_search_Task = KeyboardButton("Найти решения🔍")
start_reply_how_use = KeyboardButton("Как использовать бота❔")
start_reply_Keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(start_reply_search_Task, start_reply_how_use)
ToStartReply = KeyboardButton('🔙Главное меню')
other_numbers = KeyboardButton("Другой номер")
other_solution = KeyboardButton("Другое решение")
AE_replyKeyBoard = ReplyKeyboardMarkup(resize_keyboard=True).add(other_numbers, ToStartReply, other_solution) 
#************************************************#
###****************Subjects***************###
'''
russian = KeyboardButton("Русский язык")
math = KeyboardButton("Математика")
english = KeyboardButton("Английский язык")
'''
algebra = KeyboardButton("Алгебра➕")
geometry = KeyboardButton("Геометрия📐")
phizika = KeyboardButton("Физика📊")
'''
chemestry = KeyboardButton("Химия")
Desutchland_lang = KeyboardButton("Немецкий язык")
Ukrainskiy_lang = KeyboardButton("Украинский язык")
Franch_lang = KeyboardButton("Французский язык")
Biology = KeyboardButton("Биология")
History = KeyboardButton("История")
computer_since = KeyboardButton("Информатика")
obj = KeyboardButton("ОБЖ")
Geogrphy = KeyboardButton("География")
nature_lidding = KeyboardButton("Природоведение ")
music = KeyboardButton("Музыка")
litirature = KeyboardButton("Литература")
social_scince = KeyboardButton("Обществознание")
drawing = KeyboardButton("Черчение")
envirement_world = KeyboardButton("Окружающий мир")
ecology = KeyboardButton("Экология")
technology = KeyboardButton("Технология")
natural_science = KeyboardButton("Естествознание")
Spain_lang = KeyboardButton("Испанский язык")
Art = KeyboardButton("Искусство")
China_lang = KeyboardButton("Китайский язык")
cuba = KeyboardButton(" Кубановедение")
Kazah_lang = KeyboardButton("Казахский язык")
world_ofNatrueAndHuman = KeyboardButton("Мир природы и человека")
'''


Subjects_reply_Keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    #russian, math, english,
    algebra, geometry, phizika
    #chemestry, Desutchland_lang, Ukrainskiy_lang,
    #Franch_lang, Biology, History,
    #computer_since, obj, Geogrphy,
    #nature_lidding, music, litirature,
    #social_scince, drawing, envirement_world,
    #ecology, technology, natural_science, Spain_lang,
    #Art, China_lang, cuba, Kazah_lang, world_ofNatrueAndHuman
)
#************************************************#
###****************classes***************###
class11 = KeyboardButton("11 класс")
class10 = KeyboardButton("10 класс")
class9 = KeyboardButton("9 класс")
class8 = KeyboardButton("8 класс")
class7 = KeyboardButton("7 класс")
class6 = KeyboardButton("6 класс")
class5 = KeyboardButton("5 класс")
'''
class4 = KeyboardButton("4 класс")
class3 = KeyboardButton("3 класс")
class2 = KeyboardButton("2 класс")
class1 = KeyboardButton("1 класс")
'''
age_reply_Keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    #class1, class2, class3, class4,
    class5, class6,
    class7, class8, class9,
    class10, class11
)

#####Start with 7 class
age7_reply_Keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    class7, class8, class9,
    class10, class11
)


#************************************************#
###****************Authors***************###
###****************ALGEBRA***************###
###****************Algebra11***************###
author_algebra_11_1 = KeyboardButton("Мордкович")
author_algebra_11_2 = KeyboardButton("Мордкович базовый")
author_algebra_11_3 = KeyboardButton("Алимов")
author_algebra_11_4 = KeyboardButton("Колмогоров")
autors_reply_Keyboard_algebra11 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_algebra_11_1, author_algebra_11_2, author_algebra_11_3, 
    author_algebra_11_4
)
###***************************************###
###****************Algebra10***************###
author_algebra_10_1 = KeyboardButton("Мордкович")
author_algebra_10_2 = KeyboardButton("Мордкович базовый")
author_algebra_10_3 = KeyboardButton("Алимов")
author_algebra_10_4 = KeyboardButton("Колмогоров")
autors_reply_Keyboard_algebra10 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_algebra_10_1, author_algebra_10_2, author_algebra_10_3, 
    author_algebra_10_4
)
###***************************************###
###****************Algebra9***************###
author_algebra_9_1 = KeyboardButton("Макарычев")
author_algebra_9_2 = KeyboardButton("Макарычев Углубленный")
author_algebra_9_3 = KeyboardButton("Мордкович Углубленный")
author_algebra_9_4 = KeyboardButton("Мордкович")
author_algebra_9_5 = KeyboardButton("Мерзляк")
author_algebra_9_6 = KeyboardButton("Мерзляк Углубленный")
autors_reply_Keyboard_algebra9 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_algebra_9_1, author_algebra_9_2, author_algebra_9_3, 
    author_algebra_9_4, author_algebra_9_5, author_algebra_9_6
)
###****************Algebra8***************###
author_algebra_8_1 = KeyboardButton("Макарычев")
author_algebra_8_2 = KeyboardButton("Макарычев Углубленный")
author_algebra_8_3 = KeyboardButton("Мордкович Углубленный")
author_algebra_8_4 = KeyboardButton("Мордкович")
author_algebra_8_5 = KeyboardButton("Мерзляк")
author_algebra_8_6 = KeyboardButton("Мерзляк Углубленный")
author_algebra_8_7 = KeyboardButton("Алимов")

###***************************************###

autors_reply_Keyboard_algebra8 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_algebra_8_1, author_algebra_8_2, author_algebra_8_3, 
    author_algebra_8_4, author_algebra_8_5, author_algebra_8_6,
    author_algebra_8_7
)

###****************Algebra7***************###
author_algebra_7_1 = KeyboardButton("Макарычев")
author_algebra_7_2 = KeyboardButton("Дорофеев")
author_algebra_7_3 = KeyboardButton("Колягин")
author_algebra_7_4 = KeyboardButton("Мордкович")
author_algebra_7_5 = KeyboardButton("Мерзляк")
author_algebra_7_6 = KeyboardButton("Никольский")
autors_reply_Keyboard_algebra7 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_algebra_7_1, author_algebra_7_2, author_algebra_7_3, 
    author_algebra_7_4, author_algebra_7_5, author_algebra_7_6
)
###***************************************###
###****************GEOMETRY***************###
###****************Geometry11***************###
author_geometry_11_1 = KeyboardButton("Атанасян")
author_geometry_11_2 = KeyboardButton("Погорелов")
#author_geometry_11_3 = KeyboardButton("Александров")
#author_geometry_11_4 = KeyboardButton("Александров углубленный")
authors_reply_KeyBoard_geometry11 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_geometry_11_1, author_geometry_11_2, #author_geometry_11_3,
    #author_geometry_11_4
)

###****************Geometry10***************###
author_geometry_10_1 = KeyboardButton("Атанасян")
author_geometry_10_2 = KeyboardButton("Погорелов")
#author_geometry_11_3 = KeyboardButton("Александров")
#author_geometry_11_4 = KeyboardButton("Александров углубленный")
authors_reply_KeyBoard_geometry10 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_geometry_10_1, author_geometry_10_2, #author_geometry_11_3,
    #author_geometry_11_4
)

###****************Geometry9***************###
author_geometry_9_1 = KeyboardButton("Атанасян")
author_geometry_9_2 = KeyboardButton("Погорелов")
author_geometry_9_3 = KeyboardButton("Атанасян раб. тетрадь")
author_geometry_9_4 = KeyboardButton("Полонский")
authors_reply_KeyBoard_geometry9 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_geometry_9_1, author_geometry_9_2, author_geometry_9_3,
    author_geometry_9_4
)

###****************Geometry8***************###
author_geometry_8_1 = KeyboardButton("Атанасян")
author_geometry_8_2 = KeyboardButton("Мерзляк")
author_geometry_8_3 = KeyboardButton("Атанасян раб. тетрадь")
author_geometry_8_4 = KeyboardButton("Погорелов")
authors_reply_KeyBoard_geometry8 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_geometry_8_1, author_geometry_8_2, author_geometry_8_3,
    author_geometry_8_4
)

###****************Geometry7***************###
author_geometry_7_1 = KeyboardButton("Атанасян")
author_geometry_7_2 = KeyboardButton("Мерзляк")
author_geometry_7_3 = KeyboardButton("Мерзляк раб. тетрадь")
author_geometry_7_4 = KeyboardButton("Погорелов")
authors_reply_KeyBoard_geometry7 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_geometry_7_1, author_geometry_7_2, author_geometry_7_3,
    author_geometry_7_4
)
###****************PHITH***************###
###****************Phith11***************###
author_phith_11_1 = KeyboardButton("Задачник Рымкевич")
author_phith_11_2 = KeyboardButton("Степанов Сборник задач")
author_phith_11_3 = KeyboardButton("Парфентьева Сборник задач")
author_phith_11_4 = KeyboardButton("Громов")
authors_reply_KeyBoard_Phith11 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_phith_11_1, author_phith_11_2, author_phith_11_3,
    author_phith_11_4
)

###****************Phith10***************###
author_phith_10_1 = KeyboardButton("Мякишев")
author_phith_10_2 = KeyboardButton("Рымкевич")
#author_phith_10_3 = KeyboardButton("Александров")
#author_phith_10_4 = KeyboardButton("Александров углубленный")
authors_reply_KeyBoard_Phith10 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_phith_10_1, author_phith_10_2 #author_phith_10_3,
    #author_phith_10_4
)

###****************Phith9***************###
author_phith_9_1 = KeyboardButton("Атанасян")
author_phith_9_2 = KeyboardButton("Погорелов")
author_phith_9_3 = KeyboardButton("Атанасян раб. тетрадь")
author_phith_9_4 = KeyboardButton("Полонский")
authors_reply_KeyBoard_Phith9 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_phith_9_1, author_phith_9_2, author_phith_9_3,
    author_phith_9_4
)

###****************Phith8***************###
author_geometry_11_1 = KeyboardButton("Атанасян")
author_geometry_11_2 = KeyboardButton("Мерзляк")
author_geometry_11_3 = KeyboardButton("Атанасян раб. тетрадь")
author_geometry_11_4 = KeyboardButton("Погорелов")
authors_reply_KeyBoard_geometry8 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_geometry_11_1, author_geometry_11_2, author_geometry_11_3,
    author_geometry_11_4
)

###****************Phith7***************###
author_geometry_11_1 = KeyboardButton("Атанасян")
author_geometry_11_2 = KeyboardButton("Мерзляк")
author_geometry_11_3 = KeyboardButton("Мерзляк раб. тетрадь")
author_geometry_11_4 = KeyboardButton("Погорелов")
authors_reply_KeyBoard_geometry7 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    author_geometry_11_1, author_geometry_11_2, author_geometry_11_3,
    author_geometry_11_4
)
