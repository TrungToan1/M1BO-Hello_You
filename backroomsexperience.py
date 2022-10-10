import sys,time,os
def wait(w):
    time.sleep(w)

def typewriter(a): #first sentence
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
os.system("cls")

a = "You're in bed. "
w = 0.5
typewriter(a) #Sentence 1
wait(w)

a = "Trying to fall asleep after a long day of work.\n" 
w = 1
typewriter(a) #sentence 2
wait(w)
a = "You're bored of every day being the same."
typewriter(a)
wait(w)
a = "\nYou wish there was something else in life other than waking up in the same world.\n"
typewriter(a)
wait(w)

a = ". "
w = 0.7
typewriter(a)
wait(w)
typewriter(a)
wait(w)
typewriter(a)
print("\n")
w = 1.5
wait(w)

a = "You can't fall asleep."
typewriter(a)
w = 1
wait(w)

w = 0.5
while True:
    print("\nA. Stay in bed.")
    wait(w)
    print("B. Stand up.")
    wait(w)
    q1 = input("\nType a or b: ")
    if q1 == "a":
        w = 1
        a = "\nYou stayed in bed. Hoping you'll wake up tommorow"
        typewriter(a) #a1

        break
    
    elif q1 == "b":
        a = "You stood up. You felt like taking a walk in a park nearby."
        w = 0.5
        typewriter(a) #b1 
        wait(w)
        a = "\nYou wore your jacket and shoes, ready to leave."
        wait(w)
        a = "\nOn your way to the nearby park, you see an abandoned factory.\n"
        typewriter(a)
        w = 1
        wait(w)

        w = 0.5
        while True:
                print("A. Continue.")
                wait(w)
                print("B. Go to the abandoned factory.")
                wait(w)
                q1b = input("\nType a or b: ")
                if q1b == "a":
                    a = "You didn't think much of it and headed towards the park"
                    typewriter(a)
                    
                elif q1b == "b":
                    a = "You were curious and decided to go to the abandoned factory."
                    typewriter(a)
                    w = 1
                    wait(w)
                    a = "\nYou entered the abandoned factory."
                    typewriter(a)
                    wait(w)
                    a = "\nYou suddenly feel static electricity in the air around you."
                    typewriter(a)
                    wait(w)
                    a = "\nAs you walk through the dark abandoned factory you feel the static electricity in the air getting stronger."
                    typewriter(a)
                    wait(w)
                    while True:
                        w = 0.5
                        print("\nA. Keep exploring")
                        wait(w)
                        print("B. Go back")
                        wait(w)
                        q1bq = input ("\nType a or b: ")
                        if q1bq == "a":
                            w = 1
                            a = "The static electricity made you feel nauseous."
                            typewriter(a)
                            wait(w)
                            a = "\nWhen you headed back to the exit you tripped over a piece of broken debris."
                            typewriter(a)
                            wait(w)
                            a = "\nRight before you fell with your head on the ground, Everything turned dark."
                            typewriter(a)

                        elif q1bq == "b":
                            w = 1
                            a = "You ignored the strange feeling you have in your head"
                            typewriter(a)
                            wait(w)
                            a = "\nYour vision starts to get blurry, you're passing out"
                            typewriter(a)
                            break
    
w = 2
wait(w)
a = "\nYou are alone and disoriented, waist-deep in pool water. "
typewriter(a)
w = 1
wait(w)
a = "\nWading aimlessly around the interior room with wall-to-wall tile, your memory evades you."
typewriter(a)
wait(w)
a = "\nAfter making your way through a doorway bathed in light, the next room is a pool and the following room."
typewriter(a)
wait(w)
a = "\nShit."
typewriter(a)
wait(w)
a = "\nYour anxiety is swelling, but you soon find a small ledge to get out of the water."
typewriter(a)
wait(w)
a = "There’s no time to relax."
typewriter(a)
wait(w)
a = "A shiver goes down your spine as you hear a mysterious splash off in the distance."
typewriter(a)
wait(w)
a = 
            
               
        
    # else:
    #     os.system("cls")
    #     print("Error, Try again")
        
