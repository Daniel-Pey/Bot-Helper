from backend.bot import bot
from backend.config import config


def send_anon_message_to_admin(message):
    """Отправляет админу анонимное сообщение

    Args:
        message (_type_): Сообщение для админа
    """
    try:
        bot.send_message(config.ADMIN_ID, str(message.from_user.id) + "\n" + message.text)
        bot.send_message(message.from_user.id, "✅ Ваше сообщение отправлено")
    except Exception:
        bot.send_message(message.from_user.id, '❌ К сожалению возникла ошибка и выше сообщение не дошло...')