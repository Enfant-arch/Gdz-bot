import os
import logging
import requests
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
        url = f"https://megaresheba.ru/publ/reshebnik/{class_}_klass_{author}/34-1-0-2097/{prgh}-{taskN}-paragraph"
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
        url = f"https://megaresheba.ru/gdz/algebra/8-klass/mordkovich-uglublennyj-zadachnik/{prgh}-nomer-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Merzlyak(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/gdz/{subject}/{class_}_klass/{author}/{prgh}-1-{taskN}-nomer"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Merzlyakublennoe(subject, class_, author, prgh, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{prgh}-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_for_Alimov(subject, class_, author, taskN):
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
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_for_Merzlyak(subject, class_, author,  taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/gdz/{subject}/{class_}-klass/{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_for_nikolskij(subject, class_, author, taskN):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        url = f"https://megaresheba.ru/publ/reshebnik/{subject}/{author}/34-1-0-2298/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
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
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks

class Phith11():
    async def connect_to_rymkevich(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz-sbornik-zadach-po-fizike-10-{class_}-klass-{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_stepanova(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/geometrija/{class_}_klass/merzljak/{prgh}-paragraph-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_to_parfenova(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/gdz/geometrija/7_klass/merzlyak/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_gromov(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/geometrija/pogorelov_{class_}_8_9_klass/32-1-0-1198/{prgh}-nomer-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

class Phith10():
    async def connect_to_rymkevich(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz-sbornik-zadach-po-fizike-{class_}-11-klass-{author}/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_mjakishev(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/fizika/domashnjaja_rabote_po_fizike_za_10_klass_k_uchebniku_fizika_10_klass_g_ja_mjakishev_b_b_bukhovcev_2011/31-1-0-2190/{prgh}-nomer-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks
    
class Phith9():
    async def connect_to_perishkin(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/index/06/0-371/{prgh}-{taskN}-nomer'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_luskshin(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/index/06/0-343/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_gendenshtein_zadachnik(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/fizika/9-klass/gendenshtein-zadachnik/{prgh}-section-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks

class Phith8():
    async def connect_to_perishkin(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/index/05/0-358/{prgh}-{taskN}-nomer'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_luskshin(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/index/06/0-343/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_gendenshtein_zadachnik(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/fizika/reshebnik_k_zadachniku_po_fizike_8_klass_l_eh_gendenshtejna/31-1-0-2195/{prgh}-tema-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks


class Phith7():
    async def connect_to_perishkin(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/index/07/0-344/{prgh}-{taskN}-nomer'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_luskshin(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/index/06/0-343/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_gendenshtein_zadachnik(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/fizika/reshebnik_k_zadachniku_po_fizike_8_klass_l_eh_gendenshtejna/31-1-0-2195/{prgh}-tema-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
        return listLinks

class Russki_Yazik11():
    async def connect_to_Golcova(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/russkomu_jazyku/10_11_klass_golcova/35-1-0-1212/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_vlasenkov(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz/russkij-yazyk/10-klass/vlasenkov-rybchenkova/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_Grekov(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/gdz/russkij-yazyk/10-klass/grekov/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    #async def connect_to_Grekov(subject, class_, author, prgh, taskN):
    #    url = f'https://megaresheba.ru/publ/reshebnik/fizika/reshebnik_k_zadachniku_po_fizike_8_klass_l_eh_gendenshtejna/31-1-0-2195/{prgh}-tema-{taskN}'
    #    listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author,prgh=prgh, taskN=taskN, url=url)
    #    return listLinks    

class Russki_Yazik10():
    async def connect_to_Golcova(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/russkomu_jazyku/10_11_klass_golcova/35-1-0-1212/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_vlasenkov(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz/russkij-yazyk/10-klass/vlasenkov-rybchenkova/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_Grekov(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/gdz/russkij-yazyk/10-klass/grekov/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

class Russki_Yazik9():
    async def connect_to_trosteva(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/russkomu_jazyku/9_klass_ladyzhenskaja_2010/35-1-0-1588/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_razumovskaya(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz/russkij-yazyk/9-klass/razumovskaja/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_bahdurov(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/gdz/russkij-yazyk/9-klass/barhudarov/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_ribacheva(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/gdz/russkij-yazyk/9-klass/ribchenkova/1-{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

class Russki_Yazik8():
    async def connect_to_trosteva(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/russkomu_jazyku/8_klass_trostencova/35-1-0-1218/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_razumovskaya(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/russkomu_jazyku/razumovskaja_8_klass/35-1-0-1217/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_bahdurov(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/russkomu_jazyku/barkhudarov_8_klass/35-1-0-1220/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_ribacheva(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/gdz/russkij_jazyk/8-klass/ribchenkova/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

class Russki_Yazik7():
    async def connect_to_ladishzkaya(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/index/05/0-308/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_razumovskaya(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz/russkij-yazyk/7-klass/razumovskaya-7/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_efremova(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/russkomu_jazyku/reshebnik_gdz_k_rabochej_tetradi_po_russkomu_jazyku_7_klass_ladyzhenskaja_baranov_2013/35-1-0-2202/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_ribacheva(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/gdz/russkij_jazyk/5-klass/rybchenkova/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

class Russki_Yazik6():
    async def connect_to_ladishzkaya(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/index/04/0-4310/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_razumovskaya(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz/russkij-yazyk/6-klass/razumovskaya-6/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_shmelev(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/russkij_jazyk/6-klass/shmelev/{prgh}-section-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_to_ribacheva(subject, class_, author, taskN):
        if int(taskN) < 383:
            url = f'https://megaresheba.ru/gdz/russkij-yazyk/6-klass/rybchenkova/1-chast-{taskN}-2021'
            listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
            return listLinks
        else:
            url = f'https://megaresheba.ru/gdz/russkij-yazyk/6-klass/rybchenkova/2-chast-{taskN}-2021'
            listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
            return listLinks
    async def connect_to_livova(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/russkomu_jazyku/6_klass_lvov_lvova/35-1-0-2129/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

class Russki_Yazik5():
    async def connect_to_ladishzkaya(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/index/02/0-4303/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_razumovskaya(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/gdz/russkij-yazyk/5-klass/razumovskaya-5/{taskN}-nomer"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_shmelev(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/russkij-yazyk/5-klass/shmelev/{prgh}-nomer-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks
    async def connect_to_ribacheva(subject, class_, author, taskN):
        if int(taskN) > 383:
            url = f'https://megaresheba.ru/gdz/russkij-yazyk/5-klass/ribchenkova/1-2020-chast-{taskN}'
            listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
            return listLinks
        else:
            url = f'https://megaresheba.ru/gdz/russkij-yazyk/5-klass/ribchenkova/2-2020-chast-{taskN}'
            listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
            return listLinks
    async def connect_to_livova(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/russkomu_jazyku/6_klass_lvov_lvova/35-1-0-2129/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
    async def connect_to_efremova(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/gdz/russkij-yazyk/5-klass/rabochaya-tetrad-efremova/{taskN}-nomer'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks
        
class English11():
    async def connect_to_enjoy(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/anglijskij-yazyk/11-klass/enjoy-english-biboletova-snezhko/{prgh}-unit-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_enjoywn(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/gdz/russkij-yazyk/10-klass/vlasenkov-rybchenkova/{taskN}-nomer"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_kuzolevwn(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/anglijskij-yazyk/11-klass/kuzovlev-activity-book/{prgh}-unit-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_afanaseva(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/gdz/anglijskij-yazyk/11-klass/afanaseva/{prgh}-unit-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_afanasevawn(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/anglijskij-yazyk/11-klass/activity-book-afanasjeva/{prgh}-unit-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_spotlight(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/anglijskij/11_klass_spotlight_evans/{taskN}-str"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_spotlightwn(subject, class_, author, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/anglijskij/11_klass_spotlight_afanaseva_workbook/{taskN}-str'
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

class English10():
    async def connect_to_enjoy(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/publ/reshebnik/anglijskij/10_klass_biboletova/42-1-0-2106/{prgh}-unit-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_enjoywn(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/gdz/russkij-yazyk/10-klass/vlasenkov-rybchenkova/{taskN}-nomer"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_kuzolevwn(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/anglijskij-yazyk/11-klass/kuzovlev-activity-book/{prgh}-unit-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_afanaseva(subject, class_, author, prgh, taskN):
        url = f"https://megaresheba.ru/gdz/anglijskij-yazyk/10-klass/afanaseva/{prgh}-unit-{taskN}"
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_afanasevawn(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/anglijskij-yazyk/10-klass/tetrad-afanaseva/{taskN}-str'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks

    async def connect_to_spotlight(subject, class_, author, taskN):
        url = f"https://megaresheba.ru/publ/reshebnik/anglijskij/10_klass_spotlight_evans/{taskN}-str"
        listLinks = await connecting_and_save_NONEprgh(subject=subject, class_=class_, author=author, taskN=taskN, url=url)
        return listLinks

    async def connect_to_spotlightwn(subject, class_, author, prgh, taskN):
        url = f'https://megaresheba.ru/gdz/anglijskij/10-klass/workbook-spotlight-evans/{prgh}-module-{taskN}'
        listLinks = await connecting_and_save_withprgh(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, url=url)
        return listLinks



###TODO Eng, Chemisty, History, Biology

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
