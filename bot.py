from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler
from telegram.ext import filters

class Bot:
    def __init__(self, token, psychologist_username):
        self.token = token
        self.psychologist_username = psychologist_username
        self.application = Application.builder().token(self.token).build()

    async def start(self, update, context):
        buttons = [['Теоретичні відомості'], ['Тести'], ['Зв\'язатися з психологом компанії']]
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаємо! Я психологічний бот компанії. Оберіть опцію:", reply_markup=ReplyKeyboardMarkup(buttons))

    # Пункт 1: Теоретичні відомості
    async def send_theoretical_info(self, update, context):
        info_text = (
            "Стрес:\nЦе реакція організму на виклики або тиск. "
            "Методи подолання: регулярні фізичні вправи, дихальні техніки.\n\n"
            "Емоційне вигорання:\nХронічний стрес на роботі. "
            "Методи: відпочинок, зміна діяльності.\n\n"
            "Тривожність:\nЦе відчуття неспокою або страху. "
            "Методи: медитація, релаксація.\n\n"
            "Способи релаксації: дихальні вправи, медитація, прогулянки."
        )
        await context.bot.send_message(chat_id=update.effective_chat.id, text=info_text)

    # Пункт 2: Тести (Пример тестового вопроса)
    async def send_test_question(self, update, context):
        question = "Як часто ви відчуваєте втому протягом дня?\n1. Рідко\n2. Час від часу\n3. Постійно"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=question)

    # Пункт 3: Зв'язатися з психологом компанії
    async def contact_psychologist(self, update, context):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Для зв'язку з психологом, перейдіть у приватний чат: @{self.psychologist_username}")

    def add_handlers(self):
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(MessageHandler(filters.TEXT & filters.Regex('Теоретичні відомості'), self.send_theoretical_info))
        self.application.add_handler(MessageHandler(filters.TEXT & filters.Regex('Тести'), self.send_test_question))
        self.application.add_handler(MessageHandler(filters.TEXT & filters.Regex('Зв\'язатися з психологом компанії'), self.contact_psychologist))

    def run(self):
        self.add_handlers()
        self.application.run_polling()

