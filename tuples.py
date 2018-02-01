someTuple = ("Doron",45,(("Vered",22),("Dona",47)))
a,b,c = someTuple
print(a)
print(b)
print(c)

d,e=c
print(d)
print(e)

f,g = e
print(f)
print(g)

print('')
for item in c:
    print(item[0] )