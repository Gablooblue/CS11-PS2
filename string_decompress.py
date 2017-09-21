n = int(input())

s = [] #Initialize an empty list
for i in range(n):
    s.append(input())
    
for i in range(n):
    a = s[i]
    for j in range(len(a)):
        character = a[j]
        #Checking if it's a character
        if ord(character) > 57: 
            next_char = j+1
            if next_char < len(a):
                if  48 <= ord(a[next_char]) < 57:
                    for repeats in range(int(a[next_char])):
                        print(character, end= "")
                else:
                    print(character, end="")
            else:
                print(character, end = "")
    print()
