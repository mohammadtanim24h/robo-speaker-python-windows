import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
print("Welcome to RoboSpeaker 1.0. Created by Tanim")
while True:
    text = input("Enter what you want me to speak: ")
    if text == "exit speaker":
        speak.Speak("Bye. See you again.")
        break
    speak.Speak(text)

