#This is THYROID and DIABETES range detection for male and female

from prettytable import PrettyTable

x = PrettyTable(["Symptoms","Prevention"])

# This Table for HIGH LEVEL patients in male (Hyperthyroid)

x.add_row(["unexpected weight loss, even when food consumption and appetite remain unchanged","Radioiodine therapy"])
x.add_row(["irregular heartbeat","Surgery"])
x.add_row(["heart palpitations","Antithyroid medication"])
x.add_row(["nervousness","-"])
x.add_row(["irritability","-"])
x.add_row(["fatigue","-"])
x.add_row(["tremor (usually trembling of the fingers and hands)","-"])
x.add_row(["sweating","-"])
x.add_row(["increased sensitivity to heat and/or cold","-"])
x.add_row(["more frequent bowel movements","-"])
x.add_row(["muscle weakness","-"])
x.add_row(["hair thinning","-"])

# This Table for LOW LEVEL patients in male (Hypothyroid)

y = PrettyTable(["Symptoms", "Prevention"])

y.add_row(["Fatigue","Surgery"])
y.add_row(["Increased sensitivity to cold","Radioiodine therapy"])
y.add_row(["Constipation","Antithyroid medication"])
y.add_row(["Dry skin","-"])
y.add_row(["Weight gain","-"])
y.add_row(["Puffy face","-"])
y.add_row(["Hoarseness","-"])
y.add_row(["Muscle weakness","-"])
y.add_row(["Elevated blood cholesterol level","-"])
y.add_row(["Muscle aches, tenderness and stiffness","-"])
y.add_row(["Pain, stiffness or swelling in your joints","-"])
y.add_row(["Heavier than normal or irregular menstrual periods","-"])
y.add_row(["Thinning hair","-"])
y.add_row(["Slowed heart rate","-"])
y.add_row(["Depression","-"])
y.add_row(["Impaired memory","-"])
y.add_row(["Enlarged thyroid gland (goiter)","-"])


# This table for HIGH SUGAR LEVEL patients (Hyperglycemia)

h = PrettyTable(["Symptoms", "Prevention"])

h.add_row(["Fatigue","Follow your meal plan"])
h.add_row(["Frequent urination","Keep an eye on your blood sugar level"])
h.add_row(["Increased thirst","Take your medication as directed"])
h.add_row(["Nausea and vomiting","Have a sick-day plan"])
h.add_row(["Shortness of breath","Check for ketones when your blood sugar is high"])
h.add_row(["Stomach pain","Have glucagon and fast-acting sources of sugar available"])
h.add_row(["Fruity breath odor","Consider a continuous glucose monitor (CGM)"])
h.add_row(["A very dry mouth","Drink alcohol with caution"])
h.add_row(["A rapid heartbeat","Educate your loved ones, friends and co-workers"])
h.add_row(["-","Wear a medical ID bracelet or necklace"])


# This table for LOW SUGAR LEVEL patients (hypoglycemia)

l = PrettyTable(["Symptoms", "Prevention"])

l.add_row(["Fatigue","Follow your meal plan"])
l.add_row(["Shakiness or nervousness","Keep an eye on your blood sugar level"])
l.add_row(["Anxiety","Take your medication as directed"])
l.add_row(["Weakness","Have a sick-day plan"])
l.add_row(["Sweating","Check for ketones when your blood sugar is high"])
l.add_row(["Hunger","Have glucagon and fast-acting sources of sugar available"])
l.add_row(["Nausea","Consider a continuous glucose monitor (CGM)"])
l.add_row(["Dizziness or lightheadedness","Drink alcohol with caution"])
l.add_row(["Difficulty speaking","Educate your loved ones, friends and co-workers"])
l.add_row(["Confusion","Wear a medical ID bracelet or necklace"])


#   Main Coding

print("Are you a male or female:\n1: Select M or m  for male\n2: Select F or f for female\n")

a = input("ANS:- ") 

age = int(input("Please enter your age:- "))

if a =='M' or a == 'm':
    
    print("You select Male, Thank you for your response! Please select your Disease\n")
    print("\n1: Select T or t for Thyroid\n2: Select D or d for Diabetes")
    disease = input("ANS:- ")

    if  age in range(18, 50):
        if disease == 'D' or disease == 'd':
            fasting = input("\nPlease enter your categaory - Fasting or not (Y/N)\n")
            print("\nPlease enter your given range\n") 
            BS_level = float(input("Enter your Blood Sugar level:- "))

            if fasting == "Y" or fasting == "y":
                if BS_level <70:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                elif BS_level in range (70, 100):
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (101, 125):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >126:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)

            elif fasting == "N" or fasting == "n":
                if BS_level <90:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level < 140:
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (140, 200):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >200:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")                    
                    print(h)
            else:
                print("\n\n Sorry you entered wrong entities\n")


        if disease == 'T' or disease == 't':
            print("\nPlease enter your given range\n")
            TSH_level = float(input("Enter your TSH level:- "))

            if TSH_level <= 0.5:
                print("\nYour TSH level is low", TSH_level, "mlU/L""\n")
                print(y)
            elif TSH_level >= 4.5:
                print ("\nYour TSH level is High", TSH_level ,"mlU/L""\n")
                print(x)
            else:
                print ("\nYour TSH level is Normal", TSH_level , "mlU/L""\n")


    elif  age in range(50, 71):
        if disease == 'T' or disease == 't':
            print("\nPlease enter your given range\n")
            TSH_level = float(input("Enter your TSH level:- "))

            if TSH_level <= 0.5:
                print("\nYour TSH level is low", TSH_level, "mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(y)
       
            elif TSH_level >= 4.6:
                print ("\nYour TSH level is High", TSH_level ,"mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(x)

            else:
                print ("\nYour TSH level is Normal", TSH_level , "mlU/L""\n")

        if disease == 'D' or disease == 'd':
            fasting = input("\nPlease enter your categaory - Fasting or not (Y/N)\n")
            print("\nPlease enter your given range\n") 
            BS_level = float(input("Enter your Blood Sugar level:- "))

            if fasting == "Y" or fasting == "y":
                if BS_level <70:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level in range (70, 100):
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (101, 125):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >126:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)

            elif fasting == "N" or fasting == "n":
                if BS_level <90:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level < 140:
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (140, 200):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >200:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)               

            else:
                print("\n\n Sorry you entered wrong entities\n")

    elif  age in range(71, 91):
        if disease == 'T' or disease == 't':
            print("\nPlease enter your given range\n")
            TSH_level = float(input("Enter your TSH level:- "))

            if TSH_level <= 0.4:
                print("\nYour TSH level is low", TSH_level, "mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(y)
            elif TSH_level >= 5.5:
                print ("\nYour TSH level is High", TSH_level ,"mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(x)

            else:
                print ("\nYour TSH level is Normal", TSH_level , "mlU/L""\n")

        if disease == 'D' or disease == 'd':
            fasting = input("\nPlease enter your categaory - Fasting or not (Y/N)\n")
            print("\nPlease enter your given range\n") 
            BS_level = float(input("Enter your Blood Sugar level:- "))

            if fasting == "Y" or fasting == "y":
                if BS_level <70:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level in range (70, 100):
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (101, 125):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >126:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)

            elif fasting == "N" or fasting == "n":
                if BS_level <90:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level < 140:
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (140, 200):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >200:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)                    

            else:
                print("\n\n Sorry you entered wrong entities\n")
        

