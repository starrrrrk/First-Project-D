import speech_recognition as sr
from os import system
from time import sleep
from pynput.keyboard import Key, Listener
from webbrowser import open_new


def action():
    while True:
        #open_new("https://www.google.com")
        print('I am in action')
        r = sr.Recognizer()
        m = sr.Microphone()
        #system('clear')
        with m as source:
            r.adjust_for_ambient_noise(source)
        with m as source:
            audio = r.listen(source)
   
        try:
            statement = r.recognize_google(audio, language='ru-RU')

        #except:
        #    statement = r.recognize_google(audio, language='eng-ENG')
    
        except sr.UnknownValueError:
            print("ошибка - РЫБКА")
            
        try:
            print("Вы сказали: {}".format(statement))
            open_new('https://yandex.ru/yandsearch?text=' + statement)
        except:
            print("Не могу вывести текст")

        with Listener(on_press=on_press,on_release=on_release) as f:

            f.join()
    
def action_alt():
    print("I am in action_alt")
    pass


def on_press(key):
    print('i am in on_press')
    key_prnt = "{0} pressed".format(key)
    print(key_prnt)

    if 'Key.ctrl' in key_prnt:# and 'key.ctrl.r' in key:
        print('going to action')
        action()


def on_release(key):
    key_prnt = "{0} released".format(key)
    print(key_prnt)
    if 'Key.ctrl' in key_prnt: #and "Key.ctrl.r" in key:
        #sleep(10)
        print('released going to pass')
        action_alt()

    else:
        pass


#action()
with Listener (
        on_press = on_press,
        on_release = on_release) as f:
    f.join()
