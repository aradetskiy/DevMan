from transliterate import translit
from num2words import num2words
from gtts import gTTS
from playsound import playsound

my_text = ''' \
Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.

More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...
'''
trans_text = translit(my_text, 'ru')
print(trans_text)

my_counts = [78, 15, 3, 40, 8]
for i in my_counts:
    print(i, translit(num2words(i), language_code='ru'), sep=' - ')

tts_en = gTTS(my_text)
tts_en.save('.\DevMan\les2_speach_en.mp3')
playsound('.\DevMan\les2_speach_en.mp3')

tts_ru = gTTS(my_text, lang='ru')
tts_ru.save('.\DevMan\les2_speach_ru.mp3')
playsound('.\DevMan\les2_speach_ru.mp3')
