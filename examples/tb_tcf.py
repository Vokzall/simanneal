
import threading

# Функция 1
def function1():
    print("Function 1 is running")

# Функция 2
def function2():
    print("Function 2 is running")

# Создание и запуск потока для функции 1
thread1 = threading.Thread(target=function1)
thread1.start()

# Создание и запуск потока для функции 2
thread2 = threading.Thread(target=function2)
thread2.start()

# Ожидание завершения потоков
thread1.join()
thread2.join()

print("Both functions have finished running")