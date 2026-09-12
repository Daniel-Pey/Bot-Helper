from ..bot import bot
from backend.utils import is_subscribed


@bot.message_handler(chat_types=['group'])
def group_message(message):
    if not is_subscribed(message):
        bot.delete_message(message.chat.id, message.message_id)