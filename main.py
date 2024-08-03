import telebot
from telebot import types

bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("Работа в интернете", callback_data='internet')
    button2 = types.InlineKeyboardButton("Большие вычислительные мощности", callback_data='calculations')
    button3 = types.InlineKeyboardButton("Игры", callback_data='games')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Йоу! Ты скоро станешь обладателем крутого компа! Расскажи для чего ты хочешь "
                                      "его использовать?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'internet' or call.data == 'calculations' or call.data == 'games':
        markup = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton("До 50 000 ₽", callback_data='price_1')
        button2 = types.InlineKeyboardButton("До 100 000 ₽", callback_data='price_2')
        button3 = types.InlineKeyboardButton("До 200 000 ₽", callback_data='price_3')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back')
        markup.add(button1, button2, button3, button_back)
        bot.send_message(call.message.chat.id, "Выберите вариант стоимости:", reply_markup=markup)

    elif call.data == 'back':
        start(call.message)

    elif call.data == 'price_1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        button_model1 = types.InlineKeyboardButton("i5-10400F x GT 1030 - 35 500 ₽", callback_data='model_1')
        button_model2 = types.InlineKeyboardButton("i3-12100F х RX 550 - 44 000 ₽", callback_data='model_2')
        button_model3 = types.InlineKeyboardButton("Ryzen 5 5600G х RX 6400 - 46 100 ₽", callback_data='model_3')
        button_model4 = types.InlineKeyboardButton("i3-10105F х GTX 1650 - 47 500 ₽", callback_data='model_4')
        button_model5 = types.InlineKeyboardButton("i5-10400F х GTX 1650 - 49 500 ₽", callback_data='model_5')
        button_back1 = types.InlineKeyboardButton("Назад", callback_data='back1')
        markup.add(button_model1, button_model2, button_model3, button_model4, button_model5, button_back1)
        bot.send_message(call.message.chat.id, "Выберите модель компьютера:", reply_markup=markup)

    elif call.data == "back1":
        markup = types.InlineKeyboardMarkup(row_width=1)
        price1 = types.InlineKeyboardButton('До 50 000 ₽', callback_data='price_1')
        price2 = types.InlineKeyboardButton('До 100 000 ₽', callback_data='price_2')
        price3 = types.InlineKeyboardButton('До 200 000 ₽', callback_data='price_3')
        back = types.InlineKeyboardButton('Назад', callback_data='back')
        markup.add(price1, price2, price3, back)
        bot.send_message(chat_id=call.message.chat.id, text='Выбери цену',
                              reply_markup=markup)
    elif call.data == 'model_1':
        markup = types.InlineKeyboardMarkup(row_width=1)
        order1 = types.InlineKeyboardButton('Заказать', callback_data='order1')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back2 = types.InlineKeyboardButton('Назад', callback_data='back2')
        markup.add(order1, connect, back2)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i5-10400F</b> '
                                                            '\nВидеокарта \n<b>GeForce GT 1030 2 ГБ</b> '
                                                            '\nОперативная память \n<b>8 ГБ</b> '
                                                            '\nХранение данных \n<b>512 ГБ</b> '
                                                            '\nМатеринская плата \n<b>MSI PRO H510M-B</b> '
                                                            '\nБлок питания \n<b>AeroCool VX PLUS 450W</b>'
                                                            '\nСтоимость \n<b>35 500 ₽</b>', parse_mode="html",
                         reply_markup=markup)

    elif call.data == "order1":
        model = 'ХАРАКТЕРИСТИКИ\n' '\nПроцессор \n<b>Intel Core i5-10400F</b> ' '\nВидеокарта \n<b>GeForce GT 1030 2 ГБ</b> ''\nОперативная память \n<b>8 ГБ</b> ''\nХранение данных \n<b>512 ГБ</b> ' '\nМатеринская плата \n<b>MSI PRO H510M-B</b> ''\nБлок питания \n<b>AeroCool VX PLUS 450W</b>''\nСтоимость \n<b>35 500 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id, text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')

    elif call.data == 'model_2':
        markup = types.InlineKeyboardMarkup(row_width=1)
        order2 = types.InlineKeyboardButton('Заказать', callback_data='order2')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back2 = types.InlineKeyboardButton('Назад', callback_data='back2')
        markup.add(order2, connect, back2)
        bot.send_message(chat_id=call.message.chat.id,
                         text='ХАРАКТЕРИСТИКИ\n'

                              '\nПроцессор \n<b>Intel Core i3-12100F</b> '
                              '\nВидеокарта \n<b>Radeon RX 550 4 ГБ</b> '
                              '\nОперативная память \n<b>16 ГБ</b> '
                              '\nХранение данных \n<b>512 ГБ</b> '
                              '\nМатеринская плата \n<b>MSI PRO H610M-E DDR4</b> '
                              '\nБлок питания \n<b>DEEPCOOL PF450</b>'
                              '\nСтоимость \n<b>44 000 ₽</b>', parse_mode="html", reply_markup=markup)

    elif call.data == "order2":
        model = 'ХАРАКТЕРИСТИКИ\n \nПроцессор \n<b>Intel Core i3-12100F</b> ''\nВидеокарта \n<b>Radeon RX 550 4 ГБ</b> ''\nОперативная память \n<b>16 ГБ</b> ''\nХранение данных \n<b>512 ГБ</b> ''\nМатеринская плата \n<b>MSI PRO H610M-E DDR4</b> ''\nБлок питания \n<b>DEEPCOOL PF450</b>' '\nСтоимость \n<b>44 000 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id, text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "model_3":
        markup = types.InlineKeyboardMarkup(row_width=1)
        order3 = types.InlineKeyboardButton('Заказать', callback_data='order3')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back2 = types.InlineKeyboardButton('Назад', callback_data='back2')
        markup.add(order3, connect, back2)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>AMD Ryzen 5 5600G</b> '
                                                            '\nВидеокарта \n<b>Radeon RX 6400 4 ГБ</b> '
                                                            '\nОперативная память \n<b>16 ГБ</b> '
                                                            '\nХранение данных \n<b>500 ГБ</b> '
                                                            '\nМатеринская плата \n<b>MSI A520M-A PRO</b> '
                                                            '\nБлок питания \n<b>AeroCool ECO 400W</b>'
                                                            '\nСтоимость \n<b>46 100 ₽</b>', parse_mode="html",
                         reply_markup=markup)

    elif call.data == "order3":
        model = 'ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>AMD Ryzen 5 5600G</b> ''\nВидеокарта \n<b>Radeon RX 6400 4 ГБ</b> ''\nОперативная память \n<b>16 ГБ</b> ''\nХранение данных \n<b>500 ГБ</b> ''\nМатеринская плата \n<b>MSI A520M-A PRO</b> ''\nБлок питания \n<b>AeroCool ECO 400W</b>''\nСтоимость \n<b>46 100 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id, text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "model_4":
        markup = types.InlineKeyboardMarkup(row_width=1)
        order4 = types.InlineKeyboardButton('Заказать', callback_data='order4')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back2 = types.InlineKeyboardButton('Назад', callback_data='back2')
        markup.add(order4, connect, back2)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i3-10105F</b> '
                                                            '\nВидеокарта \n<b>GeForce GTX 1650 4 ГБ</b> '
                                                            '\nОперативная память \n<b>8 ГБ</b> '
                                                            '\nХранение данных \n<b>1000 ГБ</b> '
                                                            '\nМатеринская плата \n<b>GIGABYTE H470M H</b> '
                                                            '\nБлок питания \n<b>ZALMAN Wattbit II 500W</b>'
                                                            '\nСтоимость \n<b>47 500 ₽</b>', parse_mode="html",
                         reply_markup=markup)

    elif call.data == "order4":
        model = 'ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i3-10105F</b> ' '\nВидеокарта \n<b>GeForce GTX 1650 4 ГБ</b> ''\nОперативная память \n<b>8 ГБ</b> ''\nХранение данных \n<b>1000 ГБ</b> ''\nМатеринская плата \n<b>GIGABYTE H470M H</b> ''\nБлок питания \n<b>ZALMAN Wattbit II 500W</b>''\nСтоимость \n<b>47 500 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')



    elif call.data == "model_5":
        markup = types.InlineKeyboardMarkup(row_width=1)
        order5 = types.InlineKeyboardButton('Заказать', callback_data='order5')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back2 = types.InlineKeyboardButton('Назад', callback_data='back2')
        markup.add(order5, connect, back2)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i5-10400F</b> '
                                                            '\nВидеокарта \n<b>GeForce GTX 1650 4 ГБ</b> '
                                                            '\nОперативная память \n<b>16 ГБ</b> '
                                                            '\nХранение данных \n<b>512 ГБ</b> '
                                                            '\nМатеринская плата \n<b>ASRock B560M-HDV/M.2</b> '
                                                            '\nБлок питания \n<b>DEEPCOOL PF650</b>'
                                                            '\nСтоимость \n<b>49 500 ₽</b>', parse_mode="html",
                         reply_markup=markup)


    elif call.data == "order5":
        model = 'ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i5-10400F</b> ''\nВидеокарта \n<b>GeForce GTX 1650 4 ГБ</b> ''\nОперативная память \n<b>16 ГБ</b> ''\nХранение данных \n<b>512 ГБ</b> ''\nМатеринская плата \n<b>ASRock B560M-HDV/M.2</b> ''\nБлок питания \n<b>DEEPCOOL PF650</b>''\nСтоимость \n<b>49 500 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "back2":
        markup = types.InlineKeyboardMarkup(row_width=1)
        comp1 = types.InlineKeyboardButton('i5-10400F x GT 1030 - 35 500 ₽', callback_data='model_1')
        comp2 = types.InlineKeyboardButton('i3-12100F х RX 550 - 44 000 ₽', callback_data='model_2')
        comp3 = types.InlineKeyboardButton('Ryzen 5 5600G х RX 6400 - 46 100 ₽', callback_data='model_3')
        comp4 = types.InlineKeyboardButton('i3-10105F х GTX 1650 - 47 500 ₽', callback_data='model_4')
        comp5 = types.InlineKeyboardButton('i5-10400F х GTX 1650 - 49 500 ₽', callback_data='model_5')
        back1 = types.InlineKeyboardButton('Назад', callback_data='back1')
        markup.add(comp1, comp2, comp3, comp4, comp5, back1)
        bot.send_message(chat_id=call.message.chat.id, text='Выберите ПК',
                              reply_markup=markup)

    elif call.data == 'price_2':
        markup = types.InlineKeyboardMarkup(row_width=1)
        button_model6 = types.InlineKeyboardButton("i5-10400F x RTX 3050 - 58 500 ₽", callback_data='model_6')
        button_model7 = types.InlineKeyboardButton("i3-12100F х RX 6600 - 63 500 ₽", callback_data='model_7')
        button_model8 = types.InlineKeyboardButton("Ryzen 5 5600 х GTX 1660 SUPER - 75 000 ₽", callback_data='model_8')
        button_model9 = types.InlineKeyboardButton("i5-12400F х RTX 4060 - 82 200 ₽", callback_data='model_9')
        button_model10 = types.InlineKeyboardButton("i3-12100F х RTX 3050 - 93 000 ₽", callback_data='model_10')
        button_back1 = types.InlineKeyboardButton("Назад", callback_data='back1')
        markup.add(button_model6, button_model7, button_model8, button_model9, button_model10, button_back1)
        bot.send_message(call.message.chat.id, "Выберите модель компьютера:", reply_markup=markup)


    elif call.data == 'model_6':
        markup = types.InlineKeyboardMarkup(row_width=1)
        order6 = types.InlineKeyboardButton('Заказать', callback_data='order6')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back3 = types.InlineKeyboardButton('Назад', callback_data='back3')
        markup.add(order6, connect, back3)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i5-10400F</b> '
                                                            '\nВидеокарта \n<b>GeForce RTX 3050 8 ГБ</b> '
                                                            '\nОперативная память \n<b>16 ГБ</b> '
                                                            '\nХранение данных \n<b>480 ГБ</b> '
                                                            '\nМатеринская плата \n<b>GIGABYTE H510M H</b> '
                                                            '\nБлок питания \n<b>Cougar STC 600</b>'
                                                            '\nСтоимость \n<b>58 500 ₽</b>', parse_mode="html",
                         reply_markup=markup)

    elif call.data == "order6":
        model ='ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i5-10400F</b> ' '\nВидеокарта \n<b>GeForce RTX 3050 8 ГБ</b> ''\nОперативная память \n<b>16 ГБ</b> ''\nХранение данных \n<b>480 ГБ</b> ''\nМатеринская плата \n<b>GIGABYTE H510M H</b> ''\nБлок питания \n<b>Cougar STC 600</b>''\nСтоимость \n<b>58 500 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == 'model_7':
        markup = types.InlineKeyboardMarkup(row_width=1)
        order7 = types.InlineKeyboardButton('Заказать', callback_data='order7')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back3 = types.InlineKeyboardButton('Назад', callback_data='back3')
        markup.add(order7, connect, back3)
        bot.send_message(chat_id=call.message.chat.id,
                         text='ХАРАКТЕРИСТИКИ\n'

                              '\nПроцессор \n<b>Intel Core i3-12100F</b> '
                              '\nВидеокарта \n<b>Radeon RX 6600 8 ГБ</b> '
                              '\nОперативная память \n<b>16 ГБ</b> '
                              '\nХранение данных \n<b>1 TБ</b> '
                              '\nМатеринская плата \n<b>GIGABYTE H610M K DDR4</b> '
                              '\nБлок питания \n<b>DEEPCOOL PF650 </b>'
                              '\nСтоимость \n<b>63 500 ₽</b>', parse_mode="html", reply_markup=markup)

    elif call.data == "order7":
        model ='ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i3-12100F</b> ''\nВидеокарта \n<b>Radeon RX 6600 8 ГБ</b> ''\nОперативная память \n<b>16 ГБ</b> ''\nХранение данных \n<b>1 TБ</b> ''\nМатеринская плата \n<b>GIGABYTE H610M K DDR4</b> ''\nБлок питания \n<b>DEEPCOOL PF650 </b>''\nСтоимость \n<b>63 500 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "model_8":
        markup = types.InlineKeyboardMarkup(row_width=1)
        order8 = types.InlineKeyboardButton('Заказать', callback_data='order8')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back3 = types.InlineKeyboardButton('Назад', callback_data='back3')
        markup.add(order8, connect, back3)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>AMD Ryzen 5 5600</b> '
                                                            '\nВидеокарта \n<b>GeForce GTX 1660 SUPER 6 ГБ</b> '
                                                            '\nОперативная память \n<b>16 ГБ</b> '
                                                            '\nХранение данных \n<b>1000 ГБ</b> '
                                                            '\nМатеринская плата \n<b>GIGABYTE B550M DS3H</b> '
                                                            '\nБлок питания \n<b>AeroCool AERO BRONZE 650M</b>'
                                                            '\nСтоимость \n<b>75 000 ₽</b>', parse_mode="html",
                         reply_markup=markup)

    elif call.data == "order8":
        model ='ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>AMD Ryzen 5 5600</b> ''\nВидеокарта \n<b>GeForce GTX 1660 SUPER 6 ГБ</b> ''\nОперативная память \n<b>16 ГБ</b> ''\nХранение данных \n<b>1000 ГБ</b> ''\nМатеринская плата \n<b>GIGABYTE B550M DS3H</b> ''\nБлок питания \n<b>AeroCool AERO BRONZE 650M</b>''\nСтоимость \n<b>75 000 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "model_9":
        markup = types.InlineKeyboardMarkup(row_width=1)
        order9 = types.InlineKeyboardButton('Заказать', callback_data='order9')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back3 = types.InlineKeyboardButton('Назад', callback_data='back3')
        markup.add(order9, connect, back3)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i5-12400F</b> '
                                                            '\nВидеокарта \n<b>GeForce RTX 4060 8 ГБ</b> '
                                                            '\nОперативная память \n<b>32 ГБ</b> '
                                                            '\nХранение данных \n<b>1024 ГБ</b> '
                                                            '\nМатеринская плата \n<b>MSI PRO H610M-E DDR4</b> '
                                                            '\nБлок питания \n<b>DEEPCOOL PF600</b>'
                                                            '\nСтоимость \n<b>82 200 ₽</b>', parse_mode="html",
                         reply_markup=markup)

    elif call.data == "order9":
        model ='ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i5-12400F</b> ''\nВидеокарта \n<b>GeForce RTX 4060 8 ГБ</b> ''\nОперативная память \n<b>32 ГБ</b> ''\nХранение данных \n<b>1024 ГБ</b> ''\nМатеринская плата \n<b>MSI PRO H610M-E DDR4</b> ''\nБлок питания \n<b>DEEPCOOL PF600</b>''\nСтоимость \n<b>82 200 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "model_10":
        markup = types.InlineKeyboardMarkup(row_width=1)
        order10 = types.InlineKeyboardButton('Заказать', callback_data='order10')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back3 = types.InlineKeyboardButton('Назад', callback_data='back3')
        markup.add(order10, connect, back3)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i3-12100F</b> '
                                                            '\nВидеокарта \n<b>GeForce RTX 3050 8 ГБ</b> '
                                                            '\nОперативная память \n<b>32 ГБ</b> '
                                                            '\nХранение данных \n<b>1024 ГБ</b> '
                                                            '\nМатеринская плата \n<b>MSI PRO B760M-A WIFI DDR4</b> '
                                                            '\nБлок питания \n<b> DEEPCOOL PK700D</b>'
                                                            '\nСтоимость \n<b>93 000 ₽</b>', parse_mode="html",
                         reply_markup=markup)


    elif call.data == "order10":
        model ='ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i3-12100F</b> ''\nВидеокарта \n<b>GeForce RTX 3050 8 ГБ</b> ''\nОперативная память \n<b>32 ГБ</b> ''\nХранение данных \n<b>1024 ГБ</b> ''\nМатеринская плата \n<b>MSI PRO B760M-A WIFI DDR4</b> ''\nБлок питания \n<b> DEEPCOOL PK700D</b>''\nСтоимость \n<b>93 000 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "back3":
        markup = types.InlineKeyboardMarkup(row_width=1)
        button_model6 = types.InlineKeyboardButton("i5-10400F x RTX 3050 - 58 500 ₽", callback_data='model_6')
        button_model7 = types.InlineKeyboardButton("i3-12100F х RX 6600 - 63 500 ₽", callback_data='model_7')
        button_model8 = types.InlineKeyboardButton("Ryzen 5 5600 х GTX 1660 SUPER - 75 000 ₽", callback_data='model_8')
        button_model9 = types.InlineKeyboardButton("i5-12400F х RTX 4060 - 82 200 ₽", callback_data='model_9')
        button_model10 = types.InlineKeyboardButton("i3-12100F х RTX 3050 - 93 000 ₽", callback_data='model_10')
        button_back1 = types.InlineKeyboardButton("Назад", callback_data='back1')
        markup.add(button_model6, button_model7, button_model8, button_model9, button_model10, button_back1)
        bot.send_message(call.message.chat.id, "Выберите модель компьютера:", reply_markup=markup)


    elif call.data == 'price_3':
        markup = types.InlineKeyboardMarkup(row_width=1)
        button_model11 = types.InlineKeyboardButton("i5-12400F x RTX 4060 Ti - 122 000 ₽", callback_data='model_11')
        button_model12 = types.InlineKeyboardButton("i5-12400F х RTX 4070 SUPER - 133 500 ₽", callback_data='model_12')
        button_model13 = types.InlineKeyboardButton("i5-13490F х RTX 4060 - 144 000 ₽",
                                                    callback_data='model_13')
        button_model14 = types.InlineKeyboardButton("i7-13700F х RTX 4070 - 152 200 ₽", callback_data='model_14')
        button_model15 = types.InlineKeyboardButton("i5-14600KF х RTX 4070 - 194 500 ₽", callback_data='model_15')
        button_back1 = types.InlineKeyboardButton("Назад", callback_data='back1')
        markup.add(button_model11, button_model12, button_model13, button_model14, button_model15, button_back1)
        bot.send_message(call.message.chat.id, "Выберите модель компьютера:", reply_markup=markup)


    elif call.data == 'model_11':
        markup = types.InlineKeyboardMarkup(row_width=1)
        order11 = types.InlineKeyboardButton('Заказать', callback_data='order11')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back4 = types.InlineKeyboardButton('Назад', callback_data='back4')
        markup.add(order11, connect, back4)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i5-12400F</b> '
                                                            '\nВидеокарта \n<b>GeForce RTX 4060 Ti 8 ГБ</b> '
                                                            '\nОперативная память \n<b>32 ГБ</b> '
                                                            '\nХранение данных \n<b>1000 ГБ</b> '
                                                            '\nМатеринская плата \n<b>ASRock B760M Steel Legend WiFi</b> '
                                                            '\nБлок питания \n<b>DEEPCOOL PM800D</b>'
                                                            '\nСтоимость \n<b>122 000 ₽</b>', parse_mode="html",
                         reply_markup=markup)

    elif call.data == "order11":
        model ='ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i5-12400F</b> ''\nВидеокарта \n<b>GeForce RTX 4060 Ti 8 ГБ</b> ''\nОперативная память \n<b>32 ГБ</b> ''\nХранение данных \n<b>1000 ГБ</b> ''\nМатеринская плата \n<b>ASRock B760M Steel Legend WiFi</b> ''\nБлок питания \n<b>DEEPCOOL PM800D</b>''\nСтоимость \n<b>122 000 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == 'model_12':
        markup = types.InlineKeyboardMarkup(row_width=1)
        order12 = types.InlineKeyboardButton('Заказать', callback_data='order12')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back4 = types.InlineKeyboardButton('Назад', callback_data='back4')
        markup.add(order12, connect, back4)
        bot.send_message(chat_id=call.message.chat.id,
                         text='ХАРАКТЕРИСТИКИ\n'

                              '\nПроцессор \n<b>Intel Core i5-12400F</b> '
                              '\nВидеокарта \n<b>GeForce RTX 4070 SUPER 12 ГБ</b> '
                              '\nОперативная память \n<b>32 ГБ</b> '
                              '\nХранение данных \n<b>500 ГБ</b> '
                              '\nМатеринская плата \n<b>MSI PRO B760M-P DDR4</b> '
                              '\nБлок питания \n<b>Cougar GEX X2 850</b>'
                              '\nСтоимость \n<b>133 500 ₽</b>', parse_mode="html", reply_markup=markup)


    elif call.data == "order12":
        model ='ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i5-12400F</b> ''\nВидеокарта \n<b>GeForce RTX 4070 SUPER 12 ГБ</b> ''\nОперативная память \n<b>32 ГБ</b> ''\nХранение данных \n<b>500 ГБ</b> ''\nМатеринская плата \n<b>MSI PRO B760M-P DDR4</b> ''\nБлок питания \n<b>Cougar GEX X2 850</b>''\nСтоимость \n<b>133 500 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "model_13":
        markup = types.InlineKeyboardMarkup(row_width=1)
        order13 = types.InlineKeyboardButton('Заказать', callback_data='order13')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back4 = types.InlineKeyboardButton('Назад', callback_data='back4')
        markup.add(order13, connect, back4)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i5-13490F</b> '
                                                            '\nВидеокарта \n<b>GeForce RTX 4060 8 ГБ</b> '
                                                            '\nОперативная память \n<b>2x16 ГБ</b> '
                                                            '\nХранение данных \n<b>2000 ГБ</b> '
                                                            '\nМатеринская плата \n<b>ASRock B760M Steel Legend WiFi</b> '
                                                            '\nБлок питания \n<b>DEEPCOOL PF700</b>'
                                                            '\nСтоимость \n<b>144 000 ₽</b>', parse_mode="html",
                         reply_markup=markup)


    elif call.data == "order13":
        model = 'ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i5-13490F</b> ''\nВидеокарта \n<b>GeForce RTX 4060 8 ГБ</b> ''\nОперативная память \n<b>2x16 ГБ</b> ''\nХранение данных \n<b>2000 ГБ</b> ''\nМатеринская плата \n<b>ASRock B760M Steel Legend WiFi</b> ''\nБлок питания \n<b>DEEPCOOL PF700</b>''\nСтоимость \n<b>144 000 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "model_14":
        markup = types.InlineKeyboardMarkup(row_width=1)
        order14 = types.InlineKeyboardButton('Заказать', callback_data='order14')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back4 = types.InlineKeyboardButton('Назад', callback_data='back4')
        markup.add(order14, connect, back4)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i7-13700F</b> '
                                                            '\nВидеокарта \n<b>GeForce RTX 4070 12 ГБ</b> '
                                                            '\nОперативная память \n<b>32 ГБ</b> '
                                                            '\nХранение данных \n<b>1000 ГБ</b> '
                                                            '\nМатеринская плата \n<b>GIGABYTE B760M DS3H</b> '
                                                            '\nБлок питания \n<b>DEEPCOOL PF750</b>'
                                                            '\nСтоимость \n<b>152 200 ₽</b>', parse_mode="html",
                         reply_markup=markup)

    elif call.data == "order14":
        model = 'ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i7-13700F</b> ''\nВидеокарта \n<b>GeForce RTX 4070 12 ГБ</b> ''\nОперативная память \n<b>32 ГБ</b> ''\nХранение данных \n<b>1000 ГБ</b> ''\nМатеринская плата \n<b>GIGABYTE B760M DS3H</b> ''\nБлок питания \n<b>DEEPCOOL PF750</b>''\nСтоимость \n<b>152 200 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "model_15":
        markup = types.InlineKeyboardMarkup(row_width=1)
        order15 = types.InlineKeyboardButton('Заказать', callback_data='order15')
        connect = types.InlineKeyboardButton(text='Связь с менеджером')
        back4 = types.InlineKeyboardButton('Назад', callback_data='back4')
        markup.add(order15, connect, back4)
        bot.send_message(chat_id=call.message.chat.id, text='ХАРАКТЕРИСТИКИ\n'
                                                            '\nПроцессор \n<b>Intel Core i5-14600KF</b> '
                                                            '\nВидеокарта \n<b>GeForce RTX 4070 12 ГБ</b> '
                                                            '\nОперативная память \n<b>32 ГБ</b> '
                                                            '\nХранение данных \n<b>500 ГБ</b> '
                                                            '\nМатеринская плата \n<b>MSI PRO Z790-A MAX WIFI</b> '
                                                            '\nБлок питания \n<b>Thermaltake Toughpower GF1 Snow 850W</b>'
                                                            '\nСтоимость \n<b>194 500 ₽</b>', parse_mode="html",
                         reply_markup=markup)

    elif call.data == "order15":
        model = 'ХАРАКТЕРИСТИКИ\n''\nПроцессор \n<b>Intel Core i5-14600KF</b> ''\nВидеокарта \n<b>GeForce RTX 4070 12 ГБ</b> ''\nОперативная память \n<b>32 ГБ</b> ''\nХранение данных \n<b>500 ГБ</b> ''\nМатеринская плата \n<b>MSI PRO Z790-A MAX WIFI</b> ''\nБлок питания \n<b>Thermaltake Toughpower GF1 Snow 850W</b>''\nСтоимость \n<b>194 500 ₽</b>'
        bot.send_message("396717696", f"Покупатель: @{call.from_user.username}\nМодель: {model}", parse_mode="html")
        bot.send_message(call.message.chat.id,
                         text='Ваш заказ принят! В ближайшее время с вами свяжется менеджер для подтверждения и оплаты.')


    elif call.data == "back4":
        markup = types.InlineKeyboardMarkup(row_width=1)
        button_model11 = types.InlineKeyboardButton("i5-12400F x RTX 4060 Ti - 122 000 ₽", callback_data='model_11')
        button_model12 = types.InlineKeyboardButton("i5-12400F х RTX 4070 SUPER - 133 500 ₽", callback_data='model_12')
        button_model13 = types.InlineKeyboardButton("i5-13490F х RTX 4060 - 144 000 ₽",
                                                    callback_data='model_13')
        button_model14 = types.InlineKeyboardButton("i7-13700F х RTX 4070 - 152 200 ₽", callback_data='model_14')
        button_model15 = types.InlineKeyboardButton("i5-14600KF х RTX 4070 - 194 500 ₽", callback_data='model_15')
        button_back1 = types.InlineKeyboardButton("Назад", callback_data='back1')
        markup.add(button_model11, button_model12, button_model13, button_model14, button_model15, button_back1)
        bot.send_message(call.message.chat.id, "Выберите модель компьютера:", reply_markup=markup)


bot.polling()
