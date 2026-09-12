from backend.bot import bot
from backend.utils import send_anon_message_to_admin
from telebot import types


bot.callback_query_handler(func=lambda call: call.data == "anon_message")
def anon_message_callback_handler(call):
    msg = bot.send_message(call.from_user.id, "Отлично! Напиши сообщение, которое я должен передать Дане:")
    bot.register_next_step_handler(msg, callback=send_anon_message_to_admin)