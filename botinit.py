import telebot as tlb

import tokens

bot = tlb.TeleBot(tokens.TOKEN)

bot.set_my_commands([
    tlb.types.BotCommand('start', 'запуск/перзапуск бота'),
    tlb.types.BotCommand('help', 'помощь/описание бота')
])

markup = tlb.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
button_info = tlb.types.KeyboardButton('Now Date 🕰')
markup.add(
    button_info
)

inlinemrk = tlb.types.InlineKeyboardMarkup()
inlbutton_poo = tlb.types.InlineKeyboardButton(text='PoO', callback_data='💩')
inlinemrk.add(
    inlbutton_poo
)