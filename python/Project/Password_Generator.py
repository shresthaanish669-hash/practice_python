import secrets

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}._.!@#$%&*"

all = lower + upper + numbers + symbols
length = 15

password = "".join(secrets.choice(all) for _ in range(length))
print("Password:", password)