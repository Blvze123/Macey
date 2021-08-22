
import cv2
from simple_facerec import SimpleFacerec
import os.path
import time


# Facial Recognition Method

def capture():
    sfr = SimpleFacerec()

    cap = cv2.VideoCapture(0)

    capture.Found = False
    sfr.load_encoding_images("Encodes/")
    # Picks up pictures from videos
    while capture.Found != True:
        ret, frame = cap.read()

        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2);
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2)

            # If the name of the File is Found, it sends a variable
            if name == "Found":
                capture.Found = True
                cv2.destroyAllWindows()
                break
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)

        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def FaceCheck():
    # Checks if setup picture is already there
    if os.path.exists("Encodes/Found.jpg"):
        print("Setup Already Found")
        capture()
        print(capture.Found)
    else:

        # Setup
        x = input("Do you wish to setup right now,(y/n) \n")

        if x == "n":
            quit()
        elif x == "y":
            print("Taking Picture in 5 Seconds, Save Picture by pressing Y")
            time.sleep(5)
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            while (True):
                cv2.imshow('img1', frame)
                if cv2.waitKey(1) & 0xFF == ord('y'):
                    cv2.imwrite('Encodes/Found.jpg', frame)
                    cv2.destroyAllWindows()
                    break

            cap.release()
            print("Picture taken. Now Exiting...")
            quit()


# Main
FaceCheck()


def install(module):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])


# install("pyttsx3")
# install("speechRecognition")
# install("wikipedia")
# install("pipwin")
# subprocess.check_call([sys.executable, "-m", "pipwin", "install", "pyaudio"])

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import turtle

import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!, My name is macy, your voice assistant")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir !, My name is macy, your voice assistant")

    else:
        speak("Good Evening Sir!!! ,My name is macy, your voice assistant")

    speak("Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


# Games
# 1
'''
def the_pong_game():
    scr = turtle.Screen()
    scr.setup(width=900, height=750)
    scr.title("The PONG Game by Siddhant Kumar")
    scr.bgcolor("black")
    scr.tracer()

    # Border
    bor1 = turtle.Turtle()
    bor1.speed(0)
    bor1.shape('square')
    bor1.color('white')
    bor1.shapesize(stretch_len=37.5, stretch_wid=30.5)
    bor1.penup()
    bor1.goto(0, 0)

    bor2 = turtle.Turtle()
    bor2.speed(0)
    bor2.shape('square')
    bor2.color('black')
    bor2.shapesize(stretch_len=37.2, stretch_wid=30.2)
    bor2.penup()
    bor2.goto(0, 0)

    # Left Paddle
    l_paddle = turtle.Turtle()
    l_paddle.speed(0)
    l_paddle.shape("square")
    l_paddle.color("white")
    l_paddle.shapesize(stretch_wid=5, stretch_len=1)
    l_paddle.penup()
    l_paddle.goto(-350, 0)

    # Right Paddle
    r_paddle = turtle.Turtle()
    r_paddle.speed(0)
    r_paddle.shape("square")
    r_paddle.color("white")
    r_paddle.shapesize(stretch_wid=5, stretch_len=1)
    r_paddle.penup()
    r_paddle.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.shapesize(stretch_wid=1, stretch_len=1)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 7
    ball.dy = 7

    # Score Board
    s_board = turtle.Turtle()
    s_board.speed(0)
    s_board.shape("square")
    s_board.color("white")
    s_board.penup()
    s_board.hideturtle()
    s_board.goto(0, 320)
    s_board.write("Player A : 0       |       Player B : 0", align="center", font=("Courier", 24, 'normal'))

    # Functions
    def l_paddle_up():
        y = l_paddle.ycor()
        y += 20
        l_paddle.sety(y)

    def r_paddle_up():
        y = r_paddle.ycor()
        y += 20
        r_paddle.sety(y)

    def l_paddle_down():
        y = l_paddle.ycor()
        y -= 20
        l_paddle.sety(y)

    def r_paddle_down():
        y = r_paddle.ycor()
        y -= 20
        r_paddle.sety(y)

    # Linking the keyboard
    scr.listen()
    scr.onkeypress(l_paddle_up, "w")
    scr.onkeypress(l_paddle_down, "s")
    scr.onkeypress(r_paddle_up, "Up")
    scr.onkeypress(r_paddle_down, "Down")

    # Scores
    score_a = 0
    score_b = 0

    # Main game loop
    while True:
        scr.update()

        # Ball Movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collisions
        # Top and bottom
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Left and right
        if ball.xcor() > 350:
            score_a += 1
            s_board.clear()
            s_board.write("Player A : {}       |       Player B : {}".format(score_a, score_b), align="center",
                          font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            s_board.clear()
            s_board.write("Player A : {}       |       Player B : {}".format(score_a, score_b), align="center",
                          font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < l_paddle.ycor() + 50 and ball.ycor() > l_paddle.ycor() - 50:
            ball.dx *= -1

        elif ball.xcor() > 340 and ball.ycor() < r_paddle.ycor() + 50 and ball.ycor() > r_paddle.ycor() - 50:
            ball.dx *= -1
'''

# 2
def the_snake_game():
    delay = 0.1
    score = 0
    high_score = 0

    # Creating a window screen
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("blue")
    # the width and height can be put as user's choice
    wn.setup(width=600, height=600)
    wn.tracer(0)

    # head of the snake
    head = turtle.Turtle()
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"

    # food in the game
    food = turtle.Turtle()
    colors = random.choice(['red', 'green', 'black'])
    shapes = random.choice(['square', 'triangle', 'circle'])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(0, 100)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Score : 0  High Score : 0", align="center",
              font=("candara", 24, "bold"))

    # assigning key directions
    def goup():
        if head.direction != "down":
            head.direction = "up"

    def godown():
        if head.direction != "up":
            head.direction = "down"

    def goleft():
        if head.direction != "right":
            head.direction = "left"

    def goright():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    wn.listen()
    wn.onkeypress(goup, "w")
    wn.onkeypress(godown, "s")
    wn.onkeypress(goleft, "a")
    wn.onkeypress(goright, "d")

    segments = []

    # Main Gameplay
    while True:
        wn.update()
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            # Adding segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("orange")  # tail colour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        # Checking for head collisions with body segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                colors = random.choice(['red', 'blue', 'green'])
                shapes = random.choice(['square', 'circle'])
                for segment in segments:
                    segment.goto(1000, 1000)
                segment.clear()

                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
        time.sleep(delay)

    wn.mainloop()





