#blueprints
print("""
equations:
      x = times
      + = plus
      - = negative
      / = division
      bye = end
      """)
#Looping
while 1 < 2 :
    #number input
    a = int(input("first number: "))
    b = input("equation: ")
    c = int(input("second number: "))
    # equation functions
    if b == "+" :
        print(a + c)
    if b == "x" :
        print(a * c)
    if b == "-" :
        print(a - c)
    if b == "/" :
        print(a / c)
    
    #ending
    if b == "bye" :
        break
