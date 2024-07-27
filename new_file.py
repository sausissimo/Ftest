# Пример декоратора: 
# функции, которая принимает другие функции и меняет их функционал

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    print(func("Кричу или шепчу?"))

greet(whisper)
greet(shout)