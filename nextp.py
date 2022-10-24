import sys,time,os
def wait(w):
    time.sleep(w)

def typewriter(a): #first sentence
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
os.system("cls")



# w = 0.5
# wait(w)
# a = "\nYou are alone and disoriented, waist-deep in pool water. "
# typewriter(a)
# w = 1
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
    print("A. Try to noclip back to the real world")
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
            if info_smiler == "b":
                break
    if br1 == "b":
        print("You observe your environment.")
        