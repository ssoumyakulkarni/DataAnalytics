import string
set1={"Bangalore","Munbai","Chaina","123","456","Bangalore123","8473","Munbai123","Chaina345","!@#","()*&*(&%^","Soumya kulkarni"}
setalpha=set()
setnum=set()
setspchar=set()
setalphnum=set()
remove = string.whitespace
dict={}
ls1=[]
ls2=[]
ls3=[]
ls4=[]

for j in set1: 
	if(j.isdigit()):
		setnum.add(j)
		ls1.append(j)
	elif(j.translate(None, remove).isalpha()):
		setalpha.add(j)
		ls2.append(j)
	elif(j.isalnum()):
		setalphnum.add(j)
		ls3.append(j)
	else:
		setspchar.add(j)
		ls4.append(j)
print("list of digits",ls1)
print("list of digits",ls2)
print("list of digits",ls3)
print("list of digits",ls4)

print("Original Set is : ",set1)		
print("\n")		
print("Numerical Set is : ",setnum)
print("Alphabetical Set is : ",setalpha)
print("AlphaNumberic Set is : ",setalphnum)
print("Special Charecter Set is : ",setspchar)

dict["Digits"]=ls1
dict["Alphabets"]=ls2
dict["Alphanumeric"]=ls3
dict["Special_Charects"]=ls4
print(dict)

import json
with open('data.json', 'w') as f:
    json.dump(dict, f,indent=4)
	

