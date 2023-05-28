# whisper-based-live-translator
Messy live translation project based on OpenAI Whisper. 
Still working on it. Here are just the files I run. Obviously won't work out of the box. 
Check out repo made by OpenAI it's very cool. My project works by running 3 python files at the same time which is 3 too many. It works which is great. 
But it has huge performance and quality issues which is not great. Take a look for some parts that may be useful to you.

# recorders - make files for translation (I highy recommend to record from speakers)
recorder.py - I used it to record from the mic.
recorder2.py - 'newer' version that I use now.

# transcriber - transcribes the oldets recorded file from a directory
transcriber.py - Modified many times over time. At first I used Whisper for both transcription and translation. Now I use separate translator because of performance issues.

# translators - not necessary (whisper has translation option). I tested few translators, but argotranslate is working offline so it's the one I stuck with (when not using whisper to translate directly)
translator.py - Used for testing many translators. 
translator2.py - Translating transcripts using argotranslate
