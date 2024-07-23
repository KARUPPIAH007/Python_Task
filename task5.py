def Char(character):
    if   "a" <= character <= 'z' or "A" <= character <= 'Z' or "0" <= character <= '9':
        return f"{character} You Enter Character"
    else:
        return f"{character} Enter The Special Character"

def main():
    print(Char(input("Enter the character:")))

if __name__ == "__main__":
    main()