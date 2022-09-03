import cv2
import numpy as np
import asyncio


async def refactor_subject(subject):

    if subject == "Математика":
        return "matematika"

    elif subject == "Английский язык":
        return "english"

    elif subject == "Русский язык🖊":
        return "russkii_yazik"

    elif subject == "Алгебра➕":
        return "algebra"
    elif subject == "Геометрия📐":
        return "geometria"

    elif subject == "Физика📊":
        return "fizika"

    elif subject == "Химия":
        return "himiya"

    elif subject == "Немецкий язык":
        return "nemeckiy_yazik"

    elif subject == "Украинский язык":
        return "ukrainskiy_yazik"

    elif subject == "Французский язык":
        return "francuzskiy_yazik"

    elif subject == "Биология":
        return "biologiya"

    elif subject == "История":
        return "istoriya"

    elif subject == "Информатика":
        return "informatika"

    elif subject == "ОБЖ":
        return "obj"

    elif subject == "География":
        return "geografiya"

async def refactor_class_(class_):
    if class_ == "11 класс":
        return "11"
    elif class_ == "10 класс":
        return "10"
    elif class_ == "9 класс":
        return "9"
    elif class_=="8 класс":
        return "8"
    elif class_=="7 класс":
        return "7"
    elif class_=="6 класс":
        return "6"
    elif class_=="5 класс":
        return "5"


async def refactor_authors_11Algebra(author):
    if author == "Колмогоров":
        return "kolmogorov_2010"
    elif author == "Мордкович базовый":
        return "mordkovich_2009"
    elif author == "Мордкович":
        return "zadachnik-mordkovich"
    elif author == "Алимов":
        return "alimov"

async def refactor_authors_10Algebra(author):
    if author == "Мордкович":
        return "mordkovich_semenov"

    elif author == "Мордкович базовый":
        return "mordkovich_2009"
    elif author == "Алимов":
        return "alimov"
    elif author == "Колмогоров":
        return "kolmogorov_2010"

async def refactor_authors_9Algebra(author):
    if author == "Макарычев":
        return "makarychev"
    elif author == "Макарычев Углубленный":
        return "makarichev-uglublennoe-izuchenie"
    elif author == "Мордкович":
        return "morodkovich"
    elif author == "Мордкович Углубленный":
        return "mordkovich-uglublennoe-izuchenie"
    elif author == "Мерзляк":
        return "merzlyak"
    elif author == "Мерзляк Углубленный":
        return "merzlyak-polyakov"

async def refactor_authors_8Algebra(author):
    if author == "Макарычев":
        return "makarychev_2012"
    elif author == "Макарычев Углубленный":
        return "macarichev-uglublennij-uroven"
    elif author == "Мордкович":
        return "morodkovich"
    elif author == "Мордкович Углубленный":
        return "mordkovich-uglublennyj-zadachnik"
    elif author == "Мерзляк":
        return "merzlyak"
    elif author == "Мерзляк Углубленный":
        return "merzlyak-polyakov"
    elif author == "Алимов":
        return "alimov_2012"

async def refactor_authors_7Algebra(author):
    if author == "Макарычев":
        return "makarychev_2012"
    elif author == "Дорофеев":
        return "dorofeev"
    elif author == "Мордкович":
        return "mordkovich"
    elif author == "Колягин":
        return "kolyagin-tkacheva"
    elif author == "Мерзляк":
        return "merzlyak-polonskij-yakir"
    elif author == "Никольский":
        return "nikolskij"
    
async def refactor_authors_11Geometry(author):
    if author == "Атанасян":
        return "atanasjan"
    elif author == "Погорелов":
        return "pogorelov"
    #elif author == "Александров":
        return "kolyagin-tkacheva"
    #elif author == "Александров углубленный":
        return "merzlyak-polonskij-yakir"
async def refactor_authors_10Geometry(author):
    if author == "Атанасян":
        return "atanasjan"
    elif author == "Погорелов":
        return "pogorelov"

async def refactor_authors_9Geometry(author):
    if author == "Атанасян":
        return "atanasjan"
    elif author == "Мрезляк":
        return "merzljak-polonskij"
    elif author == "Атанасян раб. тетрадь":
        return "atanasyan"
    elif author == "Погорелов":
        return "pogorelov"

async def refactor_authors_8Geometry(author):
    if author == "Атанасян":
        return "atanasjan"
    elif author == "Мерзляк":
        return "merzlyak"
    elif author == "Атанасян раб. тетрадь":
        return "atanasyanWN"
    elif author == "Погорелов":
        return "pogorelov"
