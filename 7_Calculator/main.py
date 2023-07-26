def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

from art import logo
from replit import clear

def cal():
  print(logo)
  num1 = float(input("what's the first number?: "))
  
  flag = 'y'
  
  while flag == 'y':  
    num2 = float(input("what's the second number?: "))
    
    for i in operations:
      print(i)
      
    operation_symbol = input("pick a symbol")
    cal_func = operations[operation_symbol]
    result = cal_func(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2}")
    print(f"result : {result}")
    num1 = result
    flag = input(f"keep going with {result} 'y' or reset 'n' ")
    if flag == 'n':
      clear()
      cal()
      
cal()

