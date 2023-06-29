import os
import time
import argostranslate.package
import argostranslate.translate
import atlas_settings

from_code = atlas_settings.transcript_lang
to_code = atlas_settings.translation_lang
dir_path = atlas_settings.transcripts_directory

if(atlas_settings.whisper_task_settings == "translate"):
    print('Transcriber window will show whisper translations. You can close this window')



print('looping..')
while True:
    all_files = os.listdir(dir_path)
    if not all_files:
        time.sleep(1)
        
    else:
        files = [f for f in all_files if os.path.isfile(os.path.join(dir_path, f))]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))
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
        os.remove(dir_path + oldest_file)