

n=input("PROJECT 3-INT 108 \n"
        "EMAIL SLICER \n"
        "NAME: Sayjan J. Singh \n"
        "REG.NO.: 12201529 \n"
        "Roll. No.:75\n"
        "press 1 to continue and any other key to exit \n ")
if n=='1':
    p=1
    l=[]
    r="@."
    while '@' in r and '.' in r:
        r=input('enter an email address:-')
        if p==1 and "@" not in r or '.' not in r:
            print("Please enter a valid email")
        p=p+1
        l.append(r)
    print('\n')
    for t in range(0,len(l)):
        if '@' in l[t]:
            for i in range(0,len(l[t])):
                if l[t][i]=='@':
                    s=len(l[t])
                    x=l[t][i+1:s+1]
                    x=x.upper()
                    print('username:',l[t][0:i],'and domain:',x)
                    break
    print("THANK YOU")

else:
    print("Terminating program....")






            
