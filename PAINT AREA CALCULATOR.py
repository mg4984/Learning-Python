import math
def can_use(height,width,cover):
    area= height*width
    cansreq=math.ceil(area/cover)
    print("YOU WILL NEED",cansreq,"CANS")
a=int(input("HEIGHT: "))
b=int(input("width: "))
coverage=5  
can_use(height=a,width=b,cover=coverage)
