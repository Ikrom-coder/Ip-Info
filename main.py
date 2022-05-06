import logging
import requests
import folium
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1392689751:AAFs0SYgBRn0f3kAZO_27-yBvGaNEjdx7_c'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
my_ip_public = requests.get('https://api.ipify.org').text


def ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        map_of_ip = folium.Map(location=[response.get('lat'), response.get('lon')])
        map_of_ip.save(f'location_of_{response.get("query")}.html')
        return response, map_of_ip

    except requests.exceptions.ConnectionError:
        return "Please, check your connection!"


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Hello <b>{message.from_user.first_name},</b>\nYour IP: {my_ip_public}\nsend me IP-address", parse_mode='HTML')


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("This is Info bot that gives information by IP-address.\nSend IP then take Info")


@dp.message_handler()
async def echo(message: types.Message):
    id_num = message.from_user.id
    data = []
    ip_num = message.text
    response, map_ip = ip_info(ip_num)
    for k, v in response.items():
        data.append(f'{k.capitalize()} -> {v}')
    info = '\n'.join(str(e) for e in data)
    await message.answer(f'<b>{info}</b>', parse_mode='HTML')
    with open(f'location_of_{response.get("query")}.html', 'rb') as location:
        await message.reply_document(location, caption='location of the IP')
    await message.reply_location(response.get('lat'), response.get('lon'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
