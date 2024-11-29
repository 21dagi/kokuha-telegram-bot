

from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from resources import resource
# Put your bot token here 
bot = Bot(token='7592419044:AAFt33gOBOKUlKbll0sboLxQeLYEjrxKvHs')  

# Initializing the dispatcher object 
dp = Dispatcher(bot) 
books = resource.books
helper_books = resource.helper_books
# Initial welcome keyboard with a "Welcome" button
welcome_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add("Welcome")

main_menu_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True, 
    one_time_keyboard=True,
    row_width=1,
    selective=True  # Ensures the keyboard is shown only to the selected user
)
main_menu_keyboard.add(
    KeyboardButton("መንፈሳዊ መጻሕፍት 📖"),
    KeyboardButton("አብነት-ዜማ 🎶"),
    KeyboardButton("A3"),
    KeyboardButton("A4"),
    KeyboardButton("Back")
)

# Define the A2 menu keyboard
a2_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
a2_menu_keyboard.add(KeyboardButton("ውዳሴ ማርያም ዜማ"))
a2_menu_keyboard.add(KeyboardButton("መዝሙረ ዳዊት ግዕዝ"))
a2_menu_keyboard.add(KeyboardButton("✿ቅዳሴ ✿"))
a2_menu_keyboard.add(KeyboardButton("ምንባብ ዘሰባቱ እለታት"))
a2_menu_keyboard.add(KeyboardButton("መልክአ "))
a2_menu_keyboard.add(KeyboardButton("መሀረነ አብ"))
a2_menu_keyboard.add(KeyboardButton("Back"))

qdase_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
qdase_menu_keyboard.add(KeyboardButton("ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)"))
qdase_menu_keyboard.add(KeyboardButton("ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)"))
qdase_menu_keyboard.add(KeyboardButton("Back"))


melk_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
melk_menu_keyboard.add(KeyboardButton("መልክአ ማርያም "))
melk_menu_keyboard.add(KeyboardButton("መልክአ ኢየሱስ"))
melk_menu_keyboard.add(KeyboardButton("መልክአ ፍልሰታ"))
melk_menu_keyboard.add(KeyboardButton("መልክአ ቁርባን"))
melk_menu_keyboard.add(KeyboardButton("መልክአ ስእል"))
melk_menu_keyboard.add(KeyboardButton("Back"))


# Sub-menu keyboard for A1 with buttons in a single column and a "Back" button
a1_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

a1_menu_keyboard.add(KeyboardButton("1 እስከ 12 ትምህርታዊ መጻሕፍት📖"))
a1_menu_keyboard.add(KeyboardButton("የኮርስ አጋዥ መጽሐፍት 📖"))
a1_menu_keyboard.add(KeyboardButton("ሌሎች መንፈሳዊ መጻሕፍት 📖"))
a1_menu_keyboard.add(KeyboardButton("Back to Main Menu"))


book_choice_inline = InlineKeyboardMarkup(row_width=1)
book_choice_inline.add(
    InlineKeyboardButton(text="Book 1", callback_data="book_1"),
    InlineKeyboardButton(text="Book 2", callback_data="book_2"),
    InlineKeyboardButton(text="Book 3", callback_data="book_3")
)

def create_book_choice_keyboard(row_width=1):
    keyboard = InlineKeyboardMarkup(row_width=row_width)
    for book in helper_books:
        keyboard.add(InlineKeyboardButton(text=book["name"], callback_data=book["callback"]))
    return keyboard
book_choice_inline = InlineKeyboardMarkup(row_width=3)
for i in range(0, len(books), 3):
    row = []
    for j in range(3):
        if i + j < len(books):
            book = books[i + j]
            row.append(InlineKeyboardButton(text=book["name"], callback_data=book["callback"]))
    book_choice_inline.add(*row)
    



@dp.message_handler(commands=['start', 'help']) 
async def welcome(message: types.Message): 
    welcome_text = (
        "*Welcome to the Student Resource Bot!* 🎉\n\n"
        "This bot helps students access resource files and recorded lessons from teachers easily.\n\n"
        "💡 *Features:*  \n"
        "- Access a variety of resource files 📚  \n"
        "- Listen to recorded lessons 🎧  \n"
        "- Enjoy a user-friendly experience designed just for you! 😊\n\n"
        "Feel free to explore and enjoy the resources we provide!  \n"
        "How can we assist you today?"
    )
    
    await bot.send_message(
        chat_id=message.chat.id,
        text=welcome_text,
        parse_mode='Markdown',  # Use 'HTML' if you prefer HTML formatting
        reply_markup=welcome_keyboard
    )

# Handling the "Welcome" button click to show the main menu
@dp.message_handler(lambda message: message.text == "Welcome")
async def show_main_menu(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Please choose an option:",
        reply_markup=main_menu_keyboard
    )
