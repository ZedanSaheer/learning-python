import re

email = input("What is your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.com$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")