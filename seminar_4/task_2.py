import multiprocessing
import time 
import requests

'''Задание №2  Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого 
адреса. После загрузки данных нужно записать их в отдельные 
файлы. Используйте процессы.'''

urls = ['https://accounts.google.com/SignUpWithoutGmail',
       'https://www.google.com/takeout',
       'https://support.google.com/legal',
       'https://maps.google.com/locationhistory',
       'https://history.google.com/history/audio',
       'https://www.google.com/settings/account/inactive',
       'https://security.google.com/settings/security/activity',
       'https://security.google.com/settings/security/permissions',
       ]

def download(url):
    response = requests.get(url)
    filename = f'threading_{url.replace('/', '').replace(':', '').replace(':', '')}.html'
    with open(f'Flask/seminar_4/folder/{filename}', 'w', encoding='utf-8') as file:
        file.write(response.text) 

if __name__ == '__main__':
    processes = []
    start_time = time.time()
    for url in urls:
        p = multiprocessing.Process(target=download, args=(url,))
        processes.append(p)
        p.start()
        for p in processes:
            p.join() 
    print(time.time() - start_time)        