# Handling main menu options A1, A2, A3, and A4
# Handling the main menu buttons
@dp.message_handler(lambda message: message.text in ["መንፈሳዊ መጻሕፍት 📖", "አብነት-ዜማ 🎶", "A3", "A4", "Back"])
async def handle_main_menu(message: types.Message):
    if message.text == "መንፈሳዊ መጻሕፍት 📖":
        # Show submenu for A1
        await bot.send_message(message.chat.id, "You chose A1. Please select an option:", reply_markup=a1_menu_keyboard)
        
    elif message.text == "አብነት-ዜማ 🎶":
        await message.answer(
            text="You clicked አብነት-ዜማ 🎶! Here are the options you can choose from:",
            reply_markup=a2_menu_keyboard
    )
    elif message.text == "A3":
        # Sending 3 files for A3
        await bot.send_message(message.chat.id, "You selected A3. Sending files...", reply_markup=main_menu_keyboard)
        file_ids_a3 = [
            'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA',
            'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA',
            'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'
        ]
        # Send each file
        for file_id in file_ids_a3:
            await bot.send_document(message.chat.id, file_id)

    elif message.text == "Back":
        # Go back to the main menu
        await bot.send_message(message.chat.id, "Returning to the main menu.", reply_markup=main_menu_keyboard)
        
    else:
        # Placeholder response for A4
        await bot.send_message(message.chat.id, "You selected A4. This feature is under development.", reply_markup=main_menu_keyboard)

@dp.message_handler(lambda message: message.text in ["1 እስከ 12 ትምህርታዊ መጻሕፍት📖", "የኮርስ አጋዥ መጽሐፍት 📖", "ሌሎች መንፈሳዊ መጻሕፍት 📖", "Back to Main Menu"])
async def handle_a1_menu(message: types.Message):
    if message.text == "1 እስከ 12 ትምህርታዊ መጻሕፍት📖":
        await bot.send_message(
            message.chat.id,
            "You clicked 1 እስከ 12 ትምህርታዊ መጻሕፍት📖! Choose a book below:",
            reply_markup=book_choice_inline
        )
    elif message.text == "የኮርስ አጋዥ መጽሐፍት 📖":
     	await bot.send_message(
            message.chat.id,
            "You clicked የኮርስ አጋዥ መጽሐፍት 📖! Here are the available resources:",
            reply_markup=create_book_choice_keyboard()  # Show the book choices
        )



    elif message.text == "ሌሎች መንፈሳዊ መጻሕፍት 📖":
        await bot.send_message(
            message.chat.id,
            "Sending files...",
            reply_markup=a1_menu_keyboard
        )
        file_ids_send_file = [
            'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA',
            'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA',
            'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'
        ]
        for file_id in file_ids_send_file:
            await bot.send_document(message.chat.id, file_id)

    elif message.text == "Back to Main Menu":
        await bot.send_message(
            message.chat.id,
            
            reply_markup=main_menu_keyboard
        )
qdase_audios = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'}
]

qdase_audios2 = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'}
]
melk_audios = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'}
]

melk_audios2 = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'}
]
melk_audios3 = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'}
]
melk_audios4 = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'}
]



wdase_audios = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "callback": "audio_1", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "callback": "audio_2", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 3", "callback": "audio_3", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 4", "callback": "audio_4", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 5", "callback": "audio_5", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 6", "callback": "audio_6", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 7", "callback": "audio_7", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'}
]
dawit = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "callback": "audio_1", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "callback": "audio_2", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 3", "callback": "audio_3", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 4", "callback": "audio_4", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 5", "callback": "audio_5", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 6", "callback": "audio_6", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 7", "callback": "audio_7", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'}
]
mnbab_7tulet = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "callback": "audio_1", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "callback": "audio_2", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 3", "callback": "audio_3", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 4", "callback": "audio_4", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 5", "callback": "audio_5", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 6", "callback": "audio_6", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "Audio 7", "callback": "audio_7", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'}
]
mehareneab = [
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "callback": "audio_1", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
    {"name": "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "callback": "audio_2", "file_id": 'BQACAgQAAxkBAAMZZxkYGzRW4539VvBVa8bylYa3MwUAAq0TAAKxtslQRvjuKNOmn9s2BA'},
]
@dp.message_handler(lambda message: message.text == "መልክአ")
async def handle_melka(message: types.Message):
    await message.answer(
        text="You clicked መልክአ! Here are the options you can choose from:",
        reply_markup=melk_menu_keyboard
    )
@dp.message_handler(lambda message: message.text in ["ውዳሴ ማርያም ዜማ", "መዝሙረ ዳዊት ግዕዝ","✿ቅዳሴ ✿","ምንባብ ዘሰባቱ እለታት","መልክአ ","መሀረነ አብ","Button 7",])
async def handle_a1_menu(message: types.Message):
    if message.text == "ውዳሴ ማርያም ዜማ":
         for audio in wdase_audios:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is {audio['name']}."
            )
    elif message.text == "መዝሙረ ዳዊት ግዕዝ":
     	 for audio in dawit:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is dawit {audio['name']}."
            )
    elif message.text == "✿ቅዳሴ ✿":
     	   await message.answer(
            text="You clicked ✿ቅዳሴ ✿! Here are the options you can choose from:",
            reply_markup=qdase_menu_keyboard
    )
    elif message.text == "ምንባብ ዘሰባቱ እለታት":
     	 for audio in mnbab_7tuelet:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is dawit {audio['name']}."
            )
    
    elif message.text == "መሀረነ አብ":
     	 for audio in mehareneab:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is dawit {audio['name']}."
            )
    elif message.text == "Button 7":
     	 for audio in dawit:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is dawit {audio['name']}."
            )
    elif message.text == "Back":
        await bot.send_message(
            message.chat.id,
    
            reply_markup=main_menu_keyboard
        )
