a_dict=dict()
j=1
for i in range(len(strs)):
    temp=''.join(sorted(strs[i]))
    if temp not in a_dict:
        j=1
        a_dict[temp]=j
    else:
        j+=1
        a_dict[temp]=j
a_list=[""]*len(a_dict)
# print(a_list)
for i in range(len(strs)):
    temp=''.join(sorted(strs[i]))
    if temp not in a_dict:
        a_list[i]=strs[i]
    else:
        temp=a_list[i]
        a_list[i]=[temp, strs[i]]
print(a_list)