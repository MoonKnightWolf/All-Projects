# -*- coding: utf-8 -*-
"""chatbot

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ADYL9j26OByCXvAClLfmHKi4L2TgBQk3
"""

# !pip install Chatterbot

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Digi Hung")

conversation = {
    
    'hi there',
    'how are you?',
    'My name is Digi Hung',
    'How you feelin ?',
    'If you want to take a test to test you anxiety levels type: test ',
    'Hello'
    
}

trainer = ListTrainer(bot)

trainer.train(conversation)

#answer = bot.get_response("What is your name?")
#print(answer)
sum =0

while True:
  query=input()
  if query =='bye':
    print("bye")
    break
  if query =='test':
    print("Would you like to proceed to take the test? Enter your choice as y or n")
    flag = input()
    if flag == 'y':
      question = [ "How often have you been bothered by feeling nervous, anxious or on edge over the last two weeks?" , "How often have you been bothered by not being able to stop or control worrying over the last two weeks?" , "How often have you been bothered by worrying too much about different things over the last two weeks?" , "How often have you been troubled in relaxing in past two weeks?" , "How often have you been bothered by being so restless that it is hard to sit still over the last two weeks?" , "How often have you been bothered by becoming easily annoyed or irritable over the last two weeks?" , "How often have you been bothered by feeling afraid as if something awful might happen over the last two weeks?"]
      for x in question:
        print("\n")
        print(x)
        print("1 - Never \n2 - Sometimes \n3 - 50% of the times\n4 - Everyday")
        temp = input()
        temp = int(temp)
        sum = sum +temp -1
      if sum>=0 and sum<=7:
        print("Your score is:" , sum)
        print("It's okay to take a bit of stress it helps you improve your day-to-day life, as we can see as per your score you having a normal reaction to any tough situation")
        
        print("Cheers and bye-bye")
        break
      if sum >=8 and sum <=10:
        print("Your score is:" , sum)
        print("It's all right to take a bit of stress , mavbe you are goin through a stressful situation , and your mind is responding to it ")
        print("A general advice from me the great Digi-Hung would be following-\n")
        print("1. Meditation or midfullness you can take the help of \n2.")
        break     
      if sum >=11 and sum <=15:
        print("Your score is:" , sum)
        print(" Don't woory situation is not alarming yet, you can still help yourself a bit to go back in the common range.")
        break
      if sum >=15 and sum <=21:
        print("Your score is:" , sum)
        print(" Your score falls into the high range - anxiety has probably gotten in the way of you going to work, meeting friends, or doing the stuff that matters to you. This isn’t a diagnosis but it looks like it’s time to get help.")
        break
          
  answer = bot.get_response(query)
  print(answer)