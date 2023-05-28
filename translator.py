import os
import time
from deep_translator import (GoogleTranslator, MyMemoryTranslator, QcriTranslator, single_detection)

dir_path = '' #where transcripts are | set the same in transcriber

apiDetection = '' #api key for detection - rarely used it
apiQCRI = '' #api key for QCRI

targetLang = 'en'#language you want transcripts to be
lang = 'ja'#language of the transcripts


print('looping..')
while True:
    all_files = os.listdir(dir_path)
    if not all_files:
        print('Dir empty...')
        time.sleep(1) #sleep 1 sec.
    else:
        # list out
        files = [f for f in all_files if os.path.isfile(os.path.join(dir_path, f))]

        # sort the list by modified time in ascending order
        files.sort(key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))

        # get the oldest file
        oldest_file = files[0]
        #print(oldest_file)


        #print(lang)


        #GoogleTranslator
        translator = GoogleTranslator(source=lang, target=targetLang)
        translated_text = translator.translate_file(dir_path + oldest_file)

        # Display the translated text
        print(translated_text)
        time.sleep(5)

        #different translator parts - google one works fine. The biggest issue is quality of the transcripts
        
        #translatorMyMemory = MyMemoryTranslator(source=lang, target=targetLang).translate_file(dir_path+oldest_file)
        #print(MyMemoryTranslator)
        #translatorQCRI = QcriTranslator(apiQCRI).translate(source=lang, target=targetLang, domain="news", text=dir_path+oldest_file)
