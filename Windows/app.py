import speech_recognition as sr
from flask import Flask, request, render_template
from gtts import gTTS
import os
import playsound 
r = sr.Recognizer()

app = Flask(__name__)

# @app.route('/', methods= ["GET", "POST"])
# def index():
#    pass

def numbers(inp):
    num =[]
    for i in inp.split():
        if i.isdigit():
            num.append(float(i))
    return num

def voice_out(mytext):
    mytext = str(mytext)
    myobj = gTTS(text=mytext, lang='en', slow=False)  
    filename = 'output.mp3'
    myobj.save(filename)
    playsound.playsound(filename)
    print(mytext)

def operation(inp):
    num = numbers(inp)
    if "mod" in inp or "modulus" in inp or "modulo" in inp or "remainder" in inp:
        voice_out(mod(num))
    elif "root" in inp:
        voice_out(sq_root(num))
    elif "square" in inp or "itself" in inp:
        voice_out(square(num))  
    elif "add" in inp or "+" in inp or "plus" in inp:
        voice_out(add(num))      
    elif "subtract" in inp and "from" in inp:
        voice_out(subtract(num,flag=True)) #if flag is true num[1] - num[0]
    elif "-" in inp or "minus" in inp:
        voice_out(subtract(num,flag=False)) #if flag is flase num[0] - num[1]    
    elif "multiply" in inp or "times" in inp or "multiplied" in inp or "into" in inp or "x" in inp or "*" in inp:
        voice_out(multiply(num))    
    elif "divide" in inp or "by" in inp or "/" in inp:
        voice_out(divide(num))

def add(num):
    total = 0
    for i in num:
        total += i
    return total

def subtract(num,flag):
    if flag == True:
        total = num[1] - num[0]
    else:
        total = num[0] - num[1]
    return total

def multiply(num):
    total = 1
    for i in num:
        total *= i
    return total

def divide(num):
    total = num[0] / num[1]
    return total

def mod(num):
    total = num[0] % num[1]
    return total

def sq_root(num):
    total = num[0] ** (1/2)
    return total

def square(num):
    total = num[0] **2
    return total

with sr.Microphone() as source:
    print("Kuch toh bolo, sharma kyu rahe hai")
    audio = r.listen(source)
    inp = r.recognize_google(audio)
    print(inp)
    operation(inp.lower())