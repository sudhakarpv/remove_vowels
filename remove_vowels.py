# remove_vowels
def main():
    pass
    n=input()
    inp=input().title()
    list_1=list(inp)
    for i in inp:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            list_1.remove(i)
    print(''.join(list_1[::-1]))
if __name__ == '__main__':
    main()
