import nest_asyncio
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# هذا السطر مهم جداً ليعمل الكود على السيرفرات الخارجية
nest_asyncio.apply()

# ضع التوكن الخاص بك هنا بين العلامتين
TOKEN = 8249232952:AAHOd-k4P270nODrIwIcGq8fGb6C2L6dQY4

# دالة البداية /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇸🇦 العربية", callback_data="ar"),
         InlineKeyboardButton("🇬🇧 English", callback_data="en")],
        [InlineKeyboardButton("🇮🇩 Indonesia", callback_data="id")],
        [InlineKeyboardButton("🇵🇰 Urdu", callback_data="ur"),
         InlineKeyboardButton("🇹🇷 Türkçe", callback_data="tr")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "مرحبًا بك في دليلك للحج والعمرة 🕋✨\n\nاختر لغتك:",
        reply_markup=reply_markup
    )

# دالة التحكم بالأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # القائمة التي تظهر بعد اختيار اللغة
    keyboard = [
        [InlineKeyboardButton("🕋 المناسك", callback_data="manasik"), 
         InlineKeyboardButton("📖 الأدعية", callback_data="dua")],
        [InlineKeyboardButton("📍 المواقع", callback_data="locations"), 
         InlineKeyboardButton("🚐 المواصلات", callback_data="transport")],
        [InlineKeyboardButton("🎁 المتجر", callback_data="store"), 
         InlineKeyboardButton("☎️ الدعم", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "اختر من القائمة:",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    # بناء وتشغيل البوت
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    
    print("البوت يعمل الآن... اذهب لتجربته!")
    app.run_polling()
