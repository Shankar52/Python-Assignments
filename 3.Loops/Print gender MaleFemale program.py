gender = input("Please enter your Gender : ")

if (gender == "M" or gender == "m" or gender == "Male" or gender == "male"):
    print("The gender in Male")
elif (gender == "F" or gender == "f" or gender == "FeMale" or gender == "female" or gender == "feMale" or gender == "female"):
    print("The gender is Female")
else:
    print("Please provide an appropriate format")
