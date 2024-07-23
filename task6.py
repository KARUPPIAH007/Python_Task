size= int(input("Enter number"))
 
def square_numbers(size):
    ans=[]
    for i in range(1,size+1):
        ans.append(i*i)
    print(ans)
if __name__=="__main__":
    square_numbers(size)