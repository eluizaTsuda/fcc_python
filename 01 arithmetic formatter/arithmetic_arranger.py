
import re

def arithmetic_arranger(problems, answer=False):
    # C:\@Luiza_Local\MyProjects\fcc\python\01 arithmetic formatter

    arranged_problems= ''
    first = ''
    second = ''
    operator = ''
    dashes = ''
    lst_first = []
    lst_second = []
    lst_dashes = []
    lst_answer = []
    i = 0

    if (len(problems) > 5 ):
        #---------------------- ">>>>>>>>>>>>>>>>>>> checking limit = 5 
        return("Error: Too many problems.")

    for checkProblem in problems:
        #---------------------- ">>>>>>>>>>>>>>>>>>> checking others rules
        lstProblem = splitProblem(checkProblem) 

        if lstProblem[0] == False:
            if lstProblem[1] == 1:
                return("Error: Operator must be '+' or '-'.")
            elif lstProblem[1] == 2:
                return("Error: Numbers must only contain digits.")
            elif lstProblem[1] == 3:
                return("Error: Numbers cannot be more than four digits.")
            else:
                return("Error: Different pattern. Example, '1235 + 52'")

    for setProblem in problems:
        #---------------------- ">>>>>>>>>>>>>>>>>>> Problem assembly
        #print("# ---------------------- >>>>>>>>>>>>>>>>>>> Problem assembly")      
        #print("setProblem = " + setProblem)

        x = re.search("[\+\-]", setProblem)
        atpos = x.start()
        
        first = (setProblem[:atpos]).strip()
        second = (setProblem[atpos+1:]).strip()
        operator = setProblem[atpos].strip()

        #print(" >>>>>>     first: " + first)
        #print(" >>>>>>  operacao: " + operator)
        #print(" >>>>>>    second: " + second)

        if len(first) > len(second):
            diference = len(first) - len(second)
            lnsecond = operator + second.rjust(len(second) + diference + 1," ")
            lnfirst  = first.rjust(len(first) + 2," ")  # two space before operator
        else:
            diference = len(second) - len(first)
            lnfirst  = first.rjust(len(first) + diference + 2," ")
            lnsecond = operator + second.rjust(len(second) + 1," ") # one space before operator

        #print("length  first: " + str(len(lnfirst)) + " - " + lnfirst)
        #print("length second: " + str(len(lnsecond)) + " - " + lnsecond)
        
        lst_first.append(lnfirst.ljust(len(lnfirst) + 4, "."))
        lst_second.append(lnsecond.ljust(len(lnsecond) + 4, "."))
        lst_dashes.append((dashes.rjust(len(lnsecond), "-")).ljust(len(lnsecond) + 4, "."))

        if answer == True:
            if operator == "+":
                lst_answer.append((str(int(first) + int(second)).rjust(len(lnsecond), " ").ljust(len(lnsecond) + 4, ".")))
            else:
                lst_answer.append((str(int(first) - int(second)).rjust(len(lnsecond), " ").ljust(len(lnsecond) + 4, ".")))

    #print(lst_first)
    #print(lst_second)
    #print(lst_dashes)
    #print(lst_answer)

    for concat in lst_first:  # Assembly the first line
        arranged_problems += concat
    arranged_problems += '\n'

    for concat in lst_second: # Assembly the second line
        arranged_problems += concat
    arranged_problems += '\n'
    
    for concat in lst_dashes: # Assembly the dashes line
        arranged_problems += concat
    arranged_problems += '\n'

    for concat in lst_answer: # Assembly the answer line
        arranged_problems += concat
    arranged_problems += '\n'

    return arranged_problems


def splitProblem(oneProblem):

    lstOneProblem = []
    pattern = r"^\d{1,4}\s\-\s\d{1,4}$|^\d{1,4}\s\+\s\d{1,4}$"
    bMatch = bool(re.match(pattern, oneProblem))
    lstOneProblem.append(bMatch)  

    if bMatch == False:
        pattern = "\s\W\s" 
        retOperator = (re.findall(pattern, oneProblem))
        if len(retOperator) == 0:
            #---------------------- ">>>>>>>>>>> Error: Different Pattern" 
            print( "#-- >>>>>>>>>>> Error: Different Pattern --- 1 " )
            lstOneProblem.append(4)
        else: 
            #---------------------- ">>>>>>>>>>> Others Error Rules" 
            pos = re.findall(pattern, oneProblem)
            atpos = oneProblem.index(pos[0].strip())

            firstPart = oneProblem[:atpos].strip()
            operator = oneProblem[atpos].strip()
            secondPart = oneProblem[atpos+1:].strip()

            if operator != "+" and operator != "-":
                #-- ">>>>>>>>>>> Error: Operators accept are **addition** and **subtraction**." 
                lstOneProblem.append(1)

            elif firstPart.isnumeric() == False or secondPart.isnumeric() == False:
                #-- ">>>>>>>>>>>>>>> Error: Numbers must only contain digits"  
                lstOneProblem.append(2)           

            elif len(firstPart) > 4 or len(secondPart) > 4:
                #-- ">>>>>>>>>>> Error: Numbers cannot be more than four digits."  
                lstOneProblem.append(3)

            else: 
                #-- ">>>>>>>>>>> Error: Different Pattern" 
                print( "#-- >>>>>>>>>>> Error: Different Pattern --- 2 " )
                lstOneProblem.append(4)

    return (lstOneProblem)