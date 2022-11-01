import socket
import pyaudio
import wave

soc = socket.socket()
soc.bind(("127.0.0.1",80))
soc.listen(1)

c,addr = soc.accept()

pa = pyaudio.PyAudio()

stream = pa.open(48000, 2, pyaudio.paInt16,input=True)

print("Recording")

while True:
    audio = stream.read(int(48000*0.01))
    c.send(audio)
