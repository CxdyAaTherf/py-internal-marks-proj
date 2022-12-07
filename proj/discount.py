# Whether the person will get a discount or not (if the total price is greater than or equal to 10,000 the person will get a 10% discount)

sp = float(input("Enter the selling price: "))
oh = float(input("Enter the overhead ( if any, otherwise enter 0 ): "))
mp = sp + oh

if mp < 10000:
    final = mp
    print(f"You will not get a discount. Your final cost is {final}")
elif mp >= 10000:
    final = (mp * (100 - 10))/100
    print(f"You will get a discount of 10%. Your final cost is {final}")
else:
    print("hi?")