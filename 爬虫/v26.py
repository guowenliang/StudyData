import re



pattern = re.compile(r'\d+')

s = pattern.findall("I am 18 years old and 1111 cm")

print(s)

s = pattern.finditer("I am 18 years old and 1111 cm")

print(type(s))
for i in s:
    print(i.group())