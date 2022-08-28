import random
user_want = int(input("Enter the lenght of password: "))
charcters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

join_all = "".join(random.sample(charcters,user_want))
print(join_all)
