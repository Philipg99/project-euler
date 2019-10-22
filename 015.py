#40C20

def fact(n):
  f=1
  while n>1:
    f*=n
    n-=1
  return f

print(fact(40)//(fact(40-20)*fact(20)))
