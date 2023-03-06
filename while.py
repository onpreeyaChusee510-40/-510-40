weight = int(input("Enter Your Weight"))
height = int(input("Enter Your Height"))
BMI = (weight/(height*height))
if (BMI<18.5):
    print("BMI is", BMI)
    print("Unerweight")
elif(BMI<25):
    print ("BHI is",BMI)
    print ("Normal weigh")
elif(BMI <30):
    print ("BMI 1", BMI)
    print ("Over weigh")
else:
    print ("BMI 1", BMI)
    print ("Obesity")
                          
                                                                                                                                                                                        
