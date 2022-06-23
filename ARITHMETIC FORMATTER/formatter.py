from multiprocessing.sharedctypes import Value
from tracemalloc import start


def arithmetic_arranger(problems, displayMode= True):
    start == True
    side_space = "   "
    line1= line2= line3= line4 = ""
    for values in problems:
        #splitting the list
        numbers = values.split()
        #assigning numbers(string) & operand using indexes 
        first_number= numbers[0]
        operator = numbers[1]
        second_number= numbers[2]

    #Handling Exceptions
        try: 
            #converting the numbers(string) to integers
            #Only digit exception
            no1 = int(first_number)
            no2 = int(second_number)
        except:
            return "Error: Numbers must only contain digits."
        
        try:
            #less than 4 digit exception
            if len(first_number) > 4 or len(second_number) > 4:
                raise BaseException
        except:
            return "Error: Numbers must not be more than four digits."
        
        try:
            #less than 4 digit exception
            if operator != "+" and operator != "-":
                raise BaseException
        except:
            return "Error: Operator must be '+' or '-' ."
        #allocating spaces
        space = max(len(first_number), len(second_number))

    #for first arithmethic argument
        if start== True:
            line1 += first_number.rjust(space + 2)
            line2 += operator + " "+ second_number.rjust(space)
            line3 += "-" * (space + 2)
            #Determining line4 or answer
            if displayMode == True:
                if operator == "+":
                    line4 += str(no1 + no2).rjust(space + 2)
                else:
                    line4 += str(no1 - no2).rjust(space + 2)
    #other than the first arithmetic argument
        else:
            line1 += first_number.rjust(space + 6)
            line2 += operator.rjust(5) + " "+ second_number.rjust(space)
            line3 += side_space.rjust(4) + "-" * (space + 2)
            #Determining line4 or answer
            if displayMode == True:
                if operator == "+":
                    line4 += str(no1 + no2).rjust(space + 6)
                else:
                    line4 += str(no1 - no2).rjust(space + 6)
    if displayMode == True:
        arranged_problems = line1+ "\n" +line2 + "\n" +line3 + "\n" +line4
    return arranged_problems


print(arithmetic_arranger(["35 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
