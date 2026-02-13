"""
Console-Based Calculator System

Author: Muhammad Umar

Features:
- Arithmetic Operations
- BMI calculator
- Unit Converters
- Input Validation
"""


import math  
import time  

#======= Time Based Greeeting ======
def get_time_based_messages():
 
    hour = int(time.strftime('%H'))
    if 5 <= hour <= 11:
        return  "Good Morning","Have a great day!"
           
    elif 12 <= hour <= 16:
        return "Good Afternoon","Have a great day ahead!"
    elif 17 <= hour <= 20:
        return "Good Evening","Thanks for using the calculator. Enjoy your evening!" 
    else:
        return  "Welcome! Hope you're having a great night!","Good Night"        
    
welcome_msg, exit_msg = get_time_based_messages()


# =========Opreaters Menu=========
def show_main_menu():  
  print("\n===============================")
  print("=====Calculation Choices=======")
  print("===============================")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Remainder")
  print("6. Power")
  print("7. Integral Division")
  print("8. Square Root")
  print("9. BMI Calculator")
  print("10. Unit Converter") 
  print("11. Exit")

# =====unit conveter menu=======
def show_converter_menu():
  while True:
    print("\n=====Unit Converter=====")
    print("1. Length ")
    print("2. Weight ")
    print("3. Temperature ")
    print("4. Data Conversion ")
    print("5. Speed Conversion ")
    print("6. Number system ")
    print("7. Go back to main menu")
    print("----------------------------------")
    choice = (input("    Choose an option: "))
    print("----------------------------------")
    if choice not in ["1","2","3","4","5","6","7"]:
       print("Invalid choice!! Enter 1-7")
    else:
     match choice:  
       case "1":
          length_converter()
      
       case "2":
        weight_converter()
       
       case "3":
        temperature_converter()
        
       case"4":
        data_converter()
     
       case "5":
        speed_converter()
        
       case "6":
         Number_system()
 
       case"7":
         print("Exiting Conveter.....")
         return
    input("\n Press Enter to Continue...")   

#========bmi menu===============
def show_bmi_menu():
   print("\n====Select units==== ")
   print("1. kg, m")
   print("2. lbs, inch")
   bmi_choice=(input("Enter Your choice: "))
   if bmi_choice not in ["1","2"]:
       print("Invalid choice!")
   else:
      bmi_calculation(bmi_choice)

#===========calculation operation================
def calculator_operation(choice):
    # For square root input, 
  try:
     if choice == "8":
       num = float(input("Enter number: "))
     else:
       num1=float(input("Enter first value :"))
       print("-------------------------------")
       num2=float(input("Enter second value : "))
       print("-------------------------------")
     
  except ValueError:
       print("Invalid Input! Please Enter Valid Number")
       return

    
  match choice:
       case "1":
          print(num1,"+",num2,"=",num1+num2)
       case "2":
          print(num1,"-",num2,"=",num1-num2)
       case "3":
          print(num1,"X",num2,"=",num1*num2)
       case "4":
        if(num2==0):
          print("Division is not Possible  \"Maths Error!\"")
        else:
          print(num1,"/",num2,"=",num1/num2)
       case "5":
          print(num1,"/",num2,"Remainder =",num1 % num2)
       case "6":
          print(num1,"^",num2,"=",num1**num2)
       case "7":
        if(num2==0):
          print("Division is not Possible  \"Maths Error!\"")
        else:
          print(num1,"/",num2,"integral part =",num1//num2)     
       case "8":
          if num < 0:
           print("Can't take Square Root of Neagtive Number")
          else: 
           print("Square Root of",num,"=",math.sqrt(num))
      


# ========BMI Calculator======== 
def bmi_calculation(bmi_choice):
 bmi=None
 try:
        if bmi_choice == "1":
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))
        elif bmi_choice == "2":
            weight = float(input("Enter weight (lbs): "))
            height = float(input("Enter height (inch): "))
        else:
            return
 except ValueError:
        print("Invalid input")
        return

 if height <= 0 or weight<= 0:
        print("Height and weight must be greater than zero")
        return
 elif bmi_choice == "1":
       bmi = weight / (height ** 2)  

 elif bmi_choice == "2":
    bmi=(weight / (height ** 2)) * 703

 if bmi is None:
    return
 print("Your BMI is",round(bmi,2))

  # BMI category       
 if bmi < 18.5:
    print("You are Underweight")
 elif 18.5 <= bmi < 25:
    print("You have Normal weight")
 elif 25 <= bmi < 30:
     print("You are Overweight")
 elif 30 <= bmi < 35:
    print("You are Obese (Class 1)")
 elif 35 <= bmi < 40:
    print("You are Obese (Class 2)")
 else:
     print("You are Extremely Obese (Class 3)")
  
           

   

