from prettytable import PrettyTable

x = PrettyTable(["Symptoms","Prevention"])


print ("\nThis table for HIGH THYROID LEVEL patients (Hyperthyroid)\n")

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

print(x)


print ("\nThis table for LOW THYROID LEVEL patients (Hypothyroid)\n")

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

print(y)


print ("\nThis table for HIGH SUGAR LEVEL patients (Hyperglycemia)\n")

l = PrettyTable(["Symptoms", "Prevention"])

l.add_row(["Fatigue","Follow your meal plan"])
l.add_row(["Frequent urination","Keep an eye on your blood sugar level"])
l.add_row(["Increased thirst","Take your medication as directed"])
l.add_row(["Nausea and vomiting","Have a sick-day plan"])
l.add_row(["Shortness of breath","Check for ketones when your blood sugar is high"])
l.add_row(["Stomach pain","Have glucagon and fast-acting sources of sugar available"])
l.add_row(["Fruity breath odor","Consider a continuous glucose monitor (CGM)"])
l.add_row(["A very dry mouth","Drink alcohol with caution"])
l.add_row(["A rapid heartbeat","Educate your loved ones, friends and co-workers"])
l.add_row(["-","Wear a medical ID bracelet or necklace"])

print (l)


print("\nThis table for LOW SUGAR LEVEL patients (hypoglycemia)\n")

m = PrettyTable(["Symptoms", "Prevention"])

m.add_row(["Fatigue","Follow your meal plan"])
m.add_row(["Shakiness or nervousness","Keep an eye on your blood sugar level"])
m.add_row(["Anxiety","Take your medication as directed"])
m.add_row(["Weakness","Have a sick-day plan"])
m.add_row(["Sweating","Check for ketones when your blood sugar is high"])
m.add_row(["Hunger","Have glucagon and fast-acting sources of sugar available"])
m.add_row(["Nausea","Consider a continuous glucose monitor (CGM)"])
m.add_row(["Dizziness or lightheadedness","Drink alcohol with caution"])
m.add_row(["Difficulty speaking","Educate your loved ones, friends and co-workers"])
m.add_row(["Confusion","Wear a medical ID bracelet or necklace"])

print(m)