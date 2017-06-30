gender = (input("Are you a boy or girl?"))
name = (input("What is your name?"))
if gender == "boy":
    g == " he "
elif gender == "girl":
    g == " she "
else:
    exitonclose()
print("The child ran to the TV to watch Criminal Minds." + g + "always told everyone" + g  + "wanted to be a psychologist when" + g + "grew up, but the mother wanted her child to explore activities to set the future. She lectured about high school. Now a rising senior,"  + name + "has to plan out a path. Help choose!")
a = input("Do you want to take AP classes? \n\t a) Yes \n\t b) No")
if a == "a":
    YesAP = input("Will you procrastinate? \n\t a) Yes \n\t b) No")
    if YesAP == "a":
        print("You managed to graduate after barely passing your classes!")
        Proc = input("Do you want to \n\t a) Apply to college \n\t b) Go to the Workforce")
            if Proc == "a":
            elif Proc == "b":
    elif YesAP == "b":
        print("Congratulations! You rank in the top 10\% of your graduating class!")
        PostSecSchool = input("Do you want to apply to \n\t a) A Name School \n\t b) A No Name School")
            if PostSecSchool == "a":
                print("You have been accepted to your dream Ivy League/ CA State School. You have also been offered multiple internships due to an outstanding resume")
            elif PostSecSchool == "b":
                print("You have been accepted to your dream Ivy League/ CA State School. You have also been offered multiple internships due to an outstanding resume")
elif a == "b":
    NoAP = input("Would you want to have a job or invest time in extracurriculars? \n a) Job \n b)Extracurriculars")
    if NoAP == "a":
        print("You make enough to live off of")
        Money == input("Now do you want to \n\t a) Go to a 4 year Uni \n\t b) Write a book \n\t c) Drop a Mixtape")
        if Money == "a":
            print ("You have lived a stressfully college experience but earned with degree")
        elif Money == "b":
            print("You have earned the Noble Prize for your book!")
        elif Money == "c":
            print ("You blew up! You now use money as napkins.")
    elif NoAP == "b":
        print("You have gotten a scholarship for your talent.")
        PostSecSchool = input("Do you want to apply to \n\t a) A Name School \n\t b) A No Name School")
            if PostSecSchool == "a":
                print("You have been accepted to your dream Ivy League/ CA State School. You have also been offered multiple internships due to an outstanding resume")
                degree = input("Do you want one degree or two?")
            elif PostSecSchool == "b":
                print("You have been accepted to your dream Ivy League/ CA State School. You have also been offered multiple internships due to an outstanding resume")
