#variant no 4

# Task3
# async await
# Имитируем чатик с тролем
# Вы в консоли пишете какие-то сообщения - это одна асинк функция
# Вторая - это троль, который асинхронно пишет вам что-то типа
# "Хаха, затролено", "Олололо", ещё сами придумайте штуки 3-4 ответа
# Иногда он приводит вам ваши же цитаты (выбирая случайно), то есть ваши
# сообщения надо запоминать
# "'Привет, как дела?' АХАХАХАХАЗАЗАЗАЗЗ, КАК ЖЕ ТЫ ГОРИШЬ"
#
import asyncio
from random import choice
import aioconsole

list_of_inputs = ["Хаха, затролено", 'чуваааааааааааааааак, ну ты ваще.....', "Олололо", 'покеда, товарищ......']


async def input_async():
    while True:
        inp = await aioconsole.ainput()
        list_of_inputs.append(inp)
        await asyncio.sleep(0.3)


async def output_async():
    while True:
        msg_for_now = choice(list_of_inputs)
        print(msg_for_now)
        await asyncio.sleep(5)


async def main():
    await asyncio.gather(input_async(), output_async())

asyncio.run(main())
