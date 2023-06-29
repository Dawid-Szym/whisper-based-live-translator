import os
import whisper
import torch
import atlas_settings


#whisper can run on cpu but gpu is basically necessary
torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(DEVICE)

model = whisper.load_model(atlas_settings.model_settings, device=DEVICE)
task=atlas_settings.whisper_task_settings
no_speech_threshold = atlas_settings.no_speech_threshold
lang = atlas_settings.language
output_directory = atlas_settings.transcripts_directory

print('looping..')
while True:
    oldest_file = atlas_settings.newest(atlas_settings.recordings_directory)

    audio = whisper.load_audio(atlas_settings.recordings_directory+oldest_file)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    if lang == None:
        _, probs = model.detect_language(mel)
    
    #print(f"Detected language: {max(probs, key=probs.get)}")

    #LANGUAGE SETTING
    options = whisper.DecodingOptions(language=lang, without_timestamps=True, fp16 = False)

    #decoding
    result = whisper.decode(model, mel, options)
    result = model.transcribe(atlas_settings.recordings_directory+oldest_file, task = task, no_speech_threshold=no_speech_threshold)


    #open&save to file or show translation
    if(atlas_settings.whisper_task_settings == "translate"):
        print(result['text'])
    elif(atlas_settings.whisper_task_settings == "transcribe"):
        new_file = atlas_settings.get_filename()
        with open(output_directory+new_file+'.txt', "w", encoding="utf-8") as file:
            file.write(repr(result['text']))
        file.close()
    


    # delete the file after transcription
    os.remove(os.path.join(atlas_settings.recordings_directory, oldest_file))


