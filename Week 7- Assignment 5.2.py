largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        n=float(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest=n
    if n>largest:
        largest=n
    elif n<smallest:
        smallest=n
def done(largest,smallest):
    print("Maximum is",int(largest))
    print("Minimum is",int(smallest))
done(largest,smallest)
