import asyncio
from dataclasses import replace
import os
import logging
from sqlite3 import connect
from tracemalloc import take_snapshot
import requests

import urllib
from bs4 import BeautifulSoup



class Algebra11():
    async def connect_for_MordkovichBase(subject, class_, author,prgh, taskN):
        
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/zadachnik_10_{class_}_klass_{author}/34-1-0-1103/{prgh}-nomer-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Alimov(subject, class_, author, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/10_{class_}_klass_{author}/34-1-0-1964/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Mordkovich(subject, class_, author,prgh, taskN):
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{prgh}-paragraph-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Kilmogorov(subject, class_, author, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/10_{class_}_klass_{author}/34-1-0-1963/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    
        
    

class Algebra10():

    async def connect_for_Mordkovich(subject, class_, author,prgh, taskN):
       
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/reshebnik_po_algebre_{class_}_klass_{author}/{prgh}-paragraph-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
        
    async def connect_for_MordkovichBase(subject, class_, author,prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/zadachnik_{class_}_11_klass_{author}/34-1-0-1103/{prgh}-nomer-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
              
    async def connect_for_Alimov(subject, class_, author, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/{class_}_11_klass_{author}/34-1-0-1964/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
        
    async def connect_for_Kilmogorov(subject, class_, author, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/{class_}_11_klass_{author}/34-1-0-1963/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks



class Algebra9():
    async def connect_for_Makrichev(subject, class_, author,taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/9_klass_{author}/34-1-0-2034/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Makrichev_uglubleniy(subject, class_, author,taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/9-klass/{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Makrichev_uglubleniy(subject, class_, author,taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/9-klass/{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_for_Mordkovich(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/{class_}_klass_{author}/34-1-0-2097/{prgh}-{taskN}-paragraph"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_for_mordkovichuglublennoe(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{taskN}/{class_}_klass_{author}/34-1-0-2097/{prgh}-{taskN}-paragraph"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_for_Merzlyak(subject, class_, author, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{taskN}"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Merzlyakublennoe(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{prgh}-{taskN}"
        logging.info('URl :  %r', url)
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks



class Algebra8():

    async def connect_for_Makrichev(subject, class_, author,taskN):
        url = f"https://megaresheba.ru/index/reshebnik_po_algebre_{class_}_klass_{author}/0-4637/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Makrichev_uglubleniy(subject, class_, author,taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/gdz/{subject}/{class_}_klass/{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks


    async def connect_for_Mordkovich(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/index/06/0-181/{prgh}-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_for_mordkovichuglublennoe(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/gdz/{subject}/{class_}_klass/{author}/{prgh}-nomer-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Merzlyak(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
       
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}_klass/{author}/{prgh}-1-{taskN}-nomer"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Merzlyakublennoe(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{prgh}-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_for_Merzlyakublennoe(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{prgh}-{taskN}"
        logging.info('URl :  %r', url)
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Alimov(subject, class_, author, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/index/reshebnik_po_algebre_{class_}_klass_{author}/0-4636/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_for_Muravin(subject, class_, author, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/index/reshebnik_po_algebre_{class_}_klass_{author}/0-4636/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

class Algebra7():
    async def connect_for_Makrichev(subject, class_, author,taskN):
        url = f"https://megaresheba.ru/index/08/0-173/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_for_dorofeev(subject, class_, author,taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks


    async def connect_for_Mordkovich(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/{class_}_klass_{author}/34-1-0-1100/{prgh}-{taskN}-paragraph"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_for_kolyagin(subject, class_, author, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Merzlyak(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_for_nikolskij(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/{author}/34-1-0-2298/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

class Geometry11():
    async def connect_to_atasyan(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/10_{class_}_klass_{author}/32-1-0-1117/class-{class_}-{taskN}"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_pogorelov(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/{class_}_klass_{author}/32-1-0-1118/{prgh}-paragraph-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
class Geometry10():
    async def connect_to_atasyan(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/{class_}_11_klass_{author}/32-1-0-1117/class-{class_}-{taskN}"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_pogorelov(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/{class_}_klass_{author}/32-1-0-1118/{prgh}-paragraph-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

class Geometry9():
    async def connect_to_atasyan(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/7_8_9_klass_{author}/32-1-0-1200/{prgh}-section-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_to_polonskij(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz/geometriya/{class_}-klass/{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_atasyan_workNote(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz-rabochaya-tetrad-geometriya-{class_}-klass-{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    
    async def connect_to_pogorelov(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/pogorelov_7_8_{class_}_klass/32-1-0-1198/{prgh}-nomer-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
class Geometry8():
    async def connect_to_atasyan(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/7_8_9_klass_{author}/32-1-0-1200/{prgh}-section-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_to_atasyan_workNote(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/rabochaya-tetrad-geometriya-{class_}-klass-atanasyan/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
        
    async def connect_to_Mezlyak(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz/geometriya/{class_}-klass/{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_pogorelov(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/pogorelov_7_{class_}_9_klass/32-1-0-1198/{prgh}-nomer-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
        
class Geometry7():
    async def connect_to_atasyan(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/7_8_9_klass_{author}/32-1-0-1200/{prgh}-section-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_merzlyak(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/geometrija/{class_}_klass/merzljak/{prgh}-paragraph-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_to_merzlyakWorkNote(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/gdz/geometrija/7_klass/merzlyak/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_pogorelov(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/pogorelov_{class_}_8_9_klass/32-1-0-1198/{prgh}-nomer-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
class Russki_Yazik11():
    pass
class Russki_Yazik10():
    pass
class Russki_Yazik9():
    pass
class Russki_Yazik8():
    pass
class Russki_Yazik7():
    pass
class Russki_Yazik6():
    pass


async def connecting_and_save_withprgh(subject, class_, author, taskN, prgh, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        logging.info('URl :  %r', url)
        responce = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(responce.text, 'lxml')
        cou = soup.find_all("div", class_='with-overtask')
        imgLinks = []
        for i in cou:
            img = i.find("img")["src"]
            logging.info('Was detected: %r', img)
            imgLinks.append(img)
            logging.info('List contain is  :  %r', imgLinks)             
        src = f'models\\file\\{subject}\\{class_}\\{author}\\{prgh}\\{taskN}'
        try:
            os.makedirs(f'{src}')
        except Exception as err:
            logging.info('Error :  %r \t File already created', err)

        for j in imgLinks:
            try:
                with open(f"{src}\\{j[-7:]}.jpg", 'wb') as handle:
                    response = requests.get(j, stream=True)
                    print(responce)

                    if not response.ok:
                        print(response)

                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)

            except FileExistsError as err:
                logging.info('error :  %r \nSending ready file', err)
        names = os.listdir(f'models\\file\\{subject}\\{class_}\\{author}\\{prgh}\\{taskN}')
        return names

async def connecting_and_save_NONEprgh(subject, class_, author, taskN, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        logging.info('URl :  %r', url)
        responce = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(responce.text, 'lxml')
        cou = soup.find_all("div", class_='with-overtask')
        imgLinks = []
        for i in cou:
            img = i.find("img")["src"]
            logging.info('Was detected: %r', img)
            imgLinks.append(img) 
            logging.info('List contain is  :  %r', imgLinks)         
        src = f'models\\file\\{subject}\\{class_}\\{author}\\{taskN}'
        try:
            os.makedirs(f'{src}')
        except Exception as err:
            logging.info('Error :  %r \t File already created', err)

        for j in imgLinks:
            try:
                with open(f"{src}\\{j[-7:]}.jpg", 'wb') as handle:
                    response = requests.get(j, stream=True)
                    print(responce)

                    if not response.ok:
                        print(response)

                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handle.write(block)

            except FileExistsError as err:
                logging.info('error :  %r \nSending ready file', err)
        names = os.listdir(f'models\\file\\{subject}\\{class_}\\{author}\\{taskN}')
        return names 
