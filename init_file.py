from aiogram import types

# t.me/my_uid_zero_bot - ссылка на бота

token = "7493419613:AAGfdf0HazDeXFWSjppyMZ5S5gfdXvEEvakmWmQ9F0"

##############################################################################################

# Установка кнопок "Начать диалог" и "Сбросить все диалоги"
def StartDialogBtn():
   start_dlg_btn = types.KeyboardButton(text="Начать диалог")
   reset_btn = types.KeyboardButton(text="Сбросить все диалоги")
   kb = [[start_dlg_btn],[reset_btn],] 
   return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

##############################################################################################

# Установка кнопок "Консультация" , "Запись на приём" , "Адрес клиники" - первый ряд кнопок
# Установка кнопки "Сбросить все диалоги" - второй ряд кнопок
def TooDialogBtn():
   cons_btn = types.KeyboardButton(text="Консультация")
   rec_audie_btn = types.KeyboardButton(text="Запись на приём")
   addr_btn = types.KeyboardButton(text="Адрес клиники")
   mode_work_btn = types.KeyboardButton(text="Режим работы")
   reset_btn = types.KeyboardButton(text="Сбросить все диалоги")
   kb = [[cons_btn,rec_audie_btn],[addr_btn,mode_work_btn],[reset_btn],] 
   return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

##############################################################################################

# Установка кнопок "Направления клиники" , "Цены" - первый ряд кнопок
# Установка кнопки "Сбросить все диалоги" - второй ряд кнопок
def ConsDialogBtn():
   direct_clinic_btn = types.KeyboardButton(text="Направления клиники")
   price_btn = types.KeyboardButton(text="Цены")
   reset_btn = types.KeyboardButton(text="Сбросить все диалоги")
   kb = [[direct_clinic_btn,price_btn],[reset_btn],] 
   return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

##############################################################################################

# Установка кнопок "Понедельник" , "Вторник", "Среда" - первый ряд кнопок
# Установка кнопок "Четверг" , "Пятница", - второй ряд кнопок
# Установка кнопки "Сбросить все диалоги" - третий ряд кнопок
def DaysWeekBtn():
   pon_btn = types.KeyboardButton(text="Понедельник")
   vtor_btn = types.KeyboardButton(text="Вторник")
   sre_btn = types.KeyboardButton(text="Среда")
   chet_btn = types.KeyboardButton(text="Четверг")
   pyat_btn = types.KeyboardButton(text="Пятница")
   reset_btn = types.KeyboardButton(text="Сбросить все диалоги")
   kb = [[pon_btn,vtor_btn,sre_btn],[chet_btn,pyat_btn],[reset_btn],] 
   return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

##############################################################################################

# Установка кнопок "9:00-11:00" , "11:30-13:00", "15:00-17:00" - первый ряд кнопок
def HoursBtn():
   hours1_btn = types.KeyboardButton(text="9:00-11:00")
   hours2_btn = types.KeyboardButton(text="11:30-13:00")
   hours3_btn = types.KeyboardButton(text="15:00-17:00")
   reset_btn = types.KeyboardButton(text="Сбросить все диалоги")
   kb = [[hours1_btn,hours2_btn,hours3_btn],[reset_btn],] 
   return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

