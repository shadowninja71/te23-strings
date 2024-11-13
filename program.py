
inventory = []
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
    print("Stavning är inte din starka gren😊, du fortsätter...")

print(" men sen där...")