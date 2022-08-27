def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b
OPERATIONS= {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
} 
def calculator():
        
    a = float(input("WHATS THE FIRST NUMBER?\n"))
    for symbol in OPERATIONS:
        print(symbol)
    should_continue = True
    while should_continue:
        
        OPERATION_symbol= input("PICK AN OPERATION\n")
        b = float(input("WHATS THE NEXT NUMBER?\n"))
        calculation = OPERATIONS[OPERATION_symbol]
        answer= calculation(a, b)
       
        print(a,OPERATION_symbol,b, "=" ,answer) 
        
        if input("TYPE 'Y' TO CONTINUE WITH OR TYPE 'N' TO EXIT\n")=="Y":
            a=answer
        else:
            should_continue= False
            calculator()
calculator()