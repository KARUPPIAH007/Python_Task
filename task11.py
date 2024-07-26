

def filtering(x,chars):


    for i in chars:
        if i in x:
            return False
   
    return True
def main():
 
    chars=[",",';']
    course=['','python','java',',,','angul;ar','php']
    print(list(filter(lambda x : filtering(x,chars) and x!='',course)))
 
if __name__ == "__main__":
    main()

