import telebot as tlb
import datetime
import timeit
import time

import botinit

bot = botinit.bot

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time} секунд")
        return result
    return wrapper

@bot.message_handler(commands=['start'])
@timing_decorator
def reaction_command_start(mess: tlb.types.Message):
    message = 'Start BOT'
    bot.send_message(mess.from_user.id, message, reply_markup=botinit.markup)

@bot.message_handler(content_types=['text'])
@timing_decorator
def reaction_message(mess: tlb.types.Message):
    if mess.text == 'Как дела?':
        message = 'Да не плохо вобщем-то!'
        bot.send_message(mess.from_user.id, message)
    elif mess.text == botinit.button_info.text:
        # bot.send_message(mess.chat.id, mess)
        date = datetime.datetime.fromtimestamp(mess.json['date'])
        bot.send_message(mess.chat.id, date)
        # MESS = mess.__dict__
        # for k, v in MESS.items():
        #     print('___________')
        #     print(k)
        #     print(v)
        #     print(datetime.datetime.fromtimestamp(mess.json['date'])
    else:
        bot.send_message(mess.from_user.id, mess.text, reply_markup=botinit.inlinemrk)

@bot.callback_query_handler(func = lambda func: True)
@timing_decorator
def callback_reaction(call: tlb.types.CallbackQuery):
    if call.data == botinit.inlbutton_poo.callback_data:
        bot.send_message(call.message.chat.id, '💩')

if __name__ == '__main__':
    bot.polling(non_stop=True)