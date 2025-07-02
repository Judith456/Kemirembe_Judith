#Create an AI agent that automates tasks of creating posts on social media platforms like Telegram using Python
 
import asyncio
from telegram import Bot
import random
import logging

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token
BOT_TOKEN = "7747970214:AAHJ_NAJ9nvsXWnQV1-MA3klrcz3EBmIlSs"

# Channel username or numeric chat ID
CHANNEL_ID = "@mydailypostschannel" 

bot = Bot(token=BOT_TOKEN)

# Messages
messages = [
    "Good morning! Here's your daily dose of inspiration.",
    "Did you know? The Eiffel Tower can be 15 cm taller during the summer.",
    "Take a deep breath and relax. Don't forget to stretch!",
    "Honey never spoils. 3000-year-old pots are still edible!",
    "Quote of the day: 'The only way to do great work is to love what you do.' - Steve Jobs",
    "Happiness! What are your plans?",
    "The day vibes! What movies are you watching?",
    "We all need a day where we can reflect, pray, and worship.",
]

async def post_message():
    message = random.choice(messages)
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=message)
        logger.info(f"Posted to Telegram: {message}")
    except Exception as e:
        logger.error(f"Error posting: {str(e)}")

if __name__ == "__main__":
    asyncio.run(post_message())
    
    
#NOTE: This code is designed to post random message to my channel when run
