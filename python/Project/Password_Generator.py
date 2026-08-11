import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}._.!@#$%&*"

all = lower + upper + numbers + symbols
length = int(input("Enter password Length: "))

password = "".join(secrets.choice(all) for _ in range(length))
print("Password:", password)