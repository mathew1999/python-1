import pickle
a=[]
n=input("Enter no of strings: ")
fp=open("palindrome.txt","w")
fnp=open("npalindrome.txt","w")
for i in range(n):
	x=raw_input("Enter string: ")
 	if (x==x[::-1]):
  		a.append(pickle.dump(x,fp))
 	else:
  		a.append(pickle.dump(x,fnp))

fp.close()
fnp.close()

fp=open("palindrome.txt","r")
fnp=open("npalindrome.txt","r")
for i in fp.read():
	print i,
for i in fnp.read():
	print i,

fp.close()
fnp.close()
