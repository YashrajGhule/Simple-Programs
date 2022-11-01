import wave,pyaudio

pa = pyaudio.PyAudio()

stream = pa.open(8000,2,pyaudio.paInt16,output=True)

wav = wave.Wave_read(r"D:\YASH FILES\SONGS\test.wav")
while True:
    data = wav.readframes(8000)
    stream.write(data)
    if data==b"":
        break
wav.close()
