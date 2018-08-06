class Cust:
    """cust app"""
    cbname="sbi"
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
    def __str__(self):
        return self.cname+" "+self.cadd+" "+str(self.cacno)+" "+str(self.cbal)+" "+Cust.cbname
c1=Cust("ravana","srilanka",1001,100000.00)
c2=Cust("sita","india",1002,1000.00)
c3=Cust("smith","dallas",1003,50000.00)
x=[c1,c2,c3]
for p in x:
    print(p)
x.sort(key=lambda c:c.cbal)
#for q in x:
 #   print(q)





