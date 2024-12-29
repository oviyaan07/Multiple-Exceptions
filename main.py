try:
    num1,num2=eval(input("enter two numbers seperated by a comma(,) "))
    res=num1/num2
    print (res)
except ZeroDivisionError as e1:
    print("an error has occured ",e1)
except SyntaxError as e2:
    print("an error has occured ",e2)
except:
    print("an error has occured")
finally:
    print("this will execute no matter what :)")