from gtts import gTTS

tts_en = gTTS('hello', lang='en')

tts_fr = gTTS('bonjour', lang='fr')


with open('.\DevMan\hello_bonjour.mp3', 'wb') as f:

    tts_en.write_to_fp(f)

    tts_fr.write_to_fp(f)
# ------------------------------
tts = gTTS('hello')
tts.save('.\DevMan\hello.mp3')
