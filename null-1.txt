print("Finding factorial of a number")
print("*****")
n=int(input("Enter the number of find the factorial:"))


def fact(k):
  if k==0.or k==1:
    return 1
  elif (k>1):
     return k * fact(k-1)
  else:
    return 0


print ("the factorial number is :",fact(n))