#===========lenght converter============
def length_converter():
    print("   Length Converter")
    print("------------------------") 
    print("1. km to m")
    print("2. km to miles")
    print("3. m to cm")
    print("4. cm to mm")
    print("5. km to cm")
    print("6. m to mm")
    print("7. m to inch")
    length_choice = input("Choose conversion: ")
    if length_choice in ["1","2","3","4","5","6","7"]:
          try:
             value = float(input("Enter value: "))
          except ValueError:
             print("Invalid Input! Please Enter Valid Number")
             return
       
          match length_choice:
           case "1":
             print(str(value) + " km = " + str(value * 1000) + " m")
           case "2":
             print(str(value) + " km = " + str(value * 0.6213371) + " miles")
           case "3":
             print(str(value) + " m = " + str(value * 100) + " cm")
           case "4":
             print(str(value) + " cm = " + str(value * 10) + " mm")
           case "5":
             print(str(value) + " km = " + str(value * 100000) + " cm")
           case "6":
             print(str(value) + " m = " + str(value * 1000) + " mm")
           case "7":
             print(str(value) + " m = " + str(value * 39.3701) + " inches")
    else:
        print("Invalid choice!!")

# ===========weight converter==============
def weight_converter():
    print("  Weight Converter")
    print("------------------------")
    print("1. kg to g")
    print("2. g to mg")
    print("3. kg to mg")
    print("4. kg to lbs")
    weight_choice = (input("Choose conversion: "))
    if weight_choice in["1","2","3","4"]:
      try:
        value = float(input("Enter value: "))
      except ValueError: 
        print("Invalid Input! Please Enter Valid Number")
        return
     
      match weight_choice:
        case "1":
                    print(str(value) + " kg = " + str(value * 1000) + " g")
        case "2":
                    print(str(value) + " g = " + str(value * 1000) + " mg")
        case "3":
                    print(str(value) + " kg = " + str(value * 1000000) + " mg")
        case "4":
                    print(str(value) + " kg = " + str(value * 2.20462) + " lbs")
    else:
      print("Invalid Choice!!!")
# ===========tempratuer converter=================
def temperature_converter():
 print("  Temperature Converter")
 print("------------------------")
 print("1. C to F")
 print("2. F to C")
 print("3. C to K")
 temp_choice = (input("Choose conversion: "))
 if temp_choice in ["1","2","3"]:
     try:
       value = float(input("Enter value: "))
     except ValueError:
       print("Invalid Input! Please Enter Valid Number")
       return
       
     
     match temp_choice:
      case "1":
        print(str(value) + " C = " + str((value * 9/5) + 32) + " F")
      case "2":
          print(str(value) + " F = " + str((value - 32) * 5/9) + " C")
      case "3":
         print(str(value) + " C = " + str(value + 273.15) + " K")
 else:
      print("Invalid Choice!!!")
# ==============speed converter==============
def speed_converter():
  print("   Speed Converter")
  print("------------------------")
  print("1. km/h to m/s")
  print("2. km/h to mph")
  print("3. m/s to km/h")
  print("4. m/s to mph")
  print("5. mph to km/h")
  print("6. mph to m/s")
  speed_choice = (input("Choose conversion: "))
  if speed_choice in ["1","2","3","4","5","6"]:
    try:
       value = float(input("Enter value: "))
    except ValueError:
       print("Invalid Input! Please Enter Valid Number")
       return
      
     
    match speed_choice:
     case "1":
         print(str(value) + " km/h = " + str(value / 3.6) + " m/s")
     case "2":
         print(str(value) + " km/h = " + str(value * 0.621371) + " mph")
     case "3":
         print(str(value) + " m/s = " + str(value * 3.6) + " km/h")
     case "4":
         print(str(value) + " m/s = " + str(value * 2.23694) + " mph")
     case "5":
         print(str(value) + " mph = " + str(value / 0.621371) + " km/h")
     case "6":
         print(str(value) + " mph = " + str(value / 2.23694) + " m/s")
  else:
      print("Invalid Choice!!!")

