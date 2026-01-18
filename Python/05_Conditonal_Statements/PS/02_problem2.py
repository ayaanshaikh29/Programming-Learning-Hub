subject1 = int(input("Enter marks of this subject: "))
subject2 = int(input("Enter marks of this subject: "))
subject3 = int(input("Enter marks of this subject: "))

#calculate the total percentage of student
total_percentage = ((subject1 + subject2 + subject3)*100)/300

if(total_percentage>40 and subject1>=33 and subject2>=33 and subject3>=33):
    print("Congratulations!! You are passed and you scored:",total_percentage)

else:
    print("You are failed, try harder next time:",total_percentage)
