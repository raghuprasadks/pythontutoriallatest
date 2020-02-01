roll=int(input("Enter your roll number"))
tut=float(input("Enter tutorial marks"))
test=float(input("input test marks"))
avg=(tut+test)/2
if avg<40:
    print("Grade F")
else:
    end=float(input("Enter end exam marks"))
    total=(tut/4)+(test/4)+(end/2)
    if 80<=total<=100:
        print("Grade A")
    elif 70<=total<80:
        print("Grade B")
    elif 60<=total<70:
        print("grade c")
    elif 50<=total<60:
        print("Grade d")
    else:
        print("Grade e")