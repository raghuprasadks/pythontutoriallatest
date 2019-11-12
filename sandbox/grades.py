# -*- coding: utf-8 -*-
name = input("Enter name")
tut_score = int(input("Enter tutorial marks"))
t_score = int(input("Enter test marks"))
f_score = 0
avg = (tut_score+t_score)/2
if (avg < 40):
    print ('You are not eligibal for final exams')
else:
    f_score = int(input("Enter final  marks"))

c_marks = tut_score*.25 + t_score*.25 + f_score *.5
print('Calculated marks ',c_marks)
if (c_marks >= 80 and c_marks <=100):
    print ('Grade A')
elif (c_marks >= 70 and c_marks <80):
    print ('Grade B')
elif (c_marks >= 60 and c_marks <70):
    print ('Grade C')
elif (c_marks >= 50 and c_marks <60):
    print ('Grade D')
else:
    print('Grade E')
    