async def refactor_authors_7Geometry(author):
    if author == "Атанасян":
        return "atanasjan"
    elif author == "Мерзляк":
        return "merzlyak"
    elif author == "Мерзляк раб. тетрадь":
        return "merzlyakWorkNote"
    elif author == "Погорелов":
        return "pogorelov"



async def refactor_authors_11Phith(author):
    if author == "Задачник Рымкевич":
        return "rymkevich"
    elif author == "Степанов Сборник задач":
        return "stepanova"
    elif author == "Парфентьева Сборник задач":
        return "parfenova"
    elif author == "Громов":
        return "gromov"


async def refactor_authors_10Phith(author):
    if author == "Рымкевич":
        return "rymkevich"
    elif author == "Мякишев":
        return "_mjakishev"
    #elif author == "Парфентьева Сборник задач":
      #  return "parfenova"
    #elif author == "Громов":
     #   return "gromov"

async def refactor_authors_9Phith(author):
    if author == "Перышкин упражнения":
        return "perishkin"
    elif author == "Генденштейн задчаник":
        return "gendenshtein-zadachnik"
    elif author == "Лукаши":
        return "lukashi"

async def refactor_authors_8Phith(author):
    if author == "Перышкин упражнения":
        return "perishkin"
    elif author == "Генденштейн задчаник":
        return "gendenshtein-zadachnik"
    elif author == "Лукаши":
        return "lukashi"

async def refactor_authors_7Phith(author):
    if author == "Перышкин упражнения":
        return "perishkin"
    elif author == "Лукаши":
        return "lukashi"






async def refactor_authors_11Russian(author):
    if author == "Гольцова Базовый уровень":
        return "golcova"
    elif author == "Власенков":
        return "vlasenkov"
    elif author == "Греков":
        return "grekov"
    elif author == "Громов":
        return "gromov"

async def refactor_authors_10Russian(author):
    if author == "Рымкевич":
        return "rymkevich"
    elif author == "Мякишев":
        return "_mjakishev"
    #elif author == "Парфентьева Сборник задач":
      #  return "parfenova"
    #elif author == "Громов":
     #   return "gromov"


async def refactor_authors_9Russian(author):
    if author == "Ладыженская":
        return "trosteva"
    elif author == "Разумовская":
        return "razumovskaya"
    elif author == "Бархударов":
        return "bahdurov"
    elif author == "Рыбченкова":
        return "ribacheva"

async def refactor_authors_8Russian(author):
    if author == "Ладыженская":
        return "trosteva"
    elif author == "Разумовская":
        return "razumovskaya"
    elif author == "Бархударов":
        return "bahdurov"
    elif author == "Рыбченкова":
        return "ribacheva"

async def refactor_authors_7Russian(author):
    if author == "Ладыженская":
        return "ladishzkaya"
    elif author == "Разумовская":
        return "razumovskaya"
    elif author == "Ефремова":
        return "efremova"
    elif author == "Рыбченкова":
        return "ribacheva"

async def refactor_authors_6Russian(author):
    if author == "Ладыженская":
        return "ladishzkaya"
    elif author == "Разумовская":
        return "razumovskaya"
    elif author == "Шмелев":
        return "shmelev"
    elif author == "Рыбченкова":
        return "ribacheva"
    elif author == "Львова":
        return "livova"

async def refactor_authors_5Russian(author):
    if author == "Ладыженская":
        return "ladishzkaya"
    elif author == "Разумовская":
        return "razumovskaya"
    elif author == "Шмелев":
        return "shmelev"
    elif author == "Рыбченкова":
        return "ribacheva"
    elif author == "Львова":
        return "livova"
    elif author == "Ефремова":
        return "efremova"

async def refactor_authors_11English(author):
    if author == "Enjoy":
        return "enjoy"
    elif author == "Enjoy Раб тетрадь":
        return "enjoywn"
    elif author == "Кузовлев":
        return "kuzolev"
    elif author == "Кузовлев Раб тетрадь":
        return "kuzolevwn"
    elif author == "Афанасьева":
        return "afanaseva"
    elif author == "Афанасьева Раб тетрадь":
        return "afanasevawn"
    elif author == "Spotlight":
        return "spotlight"
    elif author == "Spotlight Раб тетрадь":
        return "spotlightwn"