year=int(input("Enter Year to be Checked leap or not:"))
if year%4==0:
    print("Leap Year")
elif (year%4==0) and (year%400==0):
    print("Leap Year")
elif (year%100==0) and (year%400==0):
    print("Leap Year")
else:
    print("Not a leap year")
