import os
import telebot
from pymongo import MongoClient

TOKEN = os.environ.get('BOT_TOKEN', '9282120047:AAH3PGGwrwVYdpGiR-7JmjgldXrWkjA8uaE')
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://chathumaldevinda14_db_user:1pp9HpMpGw0NMeah@cluster0.3vsaj5d.mongodb.net/')
GROUP_ID = int(os.environ.get('GROUP_ID', '-5588131565'))

# Ads Links
MONETAG_LINK = os.environ.get('MONETAG_LINK', 'https://uplcm.com/4/12109270')
ADSTERRA_LINK = os.environ.get('ADSTERRA_LINK', 'https://auctionr.org/4/958decefa1d46a3a7ab59f93e40bf1c0')

bot = telebot.TeleBot(TOKEN)
client = MongoClient(MONGO_URI)
db = client['telegram_bot_db']
links_collection = db['gated_links']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ආයුබෝවන්! Link Gating Bot වෙත සාදරයෙන් පිළිගනිමු.")

@bot.message_handler(commands=['send'])
def send_link_to_group(message):
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        target_link = args[1]
        
        # Monetag සහ Adsterra දැන්වීම් එකතු කළ පණිවිඩය
        gated_message = (
            f"🔥 **නව අන්තර්ගතයක් ලබා ගැනීමට පහත පියවර අනුගමනය කරන්න!**\n\n"
            f"1️⃣ පළමුව මෙම Monetag ලින්ක් එක ක්ලික් කරන්න:\n👉 {MONETAG_LINK}\n\n"
            f"2️⃣ දෙවනුව මෙම Adsterra ලින්ක් එකත් ක්ලික් කරන්න:\n👉 {ADSTERRA_LINK}\n\n"
            f"3️⃣ ඊට පසු ඔබේ සැබෑ ලින්ක් එක මෙතැනින් ලබා ගන්න:\n👉 {target_link}"
        )
        
        try:
            bot.send_message(chat_id=GROUP_ID, text=gated_message, parse_mode="Markdown")
            bot.reply_to(message, "සාර්ථකව Public Group එකට දැන්වීම් සමඟ ලින්ක් එක යවන ලදී!")
        except Exception as e:
            bot.reply_to(message, f"දෝෂයක් සිදු විය: {str(e)}")
    else:
        bot.reply_to(message, "කරුණාකර /send විධානය සමඟ නිවැරදි ලින්ක් එකක් ඇතුළත් කරන්න.\n(උදා: /send https://example.com)")