def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: 
## printed result: 3, 4
## function
### The function add_one will give as a result a number one unit above the value placed as an input. 
## for loop
### it loopes through the values in the list and applies the condition stated. 
### only those numbers that return TRUE to the if condition (those bigger than 1) will pass to the next argument
### since that argument is to apply the previously defined function, which adds one number, only 2 and 3 pass and each gets a +1 added to them
### returning 3 and 4


# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer:
## add_one(2) will return 3. but it will not print anything unless asked to. it stores the output.
## return depends on the input and the function definition. the input is 2, and the definition is input + 1
## the print in the loop applies the function to numbers that comply with the condition, and shows the result