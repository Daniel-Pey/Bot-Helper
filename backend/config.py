import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    TELEBOT_TOKEN = os.getenv("TELEBOT_TOKEN")
    
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    
    CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
    
    COMMANDS = {
        "Анонимное сообщение 🥷": "anon_message",
        "Наши социальные сети 📱": "social_networks"
    }

    DATABASE_PATH = "data/users.db"
    
    SOCIAL_NETWORKS = {
        "GitHub": "https://github.com/Daniel-Pey",
        "ВК": "https://vk.ru/daniel_pey",
        "TG": "https://t.me/D_main_D",
        "Instagram": "https://www.instagram.com/danielpeyson/"
    }


config = Config()