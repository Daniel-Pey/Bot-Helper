from backend.bot import bot
from backend.config import config


@bot.message_handler(func=lambda x: int(x.from_user.id) == config.ADMIN_ID)
def admin_answer_for_anon(message):
    """Ответ админа на анонимное сообщение"""

    if message.reply_to_message and not message.reply_to_message.text.startswith('Ответ от Дани:'):
        replied_message = message.reply_to_message.text
        anon_id = replied_message[:replied_message.index('\n')]
        try:
            bot.send_message(anon_id, "Ответ от Дани:\n------------\n" + message.text + "\n------------\nВы можете отправить Дане ответ, ответив на это сообщение")
            bot.send_message(config.ADMIN_ID, "✅ Ваше сообщение отправлено")
        except Exception as e:
            bot.send_message(config.ADMIN_ID, f"❌ Не получилось ответить на сообщение:\n{e}")
    else:
        bot.send_message(config.ADMIN_ID, 'Bla')