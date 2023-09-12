import speech_recognition as spr
import pyaudio, wave, pyautogui

def record(time, fname):
    recorder = pyaudio.PyAudio()
    stream = recorder.open(44100, 1, pyaudio.paInt16, True, frames_per_buffer=1024)
    print("* Запись")
    pyautogui.alert("Нажмите 'OK', если готовы начать")
    frames = []
    for i in range(0, int(44100 / 1024 * time)):
        data = stream.read(1024)
        frames.append(data)
    print("* Записано")
    stream.stop_stream()
    stream.close()
    recorder.terminate()

    wf = wave.open(fname, 'wb')
    wf.setnchannels(2)
    wf.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

def recognize(fname):
    with spr.AudioFile(fname) as source:
        recoger = spr.Recognizer()
        source = recoger.listen(source)
        resp = recoger.recognize_google(source, language='ru-RU')
        return resp #"\n".join(resp)

if __name__ == '__main__':
    record(120, 'exam.wav')
    with open('recog.txt', 'w') as file:
        # time = int(input(''))
        pyautogui.alert("Запись завершена. Нажмите 'OK', чтобы начать её распознавание")
        print('Распознаём голос...')
        r = recognize('exam.wav')
        file.write(r)
        print(r)
