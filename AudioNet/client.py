import socket
import pyaudio
import wave
import sys

soc = socket.socket()

soc.connect(("127.0.0.1",80))

pa = pyaudio.PyAudio()

stream = pa.open(48000, 2, pyaudio.paInt16,output=True)

print("Playing")

while True:
    data = soc.recv(1024*1024)
    audio = stream.write(data)