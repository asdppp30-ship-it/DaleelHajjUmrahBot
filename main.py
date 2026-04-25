import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# تفعيل التزامن
nest_asyncio.apply()

# تأكد أن السطر التالي يبدو هكذا تماماً
TOKEN = "8249232952:AAEKRhu4DkN-RgThncPkDiR6SdrmvsxhomI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🇸🇦 العربية", callback_data="ar"),
                 InlineKeyboardButton("🇬🇧 English", callback_data="en")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("مرحباً بك في دليل الحج والعمرة 🕋\nاختر لغتك:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="قريباً سيتم إضافة كافة المناسك... جاري التحديث.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling(drop_pending_updates=True)
