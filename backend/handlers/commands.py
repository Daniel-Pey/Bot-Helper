from ..bot import bot
from ..config import config
from ..registration import registrate_user
from backend.keyboards.inline_keyboards import *


@bot.message_handler(commands=["start"], chat_types=['private'])
def start_answer(msg):
    """ First bot answer"""

    bot.send_message(
        msg.chat.id,
        """Привет! Я личный бот-помщник Дани

Чем могу помочь?""",
        reply_markup=commands_keyboard()
        )


@bot.message_handler(commands=['reg'])
def registrate(msg):
    """Обработчик команды /reg"""
    bot.send_message(msg.chat.id, "Отлично для этого мне нужно чтобы немного рассказал о себе 🤪")
    bot.register_next_step_handler(msg, registrate_user)