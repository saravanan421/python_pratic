# Enter your code here. Read input from STDIN. Print output to STDOUT
def pattern(h,w):
    line='.|.'
    count=1
    for i in range(h):
        if i==h//2:
            lf=(w-6)//2
            print("".rjust(lf,"-")+"WELCOME"+"".ljust(lf,"-"))
        elif i<h//2:
            pos=(w-(count*3))//2

            print("".ljust(pos,'-')+line*count+"".rjust(pos,'-'))
            count+=2
        elif i>h//2:
            count-=2
            pos=(w-(count*3))//2
            print("".ljust(pos,'-')+line*count+"".rjust(pos,'-'))
        
            
if __name__=="__main__":
    h,w=input().strip().split()
    pattern(int(h),int(w))