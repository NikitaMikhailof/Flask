'''Задание №3 Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого 
адреса. После загрузки данных нужно записать их в отдельные 
файлы. Используйте асинхронный подход.'''

import asyncio
import aiohttp
import time


urls = ['https://www.google.ru/',
'https://gb.ru/',
'https://ya.ru/',
'https://www.python.org/',
'https://habr.com/ru/all/',
]

async def download(url):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = f'asynco_{url.replace('/', '').replace(':', '').replace(':', '')}.html'
            with open(f'Flask/seminar_4/folder_1/{filename}', 'w', encoding='utf-8') as f:
                f.write(text)

    
async def main():
      tasks = []
      for url in urls:
          task = asyncio.ensure_future(download(url))
          tasks.append(task)
      await asyncio.gather(*tasks)       

if __name__ == '__main__':
    start_time = time.time()
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(main())   
    asyncio.run(main()) 
    print(time.time() - start_time)

