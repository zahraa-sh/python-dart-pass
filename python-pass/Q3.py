class myNumber:
    def __init__(self):
        pass
    def checkNumbers(self):
        n=[]
        r = int(input("How many values do you want? "))
        for i in range (0,r):
          x= int(input(""))
          n.append(x) 

        for i in n:
            
            if ((i > 0) & (i <= 10)):
                if (i % 2 == 0):
                    print(i, " is even")
                else:
                    print(i, " is odd")

m = myNumber()
m.checkNumbers()
