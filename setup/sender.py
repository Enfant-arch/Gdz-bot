import models.Gdz as solve 
import datetime

class Sender():
    async def send_solution(links, subject, class_, author, taskN, message, Shelper, keyBoard, logging):
        if len(links) == 0:
            await Shelper.send_message(chat_id=message.from_user.id, text="Такого номера нет", reply_markup=keyBoard.AE_replyKeyBoard)
        for i in links:
            with open(f"models\\file\\{subject}\\{class_}\\{author}\\{taskN}\\{i}", 'rb') as photo:
                await Shelper.send_photo(
                    chat_id= message.from_user.id,
                    photo=photo,
                    reply_markup=keyBoard.AE_replyKeyBoard,
                    disable_notification = True
                    )
        logging.info("Photos: %r", links)
    async def send_PRGHsolution(links, subject, class_, author, prgh, taskN, message, Shelper, keyBoard,logging ):
            
            if len(links) == 0:
                await Shelper.send_message(chat_id=message.from_user.id, text="Такого номера нет", reply_markup=keyBoard.AE_replyKeyBoard)
            
            for i in links:
                with open(f"models\\file\\{subject}\\{class_}\\{author}\\{prgh}\\{taskN}\\{i}", 'rb') as photo:
                    await Shelper.send_photo(
                        chat_id= message.from_user.id,
                        photo=photo,
                        reply_markup=keyBoard.AE_replyKeyBoard,
                        disable_notification = True
                        )
            logging.info("Photos: %r", links)
            return True

    async def send(message, Shelper, models, gdz_plot, keyBoard, state, logging):
        
        if message.text == "Другое решение":
            await message.answer("Выберете предмет", reply_markup=keyBoard.Subjects_reply_Keyboard)
            await gdz_plot.subject.set()

        elif message.text == "🔙Главное меню":
            await message.answer("Вы перешли в главное меню", reply_markup=keyBoard.start_reply_Keyboard)
            await state.finish()
            
        else:
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
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra11.connect_for_Mordkovich(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "mordkovich_2009":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra11.connect_for_MordkovichBase(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "alimov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra11.connect_for_Alimov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "kolmogorov_2010":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra11.connect_for_Kilmogorov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    #[REGION ALGEBRA10]
                    elif data["subject"] == "Алгебра➕" and data["class_" ] == "10 класс":
                        author = await models.refactorDates.refactor_authors_10Algebra(data["author"])
                        if author == "mordkovich_semenov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra10.connect_for_Mordkovich(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "mordkovich_2009":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra10.connect_for_MordkovichBase(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "alimov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra10.connect_for_Alimov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "kolmogorov_2010":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra10.connect_for_Kilmogorov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    #[REGION ALGEBRA9]
                    elif data["subject"] == "Алгебра➕" and data["class_" ] == "9 класс":
                        author = await models.refactorDates.refactor_authors_9Algebra(data["author"])
                        if author == "makarychev":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra9.connect_for_Makrichev(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "makarichev-uglublennoe-izuchenie":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra9.connect_for_Makrichev_uglubleniy(subject=subject, class_=class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "morodkovich":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra9.connect_for_Mordkovich(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "mordkovich-uglublennoe-izuchenie":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra9.connect_for_mordkovichuglublennoe(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "merzlyak":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra9.connect_for_Merzlyak(subject=subject, class_=class_, author=author, taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "merzlyak-polyakov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra9.connect_for_Merzlyakublennoe(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    #[REGION ALGEBRA8]
                    elif data["subject"] == "Алгебра➕" and data["class_" ] == "8 класс":
                        author = await models.refactorDates.refactor_authors_8Algebra(data["author"])
                        if author == "makarychev_2012":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra8.connect_for_Makrichev(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging)
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "macarichev-uglublennij-uroven":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra8.connect_for_Makrichev_uglubleniy(subject=subject, class_=class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging)
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "morodkovich":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra8.connect_for_Mordkovich(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging)
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "mordkovich-uglublennyj-zadachnik":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra8.connect_for_mordkovichuglublennoe(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging)
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "merzlyak":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra8.connect_for_Merzlyak(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging)
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "merzlyak-polyakov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra8.connect_for_Merzlyakublennoe(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging)
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "alimov_2012":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra8.connect_for_Alimov(subject=subject, class_=class_, author=author, taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    #[REGION ALGEBRA7]
                    elif data["subject"] == "Алгебра➕" and data["class_" ] == "7 класс":
                        author = await models.refactorDates.refactor_authors_7Algebra(data["author"])
                        if author == "makarychev_2012":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra7.connect_for_Makrichev(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "dorofeev":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra7.connect_for_dorofeev(subject=subject, class_=class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "mordkovich":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra7.connect_for_Mordkovich(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "kolyagin-tkacheva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra7.connect_for_kolyagin(subject=subject, class_=class_, author=author,  taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "merzlyak-polonskij-yakir":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra7.connect_for_Merzlyak(subject=subject, class_=class_, author=author, taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging)
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "nikolskij":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Algebra7.connect_for_nikolskij(subject=subject, class_=class_, author=author, taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    #[REGION GEOMETRIYA11]
                    elif data["subject"] == "Геометрия📐" and data["class_" ] == "11 класс":
                        author = await models.refactorDates.refactor_authors_11Geometry(data["author"])
                        if author == "atanasjan":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry11.connect_to_atasyan(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper= Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "pogorelov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry11.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    
                    #[REGION GEOMETRIYA10]
                    elif data["subject"] == "Геометрия📐" and data["class_" ] == "10 класс":
                        author = await models.refactorDates.refactor_authors_10Geometry(data["author"])
                        if author == "atanasjan":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry10.connect_to_atasyan(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "pogorelov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry10.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging)
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    #[REGION GEOMETRIYA9]
                    elif data["subject"] == "Геометрия📐" and data["class_" ] == "9 класс":
                        author = await models.refactorDates.refactor_authors_9Geometry(data["author"])
                        if author == "atanasjan":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry9.connect_to_atasyan(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_,prgh=prgh, author=author,taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "merzljak-polonskij":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry9.connect_to_polonskij(subject=subject, class_=class_, author=author,  taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging)
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "atanasyan":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry9.connect_to_atasyan_workNote(subject=subject, class_=class_, author=author,  taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "pogorelov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry9.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                            
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    elif data["subject"] == "Геометрия📐" and data["class_" ] == "8 класс":
                        author = await models.refactorDates.refactor_authors_8Geometry(data["author"])
                        if author == "atanasjan":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry8.connect_to_atasyan(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "merzlyak":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry8.connect_to_Mezlyak(subject=subject, class_=class_, author=author, taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "atanasyanWN":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry8.connect_to_atasyan_workNotek(subject=subject, class_=class_, author=author,  taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "pogorelov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry8.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    elif data["subject"] == "Геометрия📐" and data["class_" ] == "7 класс":
                        author = await models.refactorDates.refactor_authors_7Geometry(data["author"])
                        if author == "atanasjan":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry7.connect_to_merzlyakWorkNote(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "merzlyak":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry7.connect_to_merzlyak(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "merzlyakWorkNote":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry7.connect_to_merzlyakWorkNote(subject=subject, class_=class_, author=author, taskN=taskN) 
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,  taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "pogorelov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Geometry7.connect_to_pogorelov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    elif data["subject"] == "Физика📊" and data["class_"] == "11 класс":
                        author = await models.refactorDates.refactor_authors_11Phith(data["author"])
                        if author == "rymkevich":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith11.connect_to_rymkevich(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "stepanova":
                            #links = await solve.Phith11.connect_to_stepanova(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            #await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await message.answer(text="Учебник на обновлении")
                        elif author == "parfenova":
                        #links = await solve.Phith11.connect_to_gromov(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            #await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await message.answer(text="Учебник на обновлении")
                        elif author == "gromov":
                            #links = await solve.Phith11.connect_to_parfenova(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            #await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await message.answer(text="Учебник на обновлении")
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    elif data["subject"] == "Физика📊" and data["class_"] == "10 класс":
                        author = await models.refactorDates.refactor_authors_10Phith(data["author"])
                        if author == "rymkevich":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith10.connect_to_rymkevich(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "_mjakishev":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith10.connect_to_mjakishev(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "parfenova":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith10.connect_to_mjakishev(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "gromov":
                            #links = await solve.Phith11.connect_to_parfenova(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            #await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await message.answer(text="Учебник на обновлении")
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")                
            
                    elif data["subject"] == "Физика📊" and data["class_"] == "9 класс":
                        author = await models.refactorDates.refactor_authors_9Phith(data["author"])
                        if author == "perishkin":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith9.connect_to_perishkin(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "gendenshtein-zadachnik":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith9.connect_to_gendenshtein_zadachnik(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                            
                        elif author == "lukashi":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith9.connect_to_luskshin(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")                
                    elif data["subject"] == "Физика📊" and data["class_"] == "8 класс":
                        author = await models.refactorDates.refactor_authors_8Phith(data["author"])
                        if author == "perishkin":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith8.connect_to_perishkin(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "gendenshtein-zadachnik":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith8.connect_to_gendenshtein_zadachnik(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                            
                        elif author == "lukashi":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith8.connect_to_luskshin(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")

                    elif data["subject"] == "Физика📊" and data["class_"] == "7 класс":
                        author = await models.refactorDates.refactor_authors_7Phith(data["author"])
                        if author == "perishkin":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith7.connect_to_perishkin(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
    
                        elif author == "lukashi":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Phith8.connect_to_luskshin(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")

                    elif data["subject"] == "Русский язык🖊" and data["class_"] == "11 класс":
                        author = await models.refactorDates.refactor_authors_11Russian(data["author"])
                        if author == "golcova":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik11.connect_to_Golcova(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "vlasenkov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik11.connect_to_vlasenkov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "grekov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik11.connect_to_Grekov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "gromov":
                            #links = await solve.Phith11.connect_to_parfenova(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            #await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await message.answer(text="Учебник на обновлении")
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    elif data["subject"] == "Русский язык🖊" and data["class_"] == "10 класс":
                        author = await models.refactorDates.refactor_authors_11Russian(data["author"])
                        if author == "golcova":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik11.connect_to_Golcova(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "vlasenkov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik11.connect_to_vlasenkov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "grekov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik11.connect_to_Grekov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "gromov":
                            #links = await solve.Phith11.connect_to_parfenova(subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN) 
                            #await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message, Shelper=Shelper,keyBoard=keyBoard,logging=logging )
                            await message.answer(text="Учебник на обновлении")
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    elif data["subject"] == "Русский язык🖊" and data["class_"] == "9 класс":
                        author = await models.refactorDates.refactor_authors_9Russian(data["author"])
                        if author == "trosteva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik9.connect_to_trosteva(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "razumovskaya":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik9.connect_to_razumovskaya(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "bahdurov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik9.connect_to_bahdurov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "ribacheva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik9.connect_to_ribacheva(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")

                    elif data["subject"] == "Русский язык🖊" and data["class_"] == "8 класс":
                        author = await models.refactorDates.refactor_authors_8Russian(data["author"])
                        if author == "trosteva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik8.connect_to_trosteva(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "razumovskaya":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik8.connect_to_razumovskaya(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "bahdurov":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik8.connect_to_bahdurov(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "ribacheva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik8.connect_to_ribacheva(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    elif data["subject"] == "Русский язык🖊" and data["class_"] == "7 класс":
                        author = await models.refactorDates.refactor_authors_7Russian(data["author"])
                        if author == "ladishzkaya":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik7.connect_to_ladishzkaya(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "razumovskaya":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik7.connect_to_razumovskaya(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "efremova":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik7.connect_to_efremova(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "ribacheva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik7.connect_to_ribacheva(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")

                    elif data["subject"] == "Русский язык🖊" and data["class_"] == "6 класс":
                        author = await models.refactorDates.refactor_authors_6Russian(data["author"])
                        if author == "ladishzkaya":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik6.connect_to_ladishzkaya(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "razumovskaya":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik6.connect_to_razumovskaya(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "shmelev":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik6.connect_to_shmelev(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "ribacheva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik6.connect_to_ribacheva(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "livova":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik6.connect_to_livova(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")

                    elif data["subject"] == "Русский язык🖊" and data["class_"] == "5 класс":
                        author = await models.refactorDates.refactor_authors_5Russian(data["author"])
                        if author == "ladishzkaya":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik5.connect_to_ladishzkaya(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "razumovskaya":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik5.connect_to_razumovskaya(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "shmelev":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik5.connect_to_shmelev(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author, prgh=prgh, taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "ribacheva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik5.connect_to_ribacheva(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "livova":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik5.connect_to_livova(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "efremova":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.Russki_Yazik5.connect_to_efremova(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")

                    elif data["subject"] == "Английский 🇺🇸" and data["class_"] == "11 класс":
                        author = await models.refactorDates.refactor_authors_11English(data["author"])
                        if author == "enjoy":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English11.connect_to_enjoy(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author,prgh=prgh,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "kuzolevwn":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English11.connect_to_kuzolevwn(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, prgh=prgh, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "afanaseva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English11.connect_to_afanaseva(subject=subject, class_ = class_, author=author,prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author,taskN=taskN,prgh=prgh, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "afanasevawn":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English11.connect_to_afanasevawn(subject=subject, class_ = class_, author=author,prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, prgh=prgh, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "spotlight":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English11.connect_to_spotlight(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "spotlightwn":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English11.connect_to_spotlightwn(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    

                    elif data["subject"] == "Английский 🇺🇸" and data["class_"] == "10 класс":
                        author = await models.refactorDates.refactor_authors_10English(data["author"])
                        if author == "enjoy":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English10.connect_to_enjoy(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author,prgh=prgh,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "kuzolevwn":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English10.connect_to_kuzolevwn(subject=subject, class_ = class_, author=author, prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, prgh=prgh, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "afanaseva":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English10.connect_to_afanaseva(subject=subject, class_ = class_, author=author,prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author,taskN=taskN,prgh=prgh, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "afanasevawn":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English10.connect_to_afanasevawn(subject=subject, class_ = class_, author=author,prgh=prgh, taskN=taskN)
                            await Sender.send_PRGHsolution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, prgh=prgh, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "spotlight":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English10.connect_to_spotlight(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        elif author == "spotlightwn":
                            msg =  await Shelper.send_message(chat_id=message.from_user.id, text="Отправляем решение......")
                            links = await solve.English10.connect_to_spotlightwn(subject=subject, class_ = class_, author=author, taskN=taskN)
                            await Sender.send_solution(links=links, subject=subject, class_=class_, author=author,taskN=taskN, message=message,Shelper=Shelper,keyBoard=keyBoard, logging=logging )
                            await Shelper.delete_message(chat_id=message.from_user.id,message_id=msg.message_id)
                        
                        else:
                            await message.answer("Возникла не предвиденная ошибка, отпишите для устроненеия в баг репорт.")
                    







