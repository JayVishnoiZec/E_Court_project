from captcha.audio import AudioCaptcha

audio = AudioCaptcha()

text_captcha = '3456'

audio_captcha = audio.generate(text_captcha)

audio.write(text_captcha , 'Audio.wav')