import os
import datetime
import time

### settings

# where to save recordings
recordings_directory = './recordings/'

#where transcripts are going to for translation (if not translated by whisper)
transcripts_directory = './transcr/' 


## whisper settings

# whisper-model
model_settings = 'base'

# whisper-task --> either "translate" | "transcribe"
# translate if you want whisper to translate | transcribe if you want to use different translator

#whisper_task_settings = 'transcribe'
whisper_task_settings = 'translate'

#if you want to tell whisper in which language audio files are (or leave None)
language = None

no_speech_threshold = 0.2

## pyaudio settings
# length of recorders in seconds
record_time_settings = 10

# device index for recordings
input_device_index = 3



## Translator settings

transcript_lang = "ja" # set to japanese
translation_lang = "en" # set to english










def get_filename():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def newest(path):
    while True:
        all_files = os.listdir(path)
        if not all_files:
            time.sleep(1)
        else:
            files = [f for f in all_files if os.path.isfile(os.path.join(path, f))]
            files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
            oldest_file = files[0]
            return oldest_file
    