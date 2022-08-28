email = input("Enter your Email Address: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print(f"Your username is {username } and your domain name is {domain_name}")