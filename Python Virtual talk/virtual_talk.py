import pyttsx3
import datetime
import webbrowser

friend =pyttsx3.init()
x = datetime.datetime.now()

friend.say("Hello how can i help you")
friend.runAndWait()
speech=input("say something:")

if speech=="how are you":
    friend.say("I am good what about u")
    friend.runAndWait()
elif speech=="what is your name":
    friend.say("my name is virtual talk")
    friend.runAndWait()
elif speech=="what is your age":
    friend.say("my age is 30 year")
    friend.runAndWait()
elif speech=="year":
    year = x.strftime("%Y")
    friend.say( year)
    friend.runAndWait()
elif speech =="what is python":
    friend.say("Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.")
    friend.runAndWait()
elif speech=="open google":
    friend.say("opening google")
    friend.runAndWait()
    webbrowser.open('www.google.com')  # Go to example.com
elif speech=="open youtube":
    friend.say("opening youtube")
    friend.runAndWait()
    webbrowser.open('www.youtube.com')  # Go to example.com
elif speech=="best tourist place":
    friend.say("best tourist place")
    friend.runAndWait()
    webbrowser.open('https://www.holidify.com/collections/tourist-places-in-india') 
elif speech=="bitcoin price":
    friend.say(" todays bitcoin price")
    friend.runAndWait()
    webbrowser.open("https://www.google.com/search?q=bitcoin+price&oq=bitcoin+price&aqs=chrome..69i57j0i67i131i433j0i131i433l2j0i20i263j0i433l2j0i457j0j0i433.3975j0j9&sourceid=chrome&ie=UTF-8")
elif speech=="what can you do for me":
    friend.say("I can say date . I can open google. I can open youtube . I can find todays bitcoin price")
    friend.runAndWait()
elif speech=="open twitter":
    friend.say("opening twitter")
    friend.runAndWait()
    webbrowser.open('https://www.twitter.com') 
elif speech=="open python website":
    friend.say("opening python website")
    friend.runAndWait()
    webbrowser.open('https://pypi.org/') 
elif speech=="open gmail":
    friend.say("opening Gmail")
    friend.runAndWait()
    webbrowser.open('https://gmail.com/') 

    


