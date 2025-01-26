#Take the user Marks and Check whether the user are able to Admission in Collage Or Not 60 is minimum
marks = int(input("Enter your exam Marks: "))
if(marks < 60):
    print("Sorry! You cannot take admission, you need "+str(60-marks)+" numbers more to take admission")
else:
    print("Congratulation! You are Able to Take Admission in Collage")