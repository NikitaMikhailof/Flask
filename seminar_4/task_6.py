import asyncio 
import os
import time

'''Задание №6 Создать программу, которая будет производить подсчет 
количества слов в каждом файле в указанной директории и 
выводить результаты в консоль. Используйте асинхронный подход.'''

async def worker(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        count_words = len(text.split())
    return count_words

async def get_file_from_directory(directory):
    for address, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(address, file)   
            await worker(file_path)
            

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(get_file_from_directory('/folder1'))
    print(time.time() - start_time)


    