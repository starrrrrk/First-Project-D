from pynput.keyboard import Key, Listener
from pygame import mixer, time
from gtts import gTTS
from webbrowser import open_new
mixer.init()

def action_alt():
    pass

def action():
    
    tts = gTTS(text='Выполняю', lang='ru')
    tts.save('data.mp3')

    mixer.music.load('data.mp3')
    mixer.music.play()

    open_new('https://www.google.com')

    while mixer.music.get_busy():
        time.Clock().tick(10)


def on_press(key):
    key = ("{0} pressed".format(key))
    print(key)
    if 'k' in key:
        action()



def on_release(key):
    key = ("{0} released".format(key))
    print(key)
    if 'k' in key:
        action_alt()

    if key==Key.esc:
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as f:
    f.join()


