from gtts import gTTS
from playsound import playsound
import os

#경로를 .py 실행경로로 이동, 현재경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

text= '안녕하세요 파이썬과 40개의 작품들 입니다.'

tts= gTTS(text=text, lang='ko')
tts.save("hi3.mp3")

playsound("hi3.mp3")