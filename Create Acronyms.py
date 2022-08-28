user_in = str(input("Enter A Phrase: "))
split_text = user_in.split()

#using for loop
n = " "
for i in split_text:
    n = n + i[0].upper()

print(n)


