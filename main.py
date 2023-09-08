def fact_rect(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rect(n-1)
number=int(input ('Enter the Factorial number in int ')) 
result=int(fact_rect(number)) 
print("The Factorial of {} is {}".format(number,result))