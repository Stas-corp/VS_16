import telebot as tlb
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
def reaction_command_start(mess: tlb.types.Message):
    bot.send_message(mess.from_user.id, mess, reply_markup=botinit.markup)

@bot.message_handler(content_types=['text'])
def reaction_message(mess: tlb.types.Message):
    if mess.text == 'Как дела?':
        message = 'Да не плохо вобщем-то!'
        bot.send_message(mess.from_user.id, message)
    else:
        bot.send_message(mess.from_user.id, mess.text)

if __name__ == '__main__':
    bot.polling(non_stop=True)