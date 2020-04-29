hrs=input("Enter Hours:")
h=float(hrs)
rate=input("Enter rph")
r=float(rate)
if h<=40:
    pay=h*r
elif h>40:
    pay=40*r + (h-40)*1.5*r
else:
    print("WRONG PARAMETER")
print(pay)
