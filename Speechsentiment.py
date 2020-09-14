import speech_recognition as sr
from textblob import TextBlob
def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("speak")
        audio = r.listen(source)
        print("Recognizing Now . ")
        try:
            get = r.recognize_google(audio)
            print("You have said \n" + get)
            blob = TextBlob(get)
            print(blob.sentiment)
            print("Audio Recorded Successfully \n ")
        except Exception as e:
            print("Error :  " + str(e))

        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()