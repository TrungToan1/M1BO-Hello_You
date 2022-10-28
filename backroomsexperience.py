import sys,time,os
from xml.etree.ElementTree import TreeBuilder
def wait(w):
    time.sleep(w)

def typewriter(a): #first sentence
    for char in a:
        sys.stdout.write(char) 
        sys.stdout.flush()
        time.sleep(0.03)
os.system("cls")

def slowwriter(a): #first sentence
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)
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
        w = 1
        wait(w)
        a = "\nYou woke up in shock."
        slowwriter(a)
        wait(w)
        a = "\nYou're breathing heavily."
        slowwriter(a)
        wait(w)
        a = "\nYou can't move."
        slowwriter(a)
        wait(w)
        a = "\nYou start to panic."
        slowwriter(a)
        wait(w)
        a = "\nYour heartrate increases."
        slowwriter(a)
        wait(w)
        a = "\nThe door of your room slowly opens."
        slowwriter(a)
        wait(w)
        a = "\nYou can see the darkness through the doorframe."
        slowwriter(a)
        wait(w)
        a = "\nA terrifying dark entity emerges from the darkness."
        slowwriter(a)
        wait(w)
        a = "\nYou can see the bloody smile on it's head."
        slowwriter(a)
        wait(w)
        a = "\nYou want to scream but you can't"
        slowwriter(a)
        wait(w)
        a = "\nThe entity leaps towards you."
        slowwriter(a)
        wait(w)
        a = "\n\nYou woke up."
        typewriter(a)



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

        done = False
        while not done:
                print("\nA. Continue.")
                wait(w)
                print("B. Go to the abandoned factory.")
                wait(w)
                q1b = input("\nType a or b: ")
                if q1b == "a":
                    a = "\nYou didn't think much of it and headed towards the park."
                    typewriter(a)
                    wait(w)
                    a = "\nThe streets are peaceful."
                    slowwriter(a)
                    wait(w)
                    a = "\nYou have the feeling that someone is watching you."
                    slowwriter(a)
                    wait(w)
                    while True:
                        print("\nA. Return home")
                        wait(w)
                        print("B. Ignore the feeling")
                        watching = input("\nType a or b: ")
                        if watching == "a":
                            a = "\nYou trust your gut feeling and decided to head back home."
                            typewriter(a)
                            wait(w)
                            break
                        elif watching == "b":
                            a = "\nYou ignored the feeling, you headed towards the park."
                            typewriter(a)
                            wait(w)
                            break
                        
                        else:
                            print("Error, Try again.")
                            print("--------------------------------------------------")
                    
                    a = "\nYou see a very tall creature in the distance."
                    typewriter(a)
                    wait(w)
                    a = "\nIt's looking at you in the distance."
                    typewriter(a)
                    wait(w)
                    a = "\nYou're terrified."
                    typewriter(a)
                    wait(w)
                    a = "\nYou walked into an alleyway hoping it'll lose you."
                    typewriter(a)
                    wait(w)
                    a = "\nYou feel like you're the only person on the planet."
                    typewriter(a)
                    wait(w)
                    a = "\nIt doesn't feel right."
                    typewriter(a)
                    wait(w)
                    a = "\nYou see a wall with a darker spot in the middle."
                    typewriter(a)
                    wait(w)
                    while True:
                        print("\nA. Inspect it")
                        wait(w)
                        print("B. Ignore it")
                        wall = input("\nType a or b: ")
                        if wall =="a":
                            a = "\nYou walked up the wall with a raised hand."
                            typewriter(a)
                            wait(w)
                            a = "\nYou tried to lean against it but you fell through it."
                            typewriter(a)
                            wait(w)
                            a = "\nEverything went black."
                            typewriter(a)
                            wait(w)
                            a = "\nAnd when you woke up."
                            typewriter(a)
                            wait(w)
                            
                            done = True
                            break

                        elif wall == "b":
                            a = "\nYou heard a sound right behind you."
                            slowwriter(a)
                            wait(w)
                            a = "\nYou knew what it was but you don't want to turn around."
                            slowwriter(a)
                            wait(w)
                            a = "\nYou look up and you see a head facing towards you attached to a long neck behind you."
                            slowwriter(a)
                            wait(w)
                            print("\n\nUnlocked ending: Tracked down")
                            wait(9999)

                        else:
                            print("Error, Try again") #where i left off
                            print("--------------------------------------------------")
                    
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
                        print("\nA. Go back")
                        wait(w)
                        print("B. Keep exploring")
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
                            a = "\nRight before you fell with your head on the ground, Everything turned dark.\n\n"
                            typewriter(a)
                            break

                        elif q1bq == "b":
                            w = 1
                            a = "You ignored the strange feeling you have in your head."
                            typewriter(a)
                            wait(w)
                            a = "\nYour vision starts to get blurry, you're passing out."
                            typewriter(a)
                            break
                        
                        else:
                            print("Error, Try again")
                            print("--------------------------------------------------")
                    break
                    
                else:
                    print("Error, Try again")
                    print("--------------------------------------------------")        
        break
    
    else:
        print("Error, Try again.")
        print("------------------------------------------------------------")

