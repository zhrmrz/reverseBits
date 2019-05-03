class Sol:
    def reverseBits(self,n):
        reverse=0
        bit=31
        c=0
        while n>0:
            if n%2==1:
                reverse+=2**bit
            bit-=1
            n//=2
            c+=1
        return c
if __name__ == '__main__':
    a=int(input("Enter a number"))
    p1=Sol()
    print(p1.reverseBits(a))