#kdase choice
@dp.message_handler(lambda message: message.text in ["ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)", "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)", "Back"])
async def send_qdase_audios(message: types.Message):
    if message.text == "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(እዝል)":
        for audio in qdase_audios:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is A1{audio['name']}."
            )
    elif message.text == "ቅዳሴ ዘደብረ ዓባይ በጣዕመ ዜማ(ግዕዝ)":
        for audio in qdase_audios2:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is A2 {audio['name']}."
            )
    elif message.text == "Back":
        await bot.send_message(
            message.chat.id,
            reply_markup=a2_menu_keyboard
        )
#melk choices
@dp.message_handler(lambda message: message.text in ["መልክአ ማርያም ", "መልክአ ኢየሱስ","መልክአ ፍልሰታ", "መልክአ ቁርባን", "መልክአ ስእል", "Back"])
async def send_melk_audios(message: types.Message):
    if message.text == "መልክአ ማርያም ":
        for audio in melk_audios:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is melk1{audio['name']}."
            )
    elif message.text == "መልክአ ኢየሱስ":
        for audio in melk_audios2:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is melk2{audio['name']}."
            )
    elif message.text == "መልክአ ፍልሰታ":
        for audio in melk_audios3:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is melk{audio['name']}."
            )
    elif message.text == "መልክአ ቁርባን":
        for audio in melk_audios4:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is melk{audio['name']}."
            )
    elif message.text == "መልክአ ስእል":
        for audio in melk_audios4:
            await bot.send_document(
                chat_id=message.chat.id,
                document=audio["file_id"],
                caption=f"Here is melk{audio['name']}."
            )
    elif message.text == "Back":
        await bot.send_message(
            message.chat.id,
            "Returning to the main menu.",
            reply_markup=a2_menu_keyboard
        )


@dp.callback_query_handler(lambda callback_query: callback_query.data in [book["callback"] for book in books])
async def handle_book_selection(callback_query: types.CallbackQuery):
    # Find the selected book by callback data
    selected_book = next(book for book in books if book["callback"] == callback_query.data)

    # Send the corresponding file without a reply icon
    await bot.send_document(
        chat_id=callback_query.message.chat.id,
        document=selected_book["file_id"],
        caption=f"Here is {selected_book['name']}."
    )
# Handling the "የኮርስ አጋዥ መጽሐፍት 📖" button click

@dp.message_handler(lambda message: message.text == "የኮርስ አጋዥ መጽሐፍት 📖")
async def send_course_guides(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="You clicked የኮርስ አጋዥ መጽሐፍት 📖! Here are the books you can choose from:",
        reply_markup=create_book_choice_keyboard(row_width=3)  # Show the books in 3 columns
    )

# Handling book selections
@dp.callback_query_handler(lambda callback_query: callback_query.data in [book["callback"] for book in helper_books])
async def handle_book_selection(callback_query: types.CallbackQuery):
    # Find the selected book by callback data
    selected_book = next(book for book in helper_books if book["callback"] == callback_query.data)

    # Send the corresponding file without a reply icon
    await bot.send_document(
        chat_id=callback_query.message.chat.id,
        document=selected_book["file_id"],
        caption=f"Here is {selected_book['name']}.",
        reply_markup=create_book_choice_keyboard()  # Default to single column for this case
    )
    # Acknowledge the callback to dismiss loading animation in the Telegram app
    await callback_query.answer()
# Starting the bot 
if __name__ == '__main__':
    executor.start_polling(dp)

           
      
