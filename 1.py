print"Welcome to AVM Air-Ticket Booking Centre(Kochi-Mumbai, Mumbai-Kochi)"
a={}
n=input("Enter number of passengers: ")
if n ==0:
  print"Wrong Choice due to number of passenger"
else:
 for i in range (1,n+1,1):
     b=raw_input("Enter name and gender of passenger(Name,Gender): ")
     a[b]=input("Enter age of passenger: ")
 print "Passenger details are:",a   
 print"Mumbai - Kochi Flight Details - 1)0600, 2)0700,3)1800"
 print"Kochi - Mumbai Flight Details - 4)0600, 5)0700,6)1800" 
 x1=raw_input("Enter place of departure: ")
 x2=raw_input("Enter destination: ")
 o=input("Enter your choice of flight time: ")
 q=raw_input("Enter date of journey(dd/mm/yy):")
 if len(q)==6 and((o==1) or (o==2) or (o==3) or (o==4) or (o==5) or (o==6)):
  print a,"from",x1,"to",x2,"on",q

  
  print"Choose your class"
  print"1)1st Class"
  print"2)Business"
  print"3)Economy"
  x9=input("Enter choice: ")

  if (x9==1):
   print ("Choose your seat type: ")
   print "1) Window-2000 rupees"
   print "2) Middle-1750 rupees"
   print "3) Aisle-1500 rupees"
   x3=input("Choose your option: ")
   x4=len(a)
   if (x3==1):
      y1=x4*2000
      print "total price is ",y1
   elif(x3==2):
      y2=x4*1750
      print "total price is ",y2
   elif(x3==3):
      y3=x4*1500
      print "total price is ",y3
   else:
      print"Wrong option due to type of seat selection"
   if(x3==1 or x3==2 or x3==3):  
     print "Choose method of pay"  
     print "1) Credit card"
     print "2) Debit card"
     print "3) PayTm"
     print "4) Netbanking"  
     x7=input("Enter your option: ")
     if (x7==1):
      n3=raw_input("Cardholders name: ")
      n4=input("Date of expiry(mmyyyy): ")
      n5=input("CVV number: ")
      n6=input("Enter mobile number: ")
      n7=input("Enter OTP: ")
      print"Payment is getting processed by Bank"
     elif(x7==2):
      m3=raw_input("Cardholder's name: ")
      m4=input("Date of expiry(mmyyyy): ")
      m5=input("CVV number: ")
      m6=input("Enter mobile number: ")
      m7=input("Enter OTP: ")
      print"Payment is getting processed by Bank"
     elif(x7==3):
      o3=raw_input("Name: ")
      o4=input("Mobile number: ")
      o5=input("Enter OTP: ")
      print"Payment is getting processed by Bank"
     elif(x7==4):
      x8=input("Enter Customer id: ")
      t1=input("Enter OTP: ")
      print"Payment is getting processed by Bank"
     else:
      print "Wrong choice due to payment mode selection"  

  elif (x9==2):
   print ("Choose your seat type: ")
   print "1) Window-1500 rupees"
   print "2) Middle-1250 rupees"
   print "3) Aisle-1000 rupees"
   x3=input("Choose your option: ")
   x4=len(a)
   if (x3==1):
     y1=x4*1500
     print "total price is ",y1
   elif(x3==2):
     y2=x4*1250
     print "total price is ",y2
   elif(x3==3):
     y3=x4*1000
     print "total price is ",y3
   else:
     print"Wrong option due to type of seat selection"
   if(x3==1 or x3==2 or x3==3):  
    print "Choose method of pay"  
    print "1) Credit card"
    print "2) Debit card"
    print "3) PayTm"
    print "4) Netbanking"  
    x7=input("Enter your option: ")
    if (x7==1):
     n3=raw_input("Cardholders name: ")
     n4=input("Date of expiry(mmyyyy): ")
     n5=input("CVV number: ")
     n6=input("Enter mobile number: ")
     n7=input("Enter OTP: ")
     print"Payment is getting processed by Bank"
    elif(x7==2):
     m3=raw_input("Cardholder's name: ")
     m4=input("Date of expiry(mmyyyy): ")
     m5=input("CVV number: ")
     m6=input("Enter mobile number: ")
     m7=input("Enter OTP: ")
     print"Payment is getting processed by Bank"
    elif(x7==3):
     o3=raw_input("Name: ")
     o4=input("Mobile number: ")
     o5=input("Enter OTP: ")
     print"Payment is getting processed by Bank"
    elif(x7==4):
     x8=input("Enter customer id: ")
     t1=input("Enter OTP: ")
     print"Payment is getting processed by Bank"
    else:
     print "Wrong choice due to payment mode selection"  

  elif (x9==3):
   print ("Choose your seat type: ")
   print "1) Window-1000 rupees"
   print "2) Middle-750 rupees"
   print "3) Aisle-500 rupees"
   x3=input("Choose your option: ")
   x4=len(a)
   if (x3==1):
     y1=x4*1000
     print "total price is ",y1
   elif(x3==2):
     y2=x4*750
     print "total price is ",y2
   elif(x3==3):
     y3=x4*500
     print "total price is ",y3
   else:
     print"Wrong option due to type of seat selection"
   if(x3==1 or x3==2 or x3==3):  
    print "Choose method of pay"  
    print "1) Credit card"
    print "2) Debit card"
    print "3) PayTm"
    print "4) Netbanking"  
    x7=input("Enter your option: ")
    if (x7==1):
     n3=raw_input("Cardholders name: ")
     n4=input("Date of expiry(mmyyyy): ")
     n5=input("CVV number: ")
     n6=input("Enter mobile number: ")
     n7=input("Enter OTP: ")
     print"Payment is getting processed by Bank"
    elif(x7==2):
     m3=raw_input("Cardholder's name: ")
     m4=input("Date of expiry(mmyyyy): ")
     m5=input("CVV number: ")
     m6=input("Enter mobile number: ")
     m7=input("Enter OTP: ")
     print"Payment is getting processed by Bank"
    elif(x7==3):
     o3=raw_input("Name: ")
     o4=input("Mobile number: ")
     o5=input("Enter OTP: ")
     print"Payment is getting processed by Bank"
    elif(x7==4):
      x8=input("Enter customer id: ")
      t1=input("Enter OTP: ")
      print"Payment is getting processed by Bank"
    else:
     print "Wrong choice due to payment mode selection"
    
  else:
    print"Wrong choice due to type of class selection"  

 else: 
    print"Wrong choice due to date or time"
  
print "Thank you for choosing us.Have a great journey!!"  
