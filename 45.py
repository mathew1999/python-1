stock={}
n=input("Number of items: ")
for i in range(1,n+1,1):
 b=raw_input("Name of items: ")
 stock[b]=input("Number of items: ") 
print stock

x1=raw_input("Enter the item to be deleted: ")
del stock[x1]
print stock

x2=raw_input("Enter new item: ")
stock[x2]=input("Number of item: ")
print stock

for k,v in stock.items():
 print k,v

