# from telebot import TeleBot
#
# # from constants import token
#
# # from sinoptic import Weather
# # from datetime import datetime
#
# '''with open("tet.json", "w") as f:
#     json.dump(start.get_updates(), f, indent=2, ensure_ascii=False)'''
#
# __bot = TeleBot(token)
#
#
# #weather = Weather()
#
#
# def __log(message, txt):
#     from datetime import datetime
#     print(datetime.now())
#     text = ("Час: {4} \nПовідомлення від {0} {1}; (id = {2}) \nТекст - {3}\n\n".
#             format(message.from_user.first_name, message.from_user.last_name,
#                    str(message.from_user.id), txt, datetime.now()))
#
#     print(text)
#
#     f = open("messages.txt", "a")
#     f.writelines(text)
#     f.close()
#
#
# @__bot.message_handler(content_types=["text"])
# def __handle_message(message):
#     __log(message, message.text)
#     try:
#         def __mess():
#             '''try:
#                 weather.update()
#
#                 __bot.send_message(message.chat.id, weather.get_title())
#                 __bot.send_message(message.chat.id,
#                                    weather.get_weather() + ".\n" +
#                                    "мін: {0}\xB0С \nмакс: {1}\xB0С"
#                                    .format(weather.get_min_temp(),
#                                            weather.get_max_temp()))
#                 __bot.send_message(message.chat.id, "Інформація: \n" + weather.get_info())
#             except Exception as err:
#                 weather.set_local('львів')
#                 print(err)'''
#
#         if message.text.lower() == 'погода':
#             __mess()
#
#         elif (message.text.split()[0].lower() in ('місто', 'село')) and (len(message.text.split()) > 1):
#             #weather.set_local(message.text.split(' ')[1].lower())
#             __mess()
#
#         elif (message.text.split()[0].lower() in 'дата') and (len(message.text.split()) > 1):
#             #weather.set_date(message.text.split(' ')[1])
#             __mess()
#
#         elif message.text.lower() == 'сьогодні':
#             #weather.set_date(str(datetime.today().date()))
#             __mess()
#
#     except Exception as a:
#         print(a)
#
#
# __bot.polling(none_stop=True, interval=2)
