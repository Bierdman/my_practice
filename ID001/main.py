from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import random

from keyboards import kb, ikb

TOKEN_API_MY_PRACTICE_PY = '6189562382:AAFwWtmIgEFQUbaUTGdDD2FCNXJ3vvH3jXk'

bot = Bot(TOKEN_API_MY_PRACTICE_PY)
dp = Dispatcher(bot)


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>запуск бота</em>
<b>/description</b> - <em>описание бота</em>"""

arr_photos = ["https://img.fonwall.ru/o/aa/mr-freeman-mister-frimen-personazh-solnce.jpg",
              "https://coub-attachments.akamaized.net/coub_storage/coub/simple/cw_image/fd18d3a6f73/da1f1ba71159eb6da81ff/1499003203_00031.jpg",
              "https://i.ytimg.com/vi/43R4XZQoFrQ/maxresdefault.jpg"
]

photos = dict(zip(arr_photos, ['Cheel', 'Smoke', 'Meditation']))
random_photo = random.choice(list(photos.keys()))


flag = False

async def on_startup(_):
    print('practice/ID001')


async def send_random(message: types.Message):
    global random_photo
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb)



@dp.message_handler(Text(equals='Random photo'))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Рандомная фотка!',
                         reply_markup=ReplyKeyboardRemove())
    await send_random(message)
    await message.delete()


@dp.message_handler(Text(equals='Главное меню'))
async def open_kb(message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню',
                         reply_markup=kb)
    await message.delete()



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Добро пожаловать в наш бот!🐝',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         reply_markup=kb,
                         parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def cmd_description(message: types.Message):
    await message.answer(text='Наш бот умеет отправлять рандомные фотки',
                         reply_markup=kb)
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEIjG1kNbR1N-Xcj5evRPAsHA9iMumUagACBAoAArdsSUsLIHjZYlA6US8E')
    await message.delete()


@dp.message_handler(commands=['location'])
async def cmd_location(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=random.randint(0, 50),
                            longitude=random.randint(0, 50))


@dp.callback_query_handler()
async def callback_random_photo(callback: types.CallbackQuery):
    global random_photo # ! Нежелательно использование глобальных переменных внутри функций
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer('Вам понравилось!')
            flag = not flag
        else:
            await callback.answer('Вы уже лайкнули!')
        #await callback.message.answer('Вам понравилось')
    elif callback.data == 'dislike':
        await callback.answer('Вам не понравилось')
        #await callback.message.answer('Вам не понравилось')
    elif callback.data == 'main':
        await callback.message.answer(text='Добро пожаловать в главное мнею',
                                      reply_markup=kb)
        await callback.message.delete()
        await callback.answer()
    else:
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           types='photo',
                                                           caption=photos[random_photo]),
                                                           reply_markup=ikb)
        #await send_random(message=callback.message)
        await callback.answer()


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
