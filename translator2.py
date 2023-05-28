import os
import time
#argotranslate is also a very cool project. Offline translation > sending api requests to google
import argostranslate.package
import argostranslate.translate

from_code = "ja"#language of the transcripts
to_code = "en"#language you want transcripts to be
dir_path = ''#where transcripts are | set the same in transcriber

print('looping..')
while True:
    all_files = os.listdir(dir_path)
    if not all_files:
        #   print('Dir empty...')
        time.sleep(1) #sleep 1 sec.
        
    else:
        # list out
        files = [f for f in all_files if os.path.isfile(os.path.join(dir_path, f))]

        # sort the list by modified time in ascending order
        files.sort(key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))

        # get the oldest file
        oldest_file = files[0]

        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next(
            filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            )
        )
        argostranslate.package.install_from_path(package_to_install.download())

        # Translate
        with open(dir_path + oldest_file, 'r', encoding='utf-8') as f:
            text_to_translate = f.read()

        translatedText = argostranslate.translate.translate(text_to_translate, from_code, to_code)
        print(translatedText)
        os.remove(dir_path + oldest_file) #remove translated transcripts