import pyttsx3 

print("\n This is the program which will help you to find the divisible numbers of your number!!")
ch=1
engine= pyttsx3.init() 
engine.setProperty("rate", 115)
engine.say(" This is the program which will help you to find the divisible numbers of your number")
while ch==1:
    engine.runAndWait()
    engine.say("Which number's divisible number you want")
    engine.runAndWait()
    x=int(input("Which number's divisible no. you want? : "))
    engine.say("This is your Divisible Number's of"+str(x))
    g=0
    for a in range(1,x+1):
        g=g+1
        b=int(x%g)
        if b==0:
            print(g)
            engine.setProperty("rate",200)
            engine.say(g)
    engine.setProperty("rate",115)
    engine.say("Thanks for using this program , Do you want to use again")
    engine.runAndWait()
    ch=int(input("Thanks for using this program.Do you want to use again?(Yes(1),No(0)) : "))

