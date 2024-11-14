
from random import randint
inventory = []
endgame = 1
while endgame == 1:
    name = input("Hej, vad hetter du?")
    greeting = "välkommen till min värld[name]. Du vaknar upp efter lång natts sömn..."
    greeting = greeting.replace("[name]", name)
    print("Du vaknar upp efter en lång natts sömn...")
    print("Mystiskt nog finner du dig i en hamsters kropp, där du löper över ängarna i jakt på en gyllene maskros ")
    print("Du rycker till och fryser i din tanke, tittar du på [maskros], din mystiska [hamster]-kropp")
    choice = input("Vad väljer du?")
    if "hamster" in choice:
        print("I drömlik slowmotion beundrar du den fantastiska fluffigheten, dina sinnen förnimmer havre och damm.")
    elif "maskros" in choice:
        print("Du skriker inombords som den maskroallegriken du är, prosit, du stoppar maskrosen i din hamster påse")
        inventory.append("maskros")
    else:
        print("Stavning är inte din starka gren , du fortsätter...")
    print("Hasmtern ser en skum dör mit ute i fältet som ser ut att vara magisk för det fins ingenting på andra sidan av den men i den så finns det en stor bygnad")
    door = input("Går du in genom dören?")
    if "ja" in door:
        print("Du kliver in genom dören och den smälls igen bakom dig.")
    elif "nej" in door:
        print("du går för bi dören och du lever ett liv av tanke på vad som fanns bakom dören")
        endgame + 1
    print("framför dig står det en skaalbagge.")
    skalbagge = input("Attackerar du skalbaggen?")
    if "ja" in skalbagge:
        print("du attackerade skalbaggen och han vart arg")

