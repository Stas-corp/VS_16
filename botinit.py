import telebot as tlb

import tokens

bot = tlb.TeleBot(tokens.TOKEN)

bot.set_my_commands([
    tlb.types.BotCommand('start', 'запуск/перзапуск бота'),
    tlb.types.BotCommand('help', 'помощь/описание бота')
])

markup = tlb.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

