import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice") 

while True:
    say = input("enter text to speech:\n")
    if say == "q":
        break
    speaker.speak(say)

