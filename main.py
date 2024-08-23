import logging
import asyncio
import init_file
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types import FSInputFile

#######################################################################################################    

# Вставьте сюда токен вашего бота
API_TOKEN = init_file.token

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

#######################################################################################################    

#=== Обработчик команды "/start" ===#
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    # Отправка изображения в чат
    photo = FSInputFile('med_bot_no_fon.png')  # Путь к изображению
    await message.answer_photo(photo)
    # Отправка текста в чат
    await message.answer("Здраствуйте! Я бот - консультант.")
    await message.answer("Я представляю Международную академическую клинику.")
    await message.answer("Сайт клиники : http://project10249217.tilda.ws")
    
    # Установка кнопок
    keyboard = init_file.StartDialogBtn()
    await message.answer("Чем могу помочь?",reply_markup=keyboard)

#######################################################################################################        

#=== Обработчик нажатия кнопки "Начать диалог" ===#
@dp.message(F.text.lower() == "начать диалог")
async def start_dialog(message: types.Message):
    keyboard = init_file.TooDialogBtn()
    await message.answer("Какой у Вас вопрос?",reply_markup=keyboard)

#######################################################################################################        

#=== Обработчик нажатия кнопки "адрес клиники" ===#
@dp.message(F.text.lower() == "адрес клиники")    
async def addr_clin(message: types.Message):
    await message.answer("Адрес клиники :")
    await message.answer("г. Москва")
    await message.answer("ул. Автозаводская д. 16 к. 2.")
    await message.answer("метро Автозаводская")

#######################################################################################################        

#=== Обработчик нажатия кнопки "адрес клиники" ===#
@dp.message(F.text.lower() == "режим работы")    
async def addr_clin(message: types.Message):
    await message.answer("Поликлиника: 08:00-21:00")
    await message.answer("Стационар: Круглосуточно")

#######################################################################################################        

#=== Обработчик нажатия кнопки "Направления клиники" ===#
@dp.message(F.text.lower() == "направления клиники")    
async def direct_clin(message: types.Message):
    await message.answer("Онкология.")
    await message.answer("Кардиология.")
    await message.answer("Неврология и неврохирургия.")
    await message.answer("Ортопедия и травмотология.")
    await message.answer("Гинекология и репродуктивное здоровье.")
    await message.answer("Педиатрия.")
    await message.answer("Эндокринология.")
    await message.answer("Пластическая и эстетическая хирургия.")
    await message.answer("Инфекционные болезни.")
    await message.answer("Психиатрия и психотерапия.")

#######################################################################################################        

#=== Обработчик нажатия кнопки "Запись на приём" ===#
@dp.message(F.text.lower() == "запись на приём")    
async def direct_clin(message: types.Message):
    keyboard = init_file.DaysWeekBtn()
    await message.answer("Выберите день недели",reply_markup=keyboard)

#=== Обработчик нажатия кнопки "Понедельник" ===#
@dp.message(F.text.lower() == "понедельник")    
async def days_rec_pon(message: types.Message):
    global day_rec
    day_rec = "понедельник"
    keyboard = init_file.HoursBtn()    
    await message.answer("Выберите время",reply_markup=keyboard)

#=== Обработчик нажатия кнопки "Вторник" ===#
@dp.message(F.text.lower() == "вторник")    
async def days_rec_vtor(message: types.Message):
    global day_rec
    day_rec = "вторник"
    keyboard = init_file.HoursBtn()    
    await message.answer("Выберите время",reply_markup=keyboard)

#=== Обработчик нажатия кнопки "Среда" ===#
@dp.message(F.text.lower() == "среда")    
async def days_rec_sre(message: types.Message):
    global day_rec
    day_rec = "среда"
    keyboard = init_file.HoursBtn()    
    await message.answer("Выберите время",reply_markup=keyboard)

