import sys,time,os
def wait(w):
    time.sleep(w)

def typewriter(a): #first sentence
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
os.system("cls")



# w = 0
# wait(w)
# a = "\nYou are alone and disoriented, waist-deep in pool water. "
# typewriter(a)
# w = 0
# wait(w)
# a = "\nWading aimlessly around the interior room with wall-to-wall tile, your memory evades you."
# typewriter(a)
# wait(w)
# a = "\nAfter making your way through a doorway bathed in light, the next room is a pool and the following room."
# typewriter(a)
# wait(w)
# a = "\nShit."
# typewriter(a)
# wait(w)
# a = "\nYour anxiety is swelling, but you soon find a small ledge to get out of the water."
# typewriter(a)
# wait(w)
# a = "\nThere’s no time to relax."
# typewriter(a)
# wait(w)
# a = "\nA shiver goes down your spine as you hear a mysterious splash off in the distance."
# typewriter(a)
# wait(w)
# a = "\nWhile trying to get a clear look, something disappears behind the corner."
# typewriter(a)
# wait(w)
# a = "\nYou continue walking along the ledge."
# typewriter(a)
# wait(w)
# a = "\nThe splashing sounds closer."
# typewriter(a)
# wait(w)
# a = "\nA walk turns into a jog which turns into a sprint."
# typewriter(a)
# wait(w)
# a = "\nYou slip, fall, and hit your head against the wet tile as everything goes black."
# typewriter(a)
# wait(w)
# a = "\nWhen you awake to the chlorine stench, it all starts to rush back."
# typewriter(a)
# wait(w)
# a = "\nYou are trying to escape the Backrooms."
# typewriter(a)
# wait(w)

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
        a = "\nYou see a smiler approaching your way"
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
                break
            if info_smiler == "b":
                break
            else:
                print("Error, Try again")
                print("--------------------")
            break
        a = "You see the Smiler slowly approaching you."
        typewriter(a)
        wait(w)
        a = "You don't have much time to think."
        while True:
            print("\nA. Use your phone as a flashlight to shine it at the Smiler.")
            wait(w)
            print("B. Make a run for it")
            smiler1 = input("\nType a or b: ")
            if smiler1 == "a":
                a = "You took your phone out and used the flashlight to scare off the smiler."
                a = "Fire starts engulfing the environment."
                a = "The chance of survival is slim but you don't give up just yet."
                a = "You proceed consciously walking alongside the wall avoiding the flames that spread rapidly."
                a = "It's been 30 minutes and you're slowly losing hope."
                a = "Until.."
                a = "The power shut off."
                a = "And a door suddenly opened."
                a = "Without hesitation you ran through the doorway and the room behind you exploded."
                a = "The door behind closed."
                a = 'A big floating message in the air says "NOBODY LIKES CHEATERS"'
                a = "You've just realized you're in a maze."
                a = "The fire continues engulfing the environment."
                a = "You're carefully walking through a section of the maze."
                a = "You see a skin-walker looking at you unaggravated."
                while True:
                    print("A. Show skin-walker information.")
                    wait(w)
                    print("B. Skip")
                    skin_info = input("Type a or b: ")
                    if skin_info == "a":
                        print("Entity 10, more commonly known as the Skin-Stealers, are large humanoid entities that can wear the skin of their victims as a disguise.")
                        wait(w)
                        print("They eat human flesh when in a hunger state.")
                        wait(w)
                        print("")
                    

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
                        a = "\nYou died."
                        typewriter(a)
                        wait(w)
                        print("\nUnlocked ending: Deception") 
                        break
                    break            
                break
    else:
        print("Error, Try again")
        print("--------------------------------------------------")                 


        