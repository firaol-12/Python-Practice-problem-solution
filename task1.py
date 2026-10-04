data = input("enter text:")

result = ""
for i in data:
    if i.islower():
        result +=i.upper()
    else:
        result +=i.lower()

print(result)
