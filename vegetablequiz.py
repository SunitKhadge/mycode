#!usr/bin/env python3

name=input("What is your name? ")

age_cat = ['a','b','c','d']
age =""
while True:
     
    age = input("How old are you: a (<18), b (18-39), c (40-65), d (>65)?" )
    
    if age in age_cat:
        break
    
while True:
    favcolor= input("What is your favorite color: green, yellow, red, blue ?" )
    if favcolor in ['green', 'yellow' , 'red', 'blue']:
        break

while True:
    morningdrink=input("What do you drink for breakfast: tea, coffee ?")
    if morningdrink in ['tea','coffee']:
        break


while True: 
    h2o= int(input("How many litres of water do you drink?") )
    if h2o>0:
        break
    
    

veggies =['brussel sprouts','kale','spinach', 'green peas','lettuce', 'broccoli','cauliflower','potato','sweet potatoes', 'carrot','pumpkin', 'squash','beet','radish','tomato', 'red pepper','turnip', 'onion','cabbage','okra','mushroom', 'celery','yam', 'gourd', 'parsnip','kale','chives','artichoke','bok choy','napa cabbage','swiss chard', 'green beans', 'cucumbers', 'mustard greens','corn', 'butter lettuce', 'tomatillo','eggplant', 'zucchini','olive','bamboo shoot', 'dill', 'cilantro','black eyes peas','shitaki mushroom','fennel','leeks','rhubarb', 'lotus']


if age=="a":
    veggie= veggies[0:16]
elif age=="b":
    veggie=veggies[16:32]
elif age=="c":
    veggie=veggies[32:48]
elif age=="d":
    veggie=veggies[25-41]

if favcolor=="green":
    veggie = veggie[0:4]
elif  favcolor=="yellow":
    veggie = veggie[4:8]
elif favcolor=="red":
    veggie=veggie[8:12]
elif favcolor=="blue":
    veggie=veggie[12:16]
if morningdrink=="tea":
    veggie=veggie[0:2]    
elif morningdrink=="coffee":            
    veggie=veggie[2:4]       

if h2o < 2:
    #print(veggie)
    print(f"{name}, your favorite vegetable is {veggie[0]}. \n I recommend trying {veggie[1]} if you have not already.")
    print("P.S. You need to drink more water.") 
else:
    #print(veggie)
    print (f"{name}, your favorite vegetabe is {veggie[1]} \n I recommend trying {veggie[0]} if you have not already.")



