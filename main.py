from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import(
    main_menu_keyboard,
    courses_menu_keyboard
)
from key_buttons import tele_button, courses

ABOUT = tele_button[0]
COURSES = tele_button[1]
PYTHON = courses[0]
JAVA = courses[1]
JS = courses[2]
QA = courses[3]
MENY = courses[4]
WHERE = tele_button[2]

def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать {update.effective_user.username}\nэтот бот расскажет о наших курсах',
        reply_markup=main_menu_keyboard()
    )

def about(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Преимущества обучение в Codify.Обучение с нуля до Junior.',
    )

def reply_coutses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Choose course',
        reply_markup=courses_menu_keyboard()
    )

def python(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Python — это язык общего назначения, то есть он может использоваться для создания множества различных программ и не специализируется на каких-либо конкретных проблемах. Эта универсальность, наряду с удобством для начинающих, сделала его одним из наиболее часто используемых языков программирования на сегодняшний день.'
    )

def java(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Java — строго типизированный объектно-ориентированный язык программирования общего назначения, разработанный компанией Sun Microsystems (в последующем приобретённой компанией Oracle).'
    )

def js(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'JavaScript – это язык программирования, который добавляет интерактивность на ваш веб-сайт (например: игры, отклик при нажатии кнопок или при вводе данных в формы, динамические стили, анимация).'
    )

def qa(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Тестировщик — это специалист, который занимается тестированием программного обеспечения с целью выявления ошибок и недоработок. Он проводит различные виды тестирования, например, функциональное, интеграционное, системное, производительности и т. д'
    )

def menu(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'back',
        reply_markup=main_menu_keyboard()
    )

def where(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'7 микрарайон, 23'
    )

updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSES),
    reply_coutses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JAVA),
    java
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    js
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(QA),
    qa
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MENY),
    menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(WHERE),
    where
))

updater.start_polling()
updater.idle()