from threading import Thread
import time

list_of_somethings = []


def thread_put_in_list_num_from_input():
    while True:
        print('я - поток 1')
        print('Введите что-то:')
        n = input()
        global list_of_somethings
        if len(list_of_somethings) == 0:
            list_of_somethings = [n]
        else:
            list_of_somethings.append(n)


def thread_sleeper_printer():
    global list_of_somethings
    while True:
        print('я - поток 2')
        time.sleep(3)
        print(list_of_somethings[0])
        del list_of_somethings[0]


th1 = Thread(target=thread_put_in_list_num_from_input())
th2 = Thread(target=thread_sleeper_printer())

th1.start()
th2.start()
