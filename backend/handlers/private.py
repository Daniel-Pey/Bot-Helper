from ..bot import bot
from backend.config import config


@bot.message_handler(func=lambda x: x.reply_to_message and x.reply_to_message.text.startswith('Ответ от Дани:'))
def reply_to_admin_answer(message):
    bot.send_message(config.ADMIN_ID, message.from_user.id + '\n' + message.text)