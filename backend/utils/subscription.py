from backend.bot import bot
from backend.config import config


def is_subscribed(message):
    """
    Проверяет, подписан ли отправитель сообщения на указанный канал.
    
    Args:
        message: объект сообщения из telebot
    
    Returns:
        bool: True если пользователь подписан, иначе False
    """

    try:
        user_id = message.from_user.id
        member = bot.get_chat_member(config.CHANNEL_ID, user_id)
        
        # Статусы, при которых пользователь считается подписанным
        subscribed_statuses = ['member', 'administrator', 'creator']
        
        return member.status in subscribed_statuses
    except Exception as e:
        print(f"Ошибка проверки подписки: {e}")
        return False