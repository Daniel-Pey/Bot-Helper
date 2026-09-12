from ..bot import bot
from ..config import config
from ..registration import registrate_user
from backend.keyboards.inline_keyboards import *
from backend.utils import send_anon_message_to_admin


@bot.message_handler(commands=["start"])
def start_answer(msg):
    """ First bot answer"""

    if msg.chat.type != 'private':
        bot.send_message(msg.chat.id, 'Эта команда доступна только в личном чате с ботом...')
        return

    bot.send_message(
        msg.chat.id,
        """Привет! Я личный бот-помщник Дани

Чем могу помочь?""",
        reply_markup=commands_keyboard()
        )


@bot.message_handler(commands=['anon'])
def send_anon_message_command(message):
    if message.chat.type != 'private':
        bot.send_message(message.chat.id, 'Эта команда доступна только в личном чате с ботом...')
        return

    send_anon_message_to_admin(message)