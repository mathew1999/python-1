rollcal={}
n=input("Number of elements :")
for i in range(1,n+1,1):
 b=input("Enter roll no: ")
 rollcal[b]=raw_input("Enter your Name :")
print rollcal

x1=input("Enter roll no: ")
for i in rollcal:
 if (i==x1):
  x2=raw_input("Name to be replaced with: ")
  rollcal[x1]=x2
print rollcal

x3=raw_input("Enter Name: ")
for k,v in rollcal.items():
 if(v==x3): 
  print k,v 


print sorted (rollcal.values())

x5=input("Enter roll no to be deleted: ")
for k,v in rollcal.items():
  if (k==x5):
   del rollcal[k]
print rollcal
