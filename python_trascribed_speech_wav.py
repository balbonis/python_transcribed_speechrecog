from flask import Flask
app = Flask(__name__)


import os

import speech_recognition as sr



def find_wav_files(directory):

    wav_files = []

    for root, _, files in os.walk(directory):

        for file in files:

            if file.lower().endswith('.wav'):

                wav_files.append(os.path.join(root, file))

    return wav_files



def transcribe_audio(file_path):

   
    recognizer = sr.Recognizer()

    with sr.AudioFile(file_path) as source:

        print(f"Transcribing: {file_path}")

        audio_data = recognizer.record(source)

        try:

            # Perform the transcription using Google's API (requires internet connection)

            text = recognizer.recognize_google(audio_data)

            return text

        except sr.UnknownValueError:

            return "Audio not clear enough to transcribe."

        except sr.RequestError as e:

            return f"API request error: {e}"



def main():

    directory = os.getcwd()  # Automatically use the current working directory
    
    print(f"Searching for .wav files in: {directory}\n")

    
    wav_files = find_wav_files(directory)

    

    if not wav_files:

        print("No .wav files found in the current directory.")

        return

    
  
    for wav_file in wav_files:
        global message
        transcription = transcribe_audio(wav_file)
        print(f"\nTranscription for {wav_file}:\n{transcription}")
        message = message + "<br>" + str({transcription}  + "<br>" )


#if __name__ == "__main__":
#    main()


message = "<strong>KABOOM!!!! Transcribing your </strong> " 

@app.route("/")
def home():
    main()
    return message 