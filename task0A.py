for i in range(1,100):
  if i%3==0:
    print("Fizz",end=" ")
    continue
  elif i%5==0:
    print("BUZZ",end=" ")
    continue
  elif i%15==0:
    print("FizzBuzz",end=" ")
    continue
  print(i,end=" ")
