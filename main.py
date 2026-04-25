import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# تفعيل التزامن ليعمل البوت على السيرفرات السحابية
nest_asyncio.apply()

# --- تنبيه: ضع التوكن الخاص بك بين العلامات " " في السطر التالي ---
TOKEN =8249232952:AAHOd-k4P270nODrIwIcGq8fGb6C2L6dQY4

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إنشاء أزرار اختيار اللغة
    keyboard = [
        [
            InlineKeyboardButton("🇸🇦 العربية", callback_data="ar"),
            InlineKeyboardButton("🇬🇧 English", callback_data="en")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # رسالة الترحيب
    await update.message.reply_text(
        "مرحباً بك في دليل الحج والعمرة 🕋\nاختر لغتك المفضلة لبدء الاستخدام:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # رسالة مؤقتة عند الضغط على الزر
    await query.edit_message_text(text="قريباً سيتم إضافة كافة المناسك والأدعية... جاري العمل على التحديث.")

if __name__ == '__main__':
    # بناء وتطوير التطبيق
    application = ApplicationBuilder().token(TOKEN).build()
    
    # إضافة الأوامر (Command Handlers)
    application.add_handler(CommandHandler('start', start))
    
    # إضافة مستجيب الأزرار (Callback Query Handler)
    application.add_handler(CallbackQueryHandler(button))
    
    print("Bot is running...")
    # تشغيل البوت مع مسح التحديثات القديمة لتفادي التعليق
    application.run_polling(drop_pending_updates=True)
