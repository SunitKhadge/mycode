#!usr/bin/env python3

name=input("What is your name? ")

age = input("How old are you: a (<18), b (18-39), c (40-65), d (>65)?" )

age_cat = ['a','b','c','d']

if age not in age_cat:
    print ('Please specify one of the age categories provided: a, b, c or d ?')
favcolor= input("What is your favorite color: green, yellow, red, blue ?" )

morningdrink=input("What do you drink for breakfast: tea, coffee ?")

h2o= int(input("How many litres of water do you drink?") )

veggies =['brussel sprouts','kale','spinach', 'green peas','lettuce', 'broccoli','cauliflower','potato','sweet potatoes', 'carrot','pumpkin', 'squash','beet','radish','tomato', 'red pepper','turnip', 'onion','cabbage','okra','mushroom', 'celery','yam', 'gourd', 'parsnip','kale','chives','artichoke','bok choy','napa cabbage','swiss chard', 'green beans', 'cucumbers', 'mustard greens','corn', 'butter lettuce', 'tomatillo','eggplant', 'zucchini','olive','bamboo shoot', 'dill', 'cilantro','black eyes peas','shitaki mushroom','fennel','leeks','rhubarb' ]

if age=="a":
    veggie= veggies[0:15]
elif age=="b":
    veggie=veggies[16:31]
elif age=="c":
    veggie=veggies[32:47]
elif age=="d":
    veggie=veggies[24-39]

if favcolor=="green":
    veggie = veggie[0:3]
elif  favcolor=="yellow":
    veggie = veggie[4:7]
elif favcolor=="red":
    veggie=veggie[8:11]
elif favcolor=="blue":
    veggie=veggie[12:15]

if morningdrink=="tea":
    veggie=veggie[0:1]    
elif mornigdrink=="coffee":            
    veggie=veggie[2:3]        

if h2o<=2:
    print(f"{name}, your favorite vegetable is {veggie[0]}")
else:
    print (f"{name}, your favorite vegetabe is {veggie[1]}")