#=== Обработчик нажатия кнопки "Четверг" ===#
@dp.message(F.text.lower() == "четверг")    
async def days_rec_chet(message: types.Message):
    global day_rec
    day_rec = "четверг"
    keyboard = init_file.HoursBtn()    
    await message.answer("Выберите время",reply_markup=keyboard)    

#=== Обработчик нажатия кнопки "Пятница" ===#
@dp.message(F.text.lower() == "пятница")    
async def days_rec_pyat(message: types.Message):
    global day_rec
    day_rec = "пятница"
    keyboard = init_file.HoursBtn()    
    await message.answer("Выберите время",reply_markup=keyboard)    

#=== Обработчик нажатия кнопки "9:00-11:00" ===#
@dp.message(F.text.lower() == "9:00-11:00")    
async def days_rec_pyat(message: types.Message):
    keyboard = init_file.HoursBtn()  
    s = f"Вы записаны на приём: {day_rec} с 9:00-11:00"  
    await message.answer(s,reply_markup=keyboard) 

    keyboard = init_file.StartDialogBtn()
    await message.answer("Чем могу ещё помочь?",reply_markup=keyboard)   

#=== Обработчик нажатия кнопки "11:30-13:00" ===#
@dp.message(F.text.lower() == "11:30-13:00")    
async def days_rec_pyat(message: types.Message):
    keyboard = init_file.HoursBtn()  
    s = f"Вы записаны на приём: {day_rec} с 11:30-13:00"  
    await message.answer(s,reply_markup=keyboard) 

    keyboard = init_file.StartDialogBtn()
    await message.answer("Чем могу ещё помочь?",reply_markup=keyboard)   

#=== Обработчик нажатия кнопки "15:00-17:00" ===#
@dp.message(F.text.lower() == "15:00-17:00")    
async def days_rec_pyat(message: types.Message):
    keyboard = init_file.HoursBtn()  
    s = f"Вы записаны на приём: {day_rec} с 11:30-13:00"  
    await message.answer(s,reply_markup=keyboard) 

    keyboard = init_file.StartDialogBtn()
    await message.answer("Чем могу ещё помочь?",reply_markup=keyboard)   

#######################################################################################################        

#=== Обработчик нажатия кнопки "Цены" ===#
@dp.message(F.text.lower() == "цены")    
async def price(message: types.Message):
    # Отправка файла в чат
    prc_fl = FSInputFile('price.pdf')  # Путь к изображению
    await message.answer_document(prc_fl)
    
#######################################################################################################    

#=== Обработчик нажатия кнопки "Сбросить все диалоги" ===#
@dp.message(F.text.lower() == "сбросить все диалоги")
async def reset_dialog(message: types.Message):
    await message.answer("Все диалоги сброшены.")
    # Отправка изображения в чат
    photo = FSInputFile('med_bot_no_fon.png')  # Путь к изображению
    await message.answer_photo(photo)
    
    await message.answer("Здраствуйте! Я бот - консультант.")
    await message.answer("Я представляю Международную академическую клинику.")
    await message.answer("Сайт клиники : http://project10249217.tilda.ws")
    # Установка кнопок
    keyboard = init_file.StartDialogBtn()
    await message.answer("Чем могу помочь?",reply_markup=keyboard)

#######################################################################################################    

#=== Обработчик нажатия кнопки "Консультация" ===#
@dp.message(F.text.lower() == "консультация")
async def cons_dialog(message: types.Message):
    keyboard = init_file.ConsDialogBtn()    
    await message.answer("Выберите интересующую вас тему.",reply_markup=keyboard)

#######################################################################################################    

#=== Обработчик всех остальных сообщений ===#
@dp.message()
async def echo_message(message: types.Message):
    # Отправка изображения бота в чат 
    photo = FSInputFile('med_bot_no_fon.png')  # Путь к изображению
    await message.answer_photo(photo)
    # Отправка текста в чат
    await message.answer("Что-то не совсем Вас понимаю - лучше нажмите соответствующую кнопку.😊")

#######################################################################################################

async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())