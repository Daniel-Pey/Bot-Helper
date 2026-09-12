from ..bot import bot
from backend.utils import send_anon_message_to_admin


@bot.message_handler(func=lambda x: x.reply_to_message and x.reply_to_message.text.startswith('Ответ от Дани:'))
def reply_to_admin_answer(message):
    send_anon_message_to_admin(message)