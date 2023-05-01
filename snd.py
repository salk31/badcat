import wave, sys, pyaudio


if __name__ == '__main__':

  wf = wave.open('snd/mg42a.wav')
  p = pyaudio.PyAudio()
  chunk = 40960
  stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)
  data = wf.readframes(chunk)
  while data != '':
    stream.write(data)
    data = wf.readframes(chunk)
    
  