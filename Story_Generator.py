import random as rd
name = ["Hamid", "Ali", "Hadi","Fatima","Jahan","Hasan","Jan"]
who = ["The Police Officer", "lawyer" , "journalist", "postman", "singer"]
palce_went = ['university','seminar', 'school', 'laundry', "Cafe", "Shop", "Hotel"]
when = ["last week", "yesterday", "few years ago",'Last night', 'A long time ago','On 20th Jan']
place = ["India","Iran","UK","USA","Germany"]
action = ['Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book','Plan for future']
print(rd.choice(when) + "," + rd.choice(who) + " that who live in " + rd.choice(place) + ", " + " went to the " + rd.choice(palce_went)+   "and "+ rd.choice(action))