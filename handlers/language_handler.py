from telebot import TeleBot
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from . import add_user
from shows.request_phone_number import request_phone_number

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
bot = TeleBot(bot_token)



    


