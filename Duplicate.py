import os

def main():
    filename1=input("Enter file name 1:")
    filename2=input("Enter file name 2:")
    filename_1=open(filename1,'r')
    filename_2=open(filename2,'r')

    if filename_1.read()==filename_2.read():
        filename_1.close()
        filename_2.close()
        os.remove(filename2)
        print('File Deleted Successfuly')
    
if __name__=="__main__":
    main()