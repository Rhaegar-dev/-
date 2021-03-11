'''
Реализуйте планировщик задач, который принимает на вход функцию f и целое число n 
и вызывает функцию f через n миллисекунд.
'''
import time

def hello():
    print('hello')

def task_manager(f, n):
    delay = n/1000
    time.sleep(delay)
    f()

task_manager(hello, 1000)
