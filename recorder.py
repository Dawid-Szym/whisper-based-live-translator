import pyaudio
import wave
import atlas_settings

chunk = 1024 
sample_format = pyaudio.paInt16
channels = 1
fs = 44100
filepath = atlas_settings.recordings_directory


while True:
    filename = atlas_settings.get_filename()
    print('rec...')

    p = pyaudio.PyAudio()
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True,
                    input_host_api_specific_stream_info=atlas_settings.input_device_index)
    frames = []
    for i in range(0, int(fs / chunk * atlas_settings.record_time_settings)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filepath+filename+".wav", 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    
