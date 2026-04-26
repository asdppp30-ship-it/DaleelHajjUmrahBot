import nest_asyncio
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

nest_asyncio.apply()

TOKEN = "YOUR_NEW_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("🇸🇦 العربية", callback_data="ar"),
        InlineKeyboardButton("🇬🇧 English", callback_data="en")
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "مرحباً بك في دليل الحج والعمرة 🕋\nاختر اللغة:",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    try:
        print("--- بدأ تشغيل البوت ---")
        application = ApplicationBuilder().token(TOKEN).build()
        application.add_handler(CommandHandler('start', start))
        print("--- البوت شغال الآن ---")
        application.run_polling(drop_pending_updates=True)

    except Exception as e:
        print(f"خطأ قاتل: {e}")
        sys.exit(1)
