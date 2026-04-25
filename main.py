import nest_asyncio
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

nest_asyncio.apply()

TOKEN = "8249232952:AAEKRhu4DkN-RgThncPkDiR6SdrmvsxhomI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🇸🇦 العربية", callback_data="ar"),
                 InlineKeyboardButton("🇬🇧 English", callback_data="en")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("مرحباً بك في دليل الحج والعمرة 🕋\nاختر اللغة:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="جاري التجهيز... قريباً")

if __name__ == '__main__':
    # بناء التطبيق مع إعدادات حماية للشبكة
    application = ApplicationBuilder().token(TOKEN).connect_timeout(30).read_timeout(30).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    
    print("Starting bot...")
    application.run_polling(drop_pending_updates=True)