w = 1
wait(w)
a = "\nYou are alone and disoriented, waist-deep in pool water. "
typewriter(a)
w = 0.5
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
a = "\nThere’s no time to relax."
typewriter(a)
wait(w)
a = "\nA shiver goes down your spine as you hear a mysterious splash off in the distance."
typewriter(a)
wait(w)
a = "\nWhile trying to get a clear look, something disappears behind the corner."
typewriter(a)
wait(w)
a = "\nYou continue walking along the ledge."
typewriter(a)
wait(w)
a = "\nThe splashing sounds closer."
typewriter(a)
wait(w)
a = "\nA walk turns into a jog which turns into a sprint."
typewriter(a)
wait(w)
a = "\nYou slip, fall, and hit your head against the wet tile as everything goes black."
typewriter(a)
wait(w)
a = "\nWhen you awake to the chlorine stench, it all starts to rush back."
typewriter(a)
wait(w)
a = "\nYou are trying to escape the Backrooms."
typewriter(a)
wait(w)

w = 0.3
while True:
    print("\n\nA. Try to noclip back to the real world")
    wait(w)
    print("B. Explore\n")
    wait(w)
    br1 = input("Type a or b: ")
    if br1 == "a":
        a = "\nYou were teleported to a different building."
        typewriter(a)
        wait(w)
        a = "\nEverything seems normal."
        typewriter(a)
        wait(w)
        a = "\nYou looked around and observed your surroundings."
        typewriter(a)
        wait(w)
        a = "\nYou walk around for a while and noticed that there's a sign on the wall that says YOU CHEATED."
        typewriter(a)
        wait(w)
        a = "\nSuddenly.."
        typewriter(a)
        wait(w)
        a = "\nPortions of the ceilings start to decline."
        typewriter(a)
        wait(w)
        a = "\nHorrifying entities start to spawn."
        typewriter(a)
        wait(w)
        a = "\nYour sanity is diminishing."
        typewriter(a)
        wait(w)
        a = "\nYou see a smiler approaching your way."
        typewriter(a)
        wait(w)
        w = 0.1
        while True:
            print("\nA. Show Smiler information")
            wait(w)
            print("B. Skip")
            info_smiler = input("type a or b: ")
            if info_smiler == "a":
                print("Smilers are hostile entities, recognizable by their signature reflective eyes and gleaming teeth.")
                wait(w)
                print("These entities only appear in dark corners or doorways, where the rest of their form is not visible.")
                wait(w)
                print("Sighting of these entities are among the most common in the Backrooms.")
                wait(w)
                print("It is speculated that these entities do not have bodies; rather, the darkness is their bodies; however, some researchers beg to differ.")
                wait(w)
                print("Smilers don't like illuminated areas.")
                w = 3
                wait(w)
                break
            if info_smiler == "b":
                break
            else:
                print("Error, Try again")
                print("--------------------")

        a = "You see the Smiler slowly approaching you."
        typewriter(a)
        w = 0.5
        wait(w)
        a = "You don't have much time to think."
        w = 0.5
        while True:
            print("\nA. Use your phone as a flashlight to shine it at the Smiler.")
            wait(w)
            print("B. Make a run for it")
            smiler1 = input("\nType a or b: ")
            if smiler1 == "a":
                a = "\nYou took your phone out and used the flashlight to scare off the smiler."
                typewriter(a)
                wait(w)
                a = "\nFire starts engulfing the environment."
                typewriter(a)
                wait(w)
                a = "\nThe chance of survival is slim but you don't give up just yet."
                typewriter(a)
                wait(w)
                a = "\nYou proceed consciously walking alongside the wall avoiding the flames that spread rapidly."
                typewriter(a)
                wait(w)
                a = "\nIt's been 30 minutes and you're slowly losing hope."
                typewriter(a)
                wait(w)
                a = "\nUntil.."
                typewriter(a)
                wait(w)
                a = "\nThe power shut off."
                typewriter(a)
                wait(w)
                a = "\nAnd a door suddenly opened."
                typewriter(a)
                wait(w)
                a = "\nWithout hesitation you ran through the doorway and the room behind you exploded."
                typewriter(a)
                wait(w)
                a = "\nThe door behind closed."
                typewriter(a)
                wait(w)
                a = '\nA big floating message in the air says "NOBODY LIKES CHEATERS".'
                typewriter(a)
                wait(w)
                a = "\nYou've just realized you're in a maze."
                typewriter(a)
                wait(w)
                a = "\nThe fire continues engulfing the environment."
                typewriter(a)
                wait(w)
                a = "\nYou're carefully walking through a section of the maze."
                typewriter(a)
                wait(w)
                a = "\nYou see a skin-stealer looking at you unaggravated."
                typewriter(a)
                wait(w)
                while True:
                    print("\nA. Show skin-stealer information.")
                    wait(w)
                    print("B. Skip")
                    skin_info = input("\nType a or b: ")
                    if skin_info == "a":
                        print("Entity 10, more commonly known as the Skin-Stealers, are large humanoid entities that can wear the skin of their victims as a disguise.")
                        wait(w)
                        print("They eat human flesh when in a hunger state.")
                        wait(w)
                        print("Otherwise roam if they do not need to eat.")
                        wait(w)
                        print("Their blood is translucent, and they can mimic human speech.")
                        wait(w)
                        print("They have impressive physical abilities.")
                        w = 5
                        wait(w)
                        break
                    elif skin_info == "b":
                        break
                    else:
                        print("Error, Try again.")
                        print("--------------------------------------------------")
                a = "\nIt approaches you in curiosity."
                w = 0.5
                typewriter(a)
                wait(w)
                a = "\nYou feel like you're in danger."
                typewriter(a)
                wait(w)
                while True:
                    print("\nA. Stand your ground.")
                    wait(w)
                    print("B. Run away")
                    skin_stealer1 = input("\nType a or b: ")
                    if skin_stealer1 == "a":
                        a = "You stared it down as it gently walks towards you."
                        slowwriter(a)
                        wait(w)
                        a = "\nIt suddenly grabbed you by the arm."
                        slowwriter(a)
                        wait(w)
                        a = "\nIt tore your arm off."
                        slowwriter(a)
                        wait(w)
                        a = "\nYou scream in agony."
                        slowwriter(a)
                        wait(w)
                        print("\n\nEnding unlocked: Naivety")
                        wait(9999)
                    elif skin_stealer1 == "b":
                        a = "You ran away."
                        typewriter(a)
                        wait(w)
                        a = "\nYou looked behind you to make sure it wasn't chasing you."
                        typewriter(a)
                        wait(w)
                        a = "\nYou're out of breath."
                        typewriter(a)
                        wait(w)
                        a = "\nYou survived for an hour."
                        typewriter(a)
                        wait(w)
                        a = "\nA quarter fell from the ceiling to the ground."
                        typewriter(a)
                        wait(w)
                        a = "\nYou decided to pick it up."
                        typewriter(a)
                        wait(w)
                        a = "\nYou walked to the nearest Arcade machine."
                        typewriter(a)
                        wait(w)
                        while True:
                            print("\nA. Insert coin")
                            wait(w)
                            print("B. Keep coin")
                            endingmaze = input("\nType a or b: ")
                            if endingmaze =="a":
                                a = "\nYou inserted the coin into the Arcade machine."
                                typewriter(a)
                                wait(w)
                                a = "\nYou got teleported to the same room where it all started..."
                                typewriter(a)
                                wait(w)
                                print("\n\nUnlocked Ending: Apeirophobic")
                                break
                            elif endingmaze == "b":
                                a = "\nYou put the quarter in your pocket and continued."
                                typewriter(a)
                                wait(a)
                                a = "\nAn arcade machine explodes right as you walked past it."
                                typewriter(a)
                                wait(a)
                                a = "\nYou were launched in the air because of the shockwave."
                                typewriter(a)
                                wait(a)
                                a = "\nDebris started falling around you."
                                typewriter(a)
                                wait(a)
                                a = "\nYou can't move."
                                typewriter(a)
                                wait(a)
                                a = "\nYou're in pain."
                                typewriter(a)
                                wait(a)
                                print("\n\nUnlocked Ending: Kakorrhaphiophobic")
                                wait(9999)
                            else:
                                print("Error, Try again.")
                                print("--------------------------------------------------")
                    else:
                        print("Error, Try again.")
                        print("--------------------------------------------------")
            elif smiler1 == "b":
                a = "\nYou ran."
                slowwriter(a)
                wait(w)
                a = "\nYou suddenly feel cold on your back."
                slowwriter(a)
                wait(w)
                a = "\nYou stopped running."
                slowwriter(a)
                wait(w)
                a = "\nYou realized you're missing a huge part of your back."
                slowwriter(a)
                wait(w)
                a = "\nYou turned around and see blood on the Smiler's mouth."
                slowwriter(a)
                wait(w)
                a = "\nThe Smiler's face is the last thing you saw."
                slowwriter(a)
                wait(w)
                a = "\nYou collapsed to the ground."
                slowwriter(a)
                wait(w)
                print("\n\nUnlocked ending: Inexperienced")
                wait(9999)
            else:
                print("Error, Try again.")
                print("--------------------------------------------------")
    elif br1 == "b":
                a = "\nYou're present in an expansive non-Euclidean space, resembling the back rooms of a retail outlet."
                typewriter(a)
                wait(w)
                a = "\nAll rooms share the same superficial features, worn mono-yellow wallpaper, old moist carpet, scattered electrical outlets, and \ninconsistently-placed fluorescent lighting. "
                typewriter(a)
                wait(w)
                a = "\nThe fluorescent lighting hums at a constant frequency."
                typewriter(a)
                wait(w)
                a = "\nEverything seems odd."
                typewriter(a)
                wait(w)
                a = "\nThis buzzing is notably louder and more obtrusive than ordinary fluorescent lights."
                typewriter(a)
                wait(w)
                a = "\nYou suddenly hear someone calling for help."
                typewriter(a)
                wait(w)
                a = '\nA noise that sounds like "Help me".'
                typewriter(a)
                wait(w)
                w = 0.3
                while True:
                    print("\n\nA. Locate where the sound comes from.")
                    wait(w)
                    print("B. Move away from it and continue.")
                    lvl_0 = input("\nType a or b: ")
                    if lvl_0 == "a":
                        a = "\nYou peeked around the corner of the wall next to you."
                        typewriter(a)
                        wait(w)
                        a = "\nYou see a tall endoskeleton standing in the middle of an open room."
                        typewriter(a)
                        wait(w)
                        a = "\nIn fear, you quickly but silently went the other direction until you heard a loud scream towards your direction."
                        typewriter(a)
                        wait(w)
                        a = "\nAdrenaline rushed your body as your flight or fight response took action."
                        typewriter(a)
                        wait(w)
                        a = "\nYou tried to run in a zig-zag motion to lose the potentially dangerous entity."
                        typewriter(a)
                        wait(w)
                        a = "\nYou tripped because you have skill issue."
                        typewriter(a)
                        wait(w)
                        a = "\nYou are paralyzed because of fear."
                        typewriter(a)
                        wait(w)
                        a = "\nYou can hear the sound of heavy footsteps getting closer."
                        typewriter(a)
                        wait(w)
                        print("\nUnlocked ending: Deception") 
                        wait(9999)
                    elif lvl_0 == "b":
                        a = "\nYou didn't pay much attention to it and continued exploring."
                        typewriter(a)
                        wait(w)
                        a = "\nYou notice several arrows pointing to 1 location."
                        typewriter(a)
                        wait(w)
                        while True:
                            print("\nA. Follow the arrows")
                            wait(w)
                            print("B, Go another direction")
                            arrow = input("type a or b: ")
                            if arrow == "a":
                                a = "You followed the arrows."
                                slowwriter(a)
                                wait(w)
                                a = "You see an open door with white light shining through."
                                slowwriter(a)
                                wait(w)
                                print("Unlocked Ending: You have escaped The Backrooms.")
                                wait(9999)
                            elif arrow == "b":
                                a = "You went the opposite direction the arrows pointed at."
                                slowwriter(a)
                                wait(w)
                                a = "\nYou have encountered a tall endoskeleton-like creature."
                                slowwriter(a)
                                print("\n\nUnlocked Ending: You were so close.")
                                wait(9999)
