from random import randint
import time
import threading 
import multiprocessing 
import asyncio

'''Задание №7 Напишите программу на Python, которая будет находить 
сумму элементов массива из 1000000 целых чисел. Пример массива: 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...].  Массив должен быть заполнен
случайными целыми числами от 1 до 100. При решении задачи нужно использовать
многопоточность, многопроцессорность и асинхронность. В каждом решении нужно
вывести время выполнения вычислений.'''

arr = [randint(1, 100) for i in range(10**6)]


'''синхронный подход'''

def incrimenet(arr):
    arr = [randint(1, 100) for i in range(10**6)]
    sum_elem_arr = 0
    start_time = time.time()
    for ar in arr:
        sum_elem_arr += ar 
    print(sum_elem_arr, (time.time() - start_time), sep ='\n')

'''многопоточный подход'''

def worker_thread(low, high):
    global counter
    for num in arr[low:high + 1]:
        counter += num

counter = 0

def incrimenet_thread(arr):
    low, high = 0, 10**4
    threads = []
    for _ in range(100):
        thread = threading.Thread(target=worker_thread, args=(low, high, )) 
        low += 10**4
        high += 10**4
        threads.append(thread)
        start_time = time.time()
        thread.start()
    for t in threads:
        t.join()        
    print(counter, time.time() - start_time, sep='\n')

'''многопроцессорный подход'''

def worker_process(low, high):
    counter = 0
    for num in arr[low:high + 1]:
        counter += num 
    return counter    

def incrimenet_process(arr):
    low, high = 0, 10**4
    processes = [] 
    count = 0
    for _ in range(100):
        process = multiprocessing.Process(target=worker_process, args=(low, high, )) 
        low += 10**4
        high += 10**4
        count += worker_process(low, high) 
        processes.append(process)
        start_time = time.time()
        process.start()
    for process in processes:
        process.join()    
    print(count, time.time() - start_time, sep='\n')

'''асинхронный подход'''

arr = [randint(1, 100) for i in range(10**6)]

async def worker_async(low, high):
    global counter
    for num in arr[low:high + 1]:
        counter += num 
    return counter    

async def incrimenet_async(arr):
    low, high = 0, 10**4
    for _ in range(100):
        start_time = time.time()
        counter = await worker_async(low, high)
        low += 10**4
        high += 10**4
    print(counter, time.time() - start_time, sep='\n')

if __name__ == '__main__':
    incrimenet_thread(arr)
    incrimenet_process(arr)
    asyncio.run(incrimenet_async(arr))

