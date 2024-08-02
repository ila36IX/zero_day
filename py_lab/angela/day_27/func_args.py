def add(name,*numbers,end):
    return (name,sum(numbers),end)

add("Sum",2,5,8,end="The end")

def calc(a,b,**kwargs):
    print(kwargs["mult"],a*b)
    print(kwargs["add"],a+b)

calc(3,8,mult="Ha ddareb : ",add="Ha Ljame3 :",makayen="aliwa")
