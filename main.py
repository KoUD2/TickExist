from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = Bot('Your_token')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

user_states = {}
marathon_answers = {}


async def on_startup(_):
    print('Бот запущен')


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(
        'Привет! \nЯ бот Отмечалка. Я помогу Вам отметить посещаемость на любой паре. Дайте мне только доступ к комментариям под постами в Вашей группе в телеграмм')


people_status = {
    "Аполонник": "❌",
    "Артеменко": "❌",
    "Боисов": "❌",
    "Гагкуев": "❌",
    "Галиева": "❌",
    "Глушкова": "❌",
    "Гомзякова": "❌",
    "Давыдович": "❌",
    "Деревянкина": "❌",
    "Ефимова": "❌",
    "Иманалиева": "❌",
    "Климова": "❌",
    "Коршунова": "❌",
    "Логинова": "❌",
    "Мартиновс": "❌",
    "Морозова": "❌",
    "Муракаева": "❌",
    "Мурашкевич": "❌",
    "Ордаш": "❌",
    "Орехова": "❌",
    "Парникова": "❌",
    "Суперека": "❌",
    "Турицына": "❌",
    "Удод": "❌",
    "Чекалин": "❌",
}



@dp.message_handler(commands=['otmetite'])
async def send_final_list(message: types.Message):
    final_list = '\n'.join([f'{key}: {value}' for key, value in people_status.items()])
    await bot.send_message(message.chat.id, final_list)

@dp.message_handler()
async def process_name(message: types.Message):
    names = message.text.replace(',', ' ').split()
    for name_raw in names:
        name = name_raw.capitalize()
        if name in people_status:
            people_status[name] = "✅"
    final_list = '\n'.join([f'{key}: {value}' for key, value in people_status.items()])






if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
