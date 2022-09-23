
import tkinter as tk

height = 600
width = 500

root = tk.Tk()
root.title("Scientific Calculator GUI")

canvas = tk.Canvas(root, height= height, width = width)
canvas.pack()

#setting up keys
def keys(event):
    char = None
    if type(event) == str:
        char = "="
    else:
        char = event.char
    if char.isdigit():
        buttonNum(int(char))
    elif char in ["+","-","x","÷","."]:
        buttonNum(event.char)
    elif char == "=":
        calculate()
    elif char == "C":
        reset()

root.bind("KEY", keys)
root.bind("RETURN", lambda x: keys("="))

#constants

buttonW, buttonHL, buttonHR = 0.23, 0.2 * 0.85, 0.2 * 0.55
displayText =""
previousOperation = None

frame = tk.Frame(root, bg = '#006400')
frame.place(relwidth=1, relheight=1)

display = tk.Label(frame, text="", bg='white')
display.place(relx=0.01,rely=0.01,relwidth=.75,relheight=0.15)


#functions
def buttonNum(button):
    global displayText, previousOperation
    operations = ["+","-","x","÷"]
    firstOperation = ["+","x","÷"]
    if previousOperation in operations and button in operations: #prevent double operations
        return
    if not previousOperation and button in firstOperation:
        return
    previousOperation = button
    displayText += str(button)
    display.config(text = displayText)

def deletePrev():
    global displayText, previousOperation
    if not displayText: #skip if there is nothing to delete
        return
    displayText = displayText[0:len(displayText) - 1]
    display.config(text = displayText)
    if displayText:
        previousOperation = displayText[-1]
    else:
        previousOperation = None
    
def calculate():
    global displayText
    numbers = []
    operations = []
    multiplier = 1 
    index = 0
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    if not displayText:
        return
    
    if displayText[0] == "-":
        multiplier = -1
        index += 1
    while index < len(displayText):
        curr = ""
        char = displayText[index]
        while char in digits:
            curr += char
            index += 1
            char = displayText[index] if index < len(displayText) else None
        numbers.append(float(curr))
        if index < len(displayText):
            operations.append(displayText[index])
            index += 1
    numbers[0] *= multiplier

    #multiplication and division first
    pemdas = ["÷", "x"]
    removeAfter = []

    for operator in operations:
        if operator in pemdas:
            i = operations.index(operator)
            num1 = numbers[i]
            num2 = numbers[i+1]
            if operator == "÷":
                num1 = num1 / num2
            else:
                num1 = num1 * num2
            numbers[i] = num1
            numbers.pop(i+1)
            removeAfter.append(i)
    for x in sorted(removeAfter, reverse = True):
        operations.pop(x)
    
    #rest of pemdas

    total = numbers[0]
    for i in range(1, len(numbers)):
        if operations[i-1] == "+":
            total += numbers[i]
        else:
            total -= numbers[i]
    if total % 1 == 0:
        total = int(total)
    displayText = str(total)
    display.config(text = displayText)

def resetting():
	global displayText, previous
	displayText = ""
	previous = None
	display.config(text = displayText)

#button config

#numbers

button1 = tk.Button(frame, text = "1", command = lambda: buttonNum(1))
button1.place(relx = 0.01, rely = 0.24, relwidth = buttonW, relheight = buttonHL)

button2 = tk.Button(frame, text = "2", command = lambda: buttonNum(2))
button2.place(relx = 0.25, rely = 0.24, relwidth = buttonW, relheight = buttonHL)

button3 = tk.Button(frame, text = "3", command = lambda: buttonNum(3))
button3.place(relx = 0.49, rely = 0.24, relwidth = buttonW, relheight = buttonHL)

button4 = tk.Button(frame, text = "4", command = lambda: buttonNum(4))
button4.place(relx = 0.01, rely = 0.24 + 0.18, relwidth = buttonW, relheight = buttonHL)

button5 = tk.Button(frame, text = "5", command = lambda: buttonNum(5))
button5.place(relx = 0.25, rely = 0.24 + 0.18, relwidth = buttonW, relheight = buttonHL)

button6 = tk.Button(frame, text = "6", command = lambda: buttonNum(6))
button6.place(relx = 0.49, rely = 0.24 + 0.18, relwidth = buttonW, relheight = buttonHL)

button7 = tk.Button(frame, text = "7", command = lambda: buttonNum(7))
button7.place(relx = 0.01, rely = 0.24 + 0.36, relwidth = buttonW, relheight = buttonHL)

button8 = tk.Button(frame, text = "8", command = lambda: buttonNum(8))
button8.place(relx = 0.25, rely = 0.24 + 0.36, relwidth = buttonW, relheight = buttonHL)

button9 = tk.Button(frame, text = "9", command = lambda: buttonNum(9))
button9.place(relx = 0.49, rely = 0.24 + 0.36, relwidth = buttonW, relheight = buttonHL)

button0 = tk.Button(frame, text = "0", command = lambda: buttonNum(0))
button0.place(relx = 0.25, rely = 0.24 + 3 * .18, relwidth = buttonW, relheight = buttonHL)

period = tk.Button(frame, text = ".", command = lambda: buttonNum("."))
period.place(relx = 0.01, rely = 0.24 + 3 * .18, relwidth = buttonW, relheight = buttonHL)

#actions
relyFactor = 0.12
delete = tk.Button(frame, text = "DEL", command = deletePrev)
delete.place(relx = 0.49, rely = 0.24 + 3 * .18, relwidth = buttonW, relheight = buttonHL)

relyFactor = 0.12
divide = tk.Button(frame, text = "÷", command = lambda: buttonNum("÷"))
divide.place(relx = 0.76, rely = 0.24, relwidth = buttonW, relheight = buttonHR)

multiply = tk.Button(frame, text = "x", command = lambda: buttonNum("x"))
multiply.place(relx = 0.76, rely = 0.24 + relyFactor, relwidth = buttonW, relheight = buttonHR)

sub = tk.Button(frame, text = "-", command = lambda: buttonNum("-"))
sub.place(relx = 0.76, rely = 0.24 + relyFactor * 2, relwidth = buttonW, relheight = buttonHR)

add = tk.Button(frame, text = "+", command = lambda: buttonNum("+"))
add.place(relx = 0.76, rely = 0.24 + relyFactor * 3, relwidth = buttonW, relheight = buttonHR)

reset = tk.Button(frame, text = "C", command = resetting)
reset.place(relx = 0.76, rely = 0.24 + relyFactor * 4, relwidth = buttonW, relheight = buttonHR)

equal = tk.Button(frame, text = "=", command = calculate)
equal.place(relx = 0.76, rely = 0.24 + relyFactor * 5, relwidth = buttonW, relheight = buttonHR)

#start animation
root.mainloop()