a = 2
b = 100
for i in range(a,b+1):
  for j in range(2,i):
    if i%j==0:
      break
  else:
    print(f"{i}",end=" ")  
    