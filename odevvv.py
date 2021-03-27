number1=int(input("Enter a number1: \n"))
number2=int(input("Enter a number2: \n"))
result1=int(0)
result2=int(1)
if str(number1)[0]==str(number1)[2] and str(number2)[0]==str(number2)[2]:
    result1=(int(number1)+int(number2))
    print("The result of addition:\n",result1)
elif str(number1)[0]==str(number1)[2] or str(number2)[0]==str(number2)[2]:
    if int(number1)>int(number2):
        result1=int(number1)-int(number2)
    else:
        result1=int(number2)-int(number1)
    print("The result of subtraction:\n",result1) 
else:
    result2=int(number1)*int(number2)
    print("Result of multiplication:\n ",result2)
''' ya da sadece 3 değil x basamaklı sayı da olsa da int-str dönüşümü yapıldıktan sonra stringin 0 ve son karakterini karşılamak yeterli'''