gender = (input("Are you a boy or girl?\n"))
name = (input("What is your name?\n"))
g = "hi"
if gender == "boy":
    g = " He "
elif gender == "girl":
    g = " She "
else:
    exitonclose()
print("The child ran to the TV to watch Criminal Minds.\n" + g + "always told everyone" + g  + "wanted to be a psychologist when" + g + "grew up, but the mother wanted her child to explore activities to set the future.\n She lectured about high school. Now a rising senior, "  + name + " has to plan out a path. Help choose!\n")
#AP classes or not
a = input("Do you want to take AP classes? \n\t a) Yes \n\t b) No\n")
if a == "a":
    #Procrastinate or not
    YesAP = input("Will you procrastinate? \n\t a) Yes \n\t b) No\n")
    if YesAP == "a":
        print("You managed to graduate after barely passing your classes!\n")
        #Apply to college or go to the workforce
        Proc = input("Do you want to \n\t a) Apply to college \n\t b) Go to the Workforce\n")
        if Proc == "a":
            #Apply to prestigious school or not
            PostSecSchool = input("Do you want to apply to \n\t a) A Name School \n\t b) A No Name School\n")
            if PostSecSchool == "a":
                print("You have been accepted to your dream Ivy League/ CA State School.\n You have also been offered multiple internships due to an outstanding resume\n")
                print("You complete college one year earlier than expected! Amazing!\n")
                print("You found a job and climbed the rankings at a rapid speed thanks to your previous hard work ethic.\n Your mom calls you to tell you she's incredibly proud of you!\n")
                #Start a family or not
                fam = input("You see an attractive human on the street. Talk to them? \n\ta) Talk to them \n\tb) Do not talk to them\n")
                if fam == "a":
                    print("You've found your soulmate and started a family! You have/adopt kids and retire at old age. You die a few years later. Good life!")

                elif fam == "b":
                    print("You die alone after retirement for being so anti-social, but your mom is still proud of you. Decent life!")

            elif PostSecSchool == "b":
                print("You have been accepted to your dream Ivy League/ CA State School.\n You have also been offered multiple internships due to an outstanding resume.\n")
                print("You get a job as the assistant of the president! Wonderful!\n")
                print("After four years, you run as president and successfully woo the masses to ascend to the president's position!\n")
                fam = input("Start a family? \n\ta) Yes \n\tb) No\n")
                if fam == "a":
                    print("You live a nice life with your family and are remembered by all posterity as one of the world's presidents.\n Good life!")

                if fam == "b":
                    print("You die alone after retiring from government work.\n But it's okay, your name is eternally in the ranks as a good president!\n Nice life!")

        elif Proc == "b":
            talk = input("You meet a man on the street, do you talk to him or not? \n\ta) Talk to him \n\tb) Do not talk to him.\n")
            if talk == "a":
                print("You've made connections and successfully gotten a job.")
                conflict = input("Your new boss scolds you for coming in late despite your protest about having to help an old man while commuting to work.\nDo you \n\ta) Plead for forgiveness or \n\tb) Argue back?\n")
                if conflict == "a":
                    print("Your boss forgives you and starts to like you! You're on your way to promotion!")
                elif conflict == "b":
                    print("Your boss gets angry, but is impressed with your guts.\n Your boss starts to like you! You're on your way to promotion! :)")
                fam = input("Because your boss favors you, you've inherited his position as CEO of the company after he retires!\n You're rich! Do you want to start a family? \n\ta) Yes \n\tb) No\n")
                if fam == "a":
                    print("You've started a family and retired at an old age. You die a few years later! Good life!")

                elif fam == "b":
                    print("You died alone but still passed your wealth over to your favorite subordinate. Decent life!")

            elif talk == "b":
                print("You missed out on a big chance.\n The man was the CEO of a large labor company.\n You've become broke and are now homeless :(\n")
                print("A few days later, you gather your composure and think deeply about your future.\n You decide to pursue your dream of becoming a singer!\n")
                song = input("Think about your passion and create a name for your first song: \n")
                print("You begin practicing vocal skills and perform for passerbys.\n You get noticed by a famous recording company and sign a contract.\n")
                print("You record one song, and hope for the best. Woe and behold! In a few weeks, your song becomes a one-hit wonder!\n")
                print("Your song " + song + " has topped the music charts for 5 consecutive weeks!\n You use money for napkins!\n")
                family = input("Do you want to start a family? \n\ta) Yes \n\tb) No\n")
                if family == "a":
                    print("You married and had kids! At old age, you retire and die a few years later.\n Good life!")

                elif family == "b":
                    print("You retire and die alone a few years later.\n Oh well, Decent life!")


    elif YesAP == "b":
        print("Congratulations! You rank in the top 10\% of your graduating class!\n")
        PostSecSchool = input("Do you want to apply to \n\t a) A Name School \n\t b) A No Name School\n")
        if PostSecSchool == "a":
            print("You have been accepted to your dream Ivy League/ CA State School.\n You have also been offered multiple internships due to an outstanding resume\n")
            print("You get a job as the assistant of the president! Wonderful!\n")
            print("After four years, you run as president and successfully woo the masses to ascend to the president's position!\n")
            fam = input("Start a family? \n\ta) Yes \n\tb) No\n")
            if fam == "a":
                print("You live a nice life with your family and are remembered by all posterity as one of the world's presidents.\n Good life!")

            if fam == "b":
                print("You die alone after retiring from government work.\n But it's okay, your name is eternally in the ranks as a good president!")

        elif PostSecSchool == "b":
            print("You have been accepted to your dream Ivy League/ CA State School.\n You have also been offered multiple internships due to an outstanding resume\n")
            talk = input("You meet a man on the street, do you talk to him or not? \n\ta) Talk to him \n\tb) Do not talk to him.\n")
            if talk == "a":
                print("You've made connections and successfully gotten a job.\n")
                conflict = input("Your new boss scolds you for coming in late despite your protest about having to help an old man while commuting to work.\nDo you \n\ta) Plead for forgiveness or \n\tb) Argue back?\n")
                if conflict == "a":
                    print("Your boss forgives you and starts to like you!\n You're on your way to promotion!\n")
                elif conflict == "b":
                    print("Your boss gets angry, but is impressed with your guts.\n Your boss starts to like you! You're on your way to promotion! :)\n")
                fam = input("Because your boss favors you, you've inherited his position as CEO of the company after he retires!\n You're rich! Do you want to start a family? \n\ta) Yes \n\tb) No\n")
                if fam == "a":
                    print("You've started a family and retired at an old age. You die a few years later! Good life!\n")

                elif fam == "b":
                    print("You died alone but still passed your wealth over to your favorite subordinate. Decent life!\n")

            elif talk == "b":
                print("You missed out on a big chance.\n The man was the CEO of a large labor company.\n You've become broke and are now homeless :(\n")
                print("A few days later, you gather your composure and think deeply about your future.\n You decide to pursue your dream of becoming a singer!\n")
                song = input("Think about your passion and create a name for your first song: \n")
                print("You begin practicing vocal skills and perform for passerbys.\n You get noticed by a famous recording company and sign a contract.\n")
                print("You record one song, and hope for the best.\n Woe and behold! In a few weeks, your song becomes a one-hit wonder!\n")
                print("Your song " + song + " has topped the music charts for 5 consecutive weeks!\n You use money for napkins!\n")
                family = input("Do you want to start a family? \n\ta) Yes \n\tb) No\n")
                if family == "a":
                    print("You married and had kids! At old age, you retire and die a few years later.\n Good life!\n")

                elif family == "b":
                    print("You retire and die alone a few years later.\nOh well, Decent life!\n")