elif a == 'F' or a == 'f':
    print("\nYou select Female, Thank you for your response! Please select your Disease\n")
    print("\n1: Select T or t for Thyroid\n2: Select D or d for Diabetes")
    disease = input("ANS:- ")
    if  age in range(18, 30):
        if disease == 'T' or disease == 't':
            print("\nPlease enter your given range\n")
            TSH_level = float(input("Enter your TSH level:- "))

            if TSH_level <= 0.4:
                print("\nYour TSH level is low", TSH_level, "mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(y)
            elif TSH_level >= 4.5:
                print ("\nYour TSH level is High", TSH_level ,"mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(x)

            else:
                print ("\nYour TSH level is Normal", TSH_level , "mlU/L""\n")

        if disease == 'D' or disease == 'd':
            fasting = input("\nPlease enter your categaory - Fasting or not (Y/N)\n")
            print("\nPlease enter your given range\n") 
            BS_level = float(input("Enter your Blood Sugar level:- "))

            if fasting == "Y" or fasting == "y":
                if BS_level <70:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level in range (70, 100):
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (101, 125):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >126:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)

            elif fasting == "N" or fasting == "n":
                if BS_level <90:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level < 140:
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (140, 200):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >200:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)                    

            else:
                print("\n\n Sorry you entered wrong entities\n")




    elif  age in range(30, 50):
        if disease == 'T' or disease == 't':
            print("\nPlease enter your given range\n")
            TSH_level = float(input("Enter your TSH level:- "))

            if TSH_level <= 0.4:
                print("\nYour TSH level is low", TSH_level, "mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(y)
            elif TSH_level >= 4.1:
                print ("\nYour TSH level is High", TSH_level ,"mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(x)

            else:
                print ("\nYour TSH level is Normal", TSH_level , "mlU/L""\n")

        if disease == 'D' or disease == 'd':
            fasting = input("\nPlease enter your categaory - Fasting or not (Y/N)\n")
            print("\nPlease enter your given range\n") 
            BS_level = float(input("Enter your Blood Sugar level:- "))

            if fasting == "Y" or fasting == "y":
                if BS_level <70:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level in range (70, 100):
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (101, 125):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >126:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)

            elif fasting == "N" or fasting == "n":
                if BS_level <90:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level < 140:
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (140, 200):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >200:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)                    

            else:
                print("\n\n Sorry you entered wrong entities\n")

    elif  age in range(50, 80):

        if disease == 'T' or disease == 't':
            print("\nPlease enter your given range\n")
            TSH_level = float(input("Enter your TSH level:- "))

            if TSH_level <= 0.46:
                print("\nYour TSH level is low", TSH_level, "mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(y)
            elif TSH_level in range (4.7, 7.0):
                print ("\nYour TSH level is High", TSH_level ,"mlU/L\n\n(It's must be between <0.5 - >4.5)""\n")
                print(x)

            else:
                print ("\nYour TSH level is Normal", TSH_level , "mlU/L""\n")

        if disease == 'D' or disease == 'd':
            fasting = input("\nPlease enter your categaory - Fasting or not (Y/N)\n")
            print("\nPlease enter your given range\n") 
            BS_level = float(input("Enter your Blood Sugar level:- "))

            if fasting == "Y" or fasting == "y":
                if BS_level <70:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level in range (70, 100):
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (101, 125):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >126:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)

            elif fasting == "N" or fasting == "n":
                if BS_level <90:
                    print("\n Your Blood Sugar Level is low\n")
                    print(l)
                if BS_level < 140:
                    print("\n Your Blood Sugar Level is Normal\n")
                elif BS_level in range (140, 200):
                    print("\n Your Blood Sugar Level is between Pre-diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)
                elif BS_level >200:
                    print("\n Your Blood Sugar Level is Diabetes, you need a consultant", BS_level,"mg/dL""\n")
                    print(h)                    

            else:
                print("\n\n Sorry you entered wrong entities\n")

else:
    print("\nSorry, you entered wrong input Please try again later!")