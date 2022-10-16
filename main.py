from Logo import logo

print(logo)

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2

operation = {                                               #dictionary
    "+":add ,
    "-":subtract ,
    "*":multiply ,
    "/":divide           
}

def calculator():                                           #used for Recurrsive Calling
  num1 = float(input("First Number "))

  for symbol in operation:                                  #in Dictionary for loop's variable symbol pass through only key
      print(symbol)                                         # It will print all the operations to choose it from

  should_continue =True

  while should_continue:
    operation_symbol = input("Pick an Operation: ")
    num2 = float(input("Next Number "))
    calculation_function = operation[operation_symbol]
    answer = calculation_function(num1,num2)                #operation_symbol variable pass an operation as a key to calculation_function with change the key to value and operation takes place

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to Continue Calculating With {answer} , or Type 'n' to start a new calculation: ") == 'y':
      num1=answer
    else:
      should_continue == False
      calculator()

calculator()
