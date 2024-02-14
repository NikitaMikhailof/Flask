import threading 
import os
import time

'''Задание №4 Создать программу, которая будет производить подсчет 
количества слов в каждом файле в указанной директории и 
выводить результаты в консоль. Используйте потоки.'''


def worker(filename):
    with open(f'Flask/seminar_4/folder_1/{filename}', 'r', encoding='utf-8') as f:
        res = f.read()
        count = len(res.split())
        return f'В файле {filename} : {count} слов'

def files_folder():
    for address, dirs, files in os.walk('Flask/seminar_4/folder_1'):
        return files    
    
if __name__ == '__main__':
    start_time = time.time()
    threads = []
    for files in files_folder():
        thread = threading.Thread(target=worker, args=(files, ))
        threads.append(thread)
        thread.start()
        start_time = time.time()
    for t in threads:
        t.join()
    print(time.time() - start_time)    
    



