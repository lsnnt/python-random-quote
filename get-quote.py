import random
f = open("quotes.txt")
quotes = f.readlines()
f.close()
last = 13
rnd = random.randint(0, last)
name = "code by nityanand thakur."
print(quotes[rnd])
print(name.title())
