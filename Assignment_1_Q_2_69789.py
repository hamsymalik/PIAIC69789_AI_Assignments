def custom_input(input_msg):
    while True:
        try:
            number = int(input(input_msg))
            if number>0 and number<101 and not(input_msg=="Enter Islamiat Marks: "):
                break
            elif number>0 and number<51 and input_msg=="Enter Islamiat Marks: ":
                break
                
            else:
                if input_msg=="Enter Islamiat Marks: ":
                    print("Enter marks in whole number between 0 and 50.")
                else:
                    print("Enter marks in whole number between 0 and 100.")
                continue
        except:
            if input_msg=="Enter Islamiat Marks: ":
                print("Enter marks in whole number between 0 and 50.")
            else:
                print("Enter marks in whole number between 0 and 100.")
    return number



name = input("Enter your name: ")

biology_marks = custom_input("Enter Biology Marks: ")
physics_marks = custom_input("Enter Physics Marks: ")
chemistry_marks = custom_input("Enter Chemistry Marks: ")
english_marks = custom_input("Enter English Marks: ")
urdu_marks = custom_input("Enter Urdu Marks: ")
islamiat_marks = custom_input("Enter Islamiat Marks: ")



total_marks = 100+100+100+100+100+50

obtained_marks=physics_marks + chemistry_marks + biology_marks + english_marks + urdu_marks + islamiat_marks
percentage = obtained_marks/total_marks
print("-------------------------------------------------")
print("\n\t\t\tDetailed Mark Certificate HSSC-I")
print("-------------------------------------------------")

print("Name: ", name)
print("Subject\t\t Obtained Marks\t\tTotal Marks")
print("Physics\t\t\t ",physics_marks, "\t\t 100")
print("Chemistry\t\t ",chemistry_marks,"\t\t 100")
print("Biology\t\t\t ", biology_marks, "\t\t 100")
print("English\t\t\t ", english_marks,"\t\t 100")
print("Urdu\t\t\t ",urdu_marks,"\t\t 100")
print("Islamiat\t\t ",islamiat_marks,"\t\t 50")
print("\nTOTAL\t\t",obtained_marks,"\t\t",total_marks)
print("\nPercentage: ",percentage*100)