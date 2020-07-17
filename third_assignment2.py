Input = input()
s2 = sorted(Input)
for i in range(len(s2)):
    if('A'<= s2[i] and s2[i]<='Z'):
        x=i
        break
for i in range(len(s2)):
    if('a'<=s2[i] and s2[i]<='z'):
        y=i
        break
integer=s2[0:x]
Upper=s2[x:y]
Lower=s2[y:]
Odd =[i for i in integer if int(i)%2 ==1 ]
Even = [i for i in integer if int(i)%2 ==0 ]
print(''.join(Lower+Upper+Odd+Even))