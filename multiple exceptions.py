try:
    num1,num2 =eval(input("please enter two numbers seperated by a comma"))
    result=num1/num2
    print("result is ",result)

except ZeroDivisionError:
    print("division by 0 is error!")    

except SyntaxError:
    print("please seperate your number with a comma like this: 1,2")    
except:
    print("wrong input")
else:
    print("no exceptions!")
finally:
    print("this will excute every time, no matter what!")