if __name__ == "__main__":
    wishMe()
    Activate = True
    while Activate:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        # Casual Conversations
        if 'Hello' in query:
            speak('hi,what can i do for you today')

        elif "how are you" in query:
            speak("I am perfectly fine. How's your day going?")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is,{strTime}")

        elif "can you do me a favour" in query:
            speak("What can I do for you?")

        elif 'who created you' in query:
            speak("I was created by a bunch of kids")

        elif "weather" in query:
            webbrowser.open('https://weather.com/en-IN/weather/today/')

        elif 'i want to play a game' in query:
            speak('which game do you want to play. pong game or snake game ')

        # Website acessing commands
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'close youtube' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'close instagram' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'close facebook' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'close google' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'close stackoverflow' in query:
            os.system("taskkill /im chrome.exe /f")

        elif "open prime video" in query:
            webbrowser.open("www.primevideo.com")

        elif "close prime video" in query:
            os.system("taskkill/im chrome.exe /f")

        elif "open netflix" in query:
            webbrowser.open("www.netflix.com")

        elif "close netflix" in query:
            os.system("takkill/im chrome.exe /f")

        elif 'open hotstar' in query:
            webbrowser.open("www.hotstar.com")

        elif "close hotstar" in query:
            os.system("taskkill/im chrome.exe /f")

        elif "open Z5" in query:
            webbrowser.open("www.zee5.com")

        elif "close Z5" in query:
            os.system("taskkill/im chrome.exe /f")

        # elif 'play music' in query:
        #    music_dir ='C:\\Users\\Kartik\\Desktop\\CS KK'
        #    songs = os.listdir(music_dir)
        #    print(songs)
        #    os.startfile(os.path.join(music_dir, songs[0]))

        elif 'close' in query:
            Activate = False
            quit()
           

        # Play Games

        elif 'pong game' in query:
            speak('use W S keys to move the left paddle and Up and Down keys to move the right paddle')
            the_pong_game()


        elif 'snake game' in query:
            speak('use w,a,s,d keys to move the snake and change its direction')
            the_snake_game()

        # elif 'flappy' in query:
        #     speak('use spacebar to make the bird fly')
        #     flappy_game()

        # For the use of this command, please replace 'app_name' with the name of the app you want to open and also replace
        # 'app_location' with the location of the app in your machine.

        #########################################

        elif 'something' in query:
            speak('Do not worry, I am your secret keeper')
            DATA = takeCommand()
            file = open('secret.txt', 'a')
            file.write(DATA)
            file.close()
            speak('Do not worry, I am fully secured with passwords and face recognition')

        elif 'today' in query:
            speak('Tell me, I am excited to know')
            story = takeCommand()
            file = open('today.txt', 'a')
            file.write(story)
            file.close()
            speak('Do not worry, I am fully secured with passwords and face recognition')

        elif 'goals' in query:
            speak('Thats impressive, let me store that to motivate you')
            passion = takeCommand()
            file = open('goal.txt', 'a')
            file.write(passion)
            file.close()
            speak('Do not worry, I am fully secured with passwords and face recognition')


        elif 'remember my secrets' in query:
            speak('Yes I do remember, I am your secret keeper')

            file = open('secret.txt', 'r')
            a = file.read()
            file.close()
            speak(a)



        elif 'my goal' in query:
            speak('yes, I do remember your goals')

            file = open('goal.txt', 'r')
            b = file.read()
            file.close()
            speak(b)
        elif 'kill' in query:
            Activate = False
            quit()

