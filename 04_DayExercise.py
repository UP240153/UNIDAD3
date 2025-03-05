T='Thirty'
D='Days'
l='Of'
P='Python'
space=' '
print(T+space+D+space+l+space+P)

c='Coding'
F='For'
A='All'
print(c+space+F+space+A)

company=c+space+F+space+A
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

pto= company[6:14]
print(pto)

print(company.index(c))

print(company.replace('Coding','Python'))     