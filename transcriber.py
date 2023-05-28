import os
import whisper
import time
import torch
import torchaudio
import numpy
import datetime
from whisper.utils import get_writer


#whisper can run on cpu but gpu is basically necessary
torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(DEVICE)


dir_path = '' #set the same path in recorder

model = whisper.load_model("base", device=DEVICE) #I use "base" model. All models are listed on OpenAI Whisper repo
task='transcribe' #set to either 'transcribe' or 'translate'
no_speech_threshold = 0.2 #I still tinker with no speech threshold setting to reduce artifacts
lang = None #if you want to specify a language of the file
output_directory = '' #where transcripts are going to for translation
now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d_%H-%M-%S")




print('looping..')
while True:
    all_files = os.listdir(dir_path)
    if not all_files:#if there are no files to transcribe
        #print('Dir empty...')
        time.sleep(1) #sleep for 1 second
    else:
        #list
        files = [f for f in all_files if os.path.isfile(os.path.join(dir_path, f))]

        #sort the list by modification time in ascending order
        files.sort(key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))

        # get the oldest file
        oldest_file = files[0]
        #print('Processing file:', oldest_file)

        #load
        audio = whisper.load_audio(dir_path+oldest_file)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        if lang == None:
            _, probs = model.detect_language(mel)
        
        #print(f"Detected language: {max(probs, key=probs.get)}")

        #LANGUAGE SETTING
        options = whisper.DecodingOptions(language=lang, without_timestamps=True, fp16 = False)

        #decoding
        result = whisper.decode(model, mel, options)
        result = model.transcribe(dir_path+oldest_file, task = task, no_speech_threshold=no_speech_threshold)


        #open&save to file
        now = datetime.datetime.now()
        filename2 = now.strftime("%Y-%m-%d_%H-%M-%S")
        with open(output_directory+filename2+'.txt', "w", encoding="utf-8") as file:
            file.write(repr(result['text']))
        file.close()


        # delete the file after transcription
        os.remove(os.path.join(dir_path, oldest_file))
