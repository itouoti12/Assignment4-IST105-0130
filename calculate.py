import sys
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]


if a.isnumeric() and b.isnumeric() and c.isnumeric():
    if int(a) < 1:
        print("<h1>the input a is too small</h1>")
    elif int(b) == 0:
        print("<h1>the input b will not affect the result</h1>")
    elif int(c) < 0:
        print("<h1>ERROR: the input c is negative value</h1>")
    elif int(c) >= 0:
        result = 0
        computeC = int(c)**3
        if computeC > 1000:
            result = computeC**0.5*10
        else:
            result =  computeC**0.5/int(a)
        
        result += int(b)

        print(f"<h3>Final Result: is {result}</h3>")
else:
    print("<h1>must type numeric values</h1>")



