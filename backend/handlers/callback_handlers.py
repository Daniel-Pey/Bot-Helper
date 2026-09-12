from backend.bot import bot
from backend.utils import send_anon_message_to_admin
from telebot import types
from backend.keyboards import social_networks_keyboard


@bot.callback_query_handler(func=lambda call: call.data == "anon_message")
def anon_message_callback_handler(call):
    """Отправка анонимных сообщений админу"""

    msg = bot.send_message(call.message.from_user.id, "Отлично! Напиши сообщение, которое я должен передать Дане:")
    bot.register_next_step_handler(msg, callback=send_anon_message_to_admin)


@bot.callback_query_handler(func=lambda call: call.data == "social_networks")
def social_networks(call):
    bot.send_message(call.message.from_user.id, 'Наши социальные сети 👇', reply_markup=social_networks_keyboard())