elif a == "b":
    NoAP = input("Would you want to have a job or invest time in extracurriculars? \n\t a) Job \n\t b) Extracurriculars\n")
    if NoAP == "a":
        print("You make enough to live off of")
        Money = input("Now do you want to \n\t a) Go to a 4 year Uni \n\t b) Write a book \n\t c) Drop a Mixtape\n")
        if Money == "a":
            print ("You have had a stressfull college experience but earned a degree\n")
            print("You get a job and life a nice life. We're lazy!\n")

        elif Money == "b":
            print("You have earned the Noble Prize for your book!\n")
            print("You receive concessions of millions of dollars for your contributions in the psychology field.\n You have enough to live until death. Nice life!\n")

        elif Money == "c":
            print ("You blew up! You now use money as napkins.\n")
            print("You overwork and get sick but it's okay your life insurance saves you and you live a nice life!\n")

    elif NoAP == "b":
        print("You have gotten a scholarship for your talent.\n")
        PostSecSchool = input("Do you want to apply to \n\t a) A Name School \n\t b) A No Name School\n")
        if PostSecSchool == "a":
            print("You have been accepted to your dream Ivy League/ CA State School.\n You have also been offered multiple internships due to an outstanding resume\n")
            print("You complete college one year later than expected! Yikes!\n")
            print("You found a job and climbed the rankings at a slow speed thanks to your previous talent.\n Your mom calls you to tell you she's incredibly proud of you!\n")
            #Start a family or not
            fam = input("You see an attractive human on the street. Talk to them? \n\ta) Talk to them \n\tb) Do not talk to them\n")
            if fam == "a":
                print("You've found your soulmate and started a family! You have/adopt kids and retire at old age. You die a few years later. Good life!\n")

            elif fam == "b":
                print("You die alone after retirement for being so anti-social, but your mom is still proud of you. Decent life!\n")

        elif PostSecSchool == "b":
            print("You have been accepted to your dream Ivy League/ CA State School.\n You have also been offered multiple internships due to an outstanding resume\n")
            talk = input("You meet a man on the street, do you talk to him or not? \n\ta) Talk to him \n\tb) Do not talk to him.\n")
            if talk == "a":
                print("You've made connections and successfully gotten a job.\n")
                conflict = input("Your new boss scolds you for coming in late despite your protest about having to help an old man while commuting to work.\nDo you \n\ta) Plead for forgiveness or \n\tb) Argue back?\n")
                if conflict == "a":
                    print("Your boss forgives you and starts to like you! You're on your way to promotion!\n")
                elif conflict == "b":
                    print("Your boss gets angry, but is impressed with your guts.\n Your boss starts to like you! You're on your way to promotion! :)\n")
                fam = input("Because your boss favors you, you've inherited his position as CEO of the company after he retires! You're rich! Do you want to start a family? \n\ta) Yes \n\tb) No\n")
                if fam == "a":
                    print("You've started a family and retired at an old age. You die a few years later! Good life!\n")

                elif fam == "b":
                    print("You died alone but still passed your wealth over to your favorite subordinate. Decent life!\n")

            elif talk == "b":
                print("You missed out on a big chance.\n The man was the CEO of a large labor company.\n You've become broke and are now homeless :(\n")
                print("A few days later, you gather your composure and think deeply about your future.\n You decide to pursue your dream of becoming a singer!\n")
                song = input("Think about your passion and create a name for your first song: \n")
                print("You begin practicing vocal skills and perform for passerbys.\n You get noticed by a famous recording company and sign a contract.\n")
                print("You record one song, and hope for the best.\n Woe and behold! In a few weeks, your song becomes a one-hit wonder!\n")
                print("Your song " + song + " has topped the music charts for 5 consecutive weeks!\n You use money for napkins!\n")
                family = input("Do you want to start a family? \n\ta) Yes \n\tb) No\n")
                if family == "a":
                    print("You married and had kids! At old age, you retire and die a few years later. Good life!\n")

                elif family == "b":
                    print("You retire and die alone a few years later.\n Oh well, Decent life!\n")
else:
    print("Invalid answer.")
