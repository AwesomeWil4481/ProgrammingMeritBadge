 
continueYN = "y"

conversionRate = 0.9

while continueYN.lower() == "y" or continueYN.lower() == "yes":
   dollarInput = input("Enter value in U.S. dollar:")
   
   try: 
      dollarValue = float(dollarInput)
      convertedDollar = dollarValue * conversionRate
   
      print("Converted value is: ", convertedDollar)
 
   except: 
      print("This value is not allowed") 

   continueYN = input("Input another? (y/n)")
