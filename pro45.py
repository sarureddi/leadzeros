m1=input()
if m1==m1[::-1]:
    print("yes")
else:
    value=m1.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=m1.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
