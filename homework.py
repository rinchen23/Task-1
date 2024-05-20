age = int(input("Enter your age:"))
student = input("Are you student(yes/no):")
if (age<=12) or (age>=13 and age<=18 and student=='yes'):
    print("Yor are eligible for discount on the movie ticket")
else:
    print("You are not eligible for discount on the movie ticket")