import nest_asyncio
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# هذا السطر مهم جداً ليعمل الكود على السيرفرات الخارجية مثل Render
nest_asyncio.apply()

# --- ضع التوكن الخاص بك بين العلامات " " في السطر التالي ---
TOKEN =8249232952:AAEKRhu4DkN-RgThncPkDiR6SdrmvsxhomI

# دالة الترحيب التي تظهر عند كتابة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إنشاء أزرار اختيار اللغة (تظهر تحت الرسالة)
    keyboard = [
        [
            InlineKeyboardButton("🇸🇦 العربية", callback_data="ar"),
            InlineKeyboardButton("🇬🇧 English", callback_data="en")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # إرسال الرسالة للمستخدم
    await update.message.reply_text(
        "مرحباً بك في دليل الحج والعمرة 🕋\nاختر لغتك المفضلة لبدء الاستخدام:",
        reply_markup=reply_markup
    )

# دالة التعامل مع ضغطات الأزرار
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # لإزالة علامة التحميل من الزر
    
    # تغيير نص الرسالة عند الضغط على أي زر
    await query.edit_message_text(text="قريباً سيتم إضافة كافة المناسك والأدعية... جاري العمل على التحديث.")

# الجزء المسؤول عن تشغيل البوت
if __name__ == '__main__':
    # بناء التطبيق باستخدام التوكن
    application = ApplicationBuilder().token(TOKEN).build()
    
    # ربط الأوامر بالوظائف (لما يكتب /start ينفذ دالة start)
    application.add_handler(CommandHandler('start', start))
    
    # ربط الأزرار بدالة button
    application.add_handler(CallbackQueryHandler(button))
    
    print("Bot is running...") # تظهر في سجلات Render لتؤكد أن البوت عمل
    
    # تشغيل البوت واستقبال الرسائل
    application.run_polling(drop_pending_updates=True)
