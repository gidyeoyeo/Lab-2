def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight / (height*height)
    print("bmi = "+ str(bmi))  
    if bmi<18.5:
        print("under weight")
    elif bmi >25.0:
        print("over weight")
    else:
        print("NOrmal weight")
calculate_bmi(weight=57, height=1.73)