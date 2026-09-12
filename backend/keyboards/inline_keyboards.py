from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from backend.config import config


def social_networks_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с нашими социльными сетями"""

    markup = InlineKeyboardMarkup()
    
    for name, link in config.SOCIAL_NETWORKS.items():
            btn = InlineKeyboardButton(
                text=name,
                url=link
                
            )
            markup.add(btn)
    
    return markup


def commands_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура команд"""
    
    markup = InlineKeyboardMarkup()
    
    for name, callback in config.COMMANDS.items():
        btn = InlineKeyboardButton(
            text=name,
            callback_data=callback
        )
        markup.add(btn)
    
    return markup