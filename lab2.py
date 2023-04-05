name0 = input("введите слово: ")  
name = "" 
for x in range(0, len(name0) - 1): 
 if x != 2: 
 name = name + name0[x] 
print(name) 
if name.find("с") >= 0: 
 print("есть с") 
print(len(name0))