#============Data Converter=============
def data_converter():
  print("Data Converter")
  print("------------------------")
  print("1. KB to MB")
  print("2. MB to KB")
  print("3. MB to GB")
  print("4. GB to MB")
  print("5. GB to TB")
  print("6. TB to GB")
  data_choice = (input("Choose conversion: "))
  if data_choice in ["1","2","3","4","5","6"]:
     try:
       value = float(input("Enter value: "))
     except ValueError:
       print("Invalid Input! Please Enter Valid Number")
       return
      
     
     match data_choice:
        case "1":
         print(str(value) + " KB = " + str(value / 1024) + " MB")
        case "2":
         print(str(value) + " MB = " + str(value * 1024) + " KB")
        case "3":
         print(str(value) + " MB = " + str(value / 1024) + " GB")
        case "4":
         print(str(value) + " GB = " + str(value * 1024) + " MB")
        case "5":
         print(str(value) + " GB = " + str(value / 1024) + " TB")
        case "6":
         print(str(value) + " TB = " + str(value * 1024) + " GB")
  else:
      print("Invalid Choice!!!")

#========Number system converter
def Number_system():
 print(" Number System converter")
 print("-----------------------------")
 print("1. Binary to Decimal")
 print("2. Decimal to Binary")
 print("3. Decimal to Hexadecimal")
 print("4. Hexadecimal to Decimal")
 choice = input("Choose conversion: ")
 if choice in ["1","2","3","4"]:
  match choice:
    case "1":
       binary = input("Enter Binary number: ")
       if set(binary) .issubset({"0","1"}):  
          decimal = int(binary, 2)
          print(binary, "(binary) =", decimal, "(decimal)")
       else:
          print("Invalid Value. Enter Binarey Values")
    case "2":
       try: 
        decimal = int(input("Enter decimal number: "))
        binary = bin(decimal)[2:]       
        print(decimal, "(decimal) =", binary, "(binary)")
       except ValueError:
          print("Invalid Value. Enter Decimal Values")
    case "3":
       try: 
         decimal = int(input("Enter decimal number: "))
         hexa = hex(decimal)[2:]
         print(decimal, "(decimal) =", hexa, "(hexadecimal)")
       except ValueError:
         print("Invalid Value. Enter Decimal Values")
       
    case "4":
        hexa = input("Enter hexadecimal number: ")
        try: 
          decimal = int(hexa, 16)
          print(hexa, "(hexadecimal) =", decimal, "(decimal)")
        except ValueError:
         print("Invalid Value. Enter Hexadecimal Values")
 else:
    print("Invalid choice. Select 1 to 4")
     


#====== Welcome Message========= 

print("\n=====",welcome_msg,"=====\n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("     Welcome to Calculator")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
 
#============ main program==============
def main():


 while True:
   show_main_menu()
   print("-------------------------------")
   choice=(input("Enter your selected Choice : ").strip())
   print("-------------------------------")

  # checking choice validation 
   valid_choice = {"1","2","3","4","5","6","7","8","9","10","11"}
   if choice not in valid_choice:
     print("Invalid input! Please select 1-11")
     continue

  # Exit time based greeting
   if(choice == "11"):
      print("\nExiting calculator......")
      print("\n====",exit_msg,"====\n")
      break

  # real calculation
   calculation_choice = {"1","2","3","4","5","6","7","8"}
   if choice in calculation_choice:
    calculator_operation(choice)

   elif choice == "9":
     show_bmi_menu()

   elif choice == "10":
         show_converter_menu()
         

# ===============Entry point==============
if __name__=="__main__":
 main()