
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
        #---------------------- ">>>>>>>>>>>>>>>>>>> checking the operator '+' and '-'"       
        retOperator = (re.findall('[^0-9]+', checkProblem))
        if (retOperator[0]).strip() != "+" and (retOperator[0]).strip() != "-":
            return("Error: Operator must be '+' or '-'.")

        #---------------------- ">>>>>>>>>>>>>>>>>>> Numbers must only contain digits"  
        print(">>>>>>>>>>>>>>>>>>> Numbers must only contain digits" ) 
        lstProblem = splitProblem(checkProblem)  
        if type(lstProblem[0]) != int or type(lstProblem[2]) != int:
            return("Error: Numbers must only contain digits.")
        
        #---------------------- ">>>>>>>>>>>>>>>>>>> Numbers cannot be more than four digits."       
        if len(lstProblem[0]) > 4 or len(lstProblem[2]) > 4:
            return("Error: Numbers cannot be more than four digits.")



    


    for problem in problems:
        #--------------------------------  
        print(">>>>>>>>>>>>>>>>>>> analysing ")      
        print("ind = " + problem)

        each_problem = problem
        x = re.search("[\+\-]", each_problem)
        atpos = x.start()
        print("position = ", atpos)
        
        first = (each_problem[:atpos]).strip()
        second = (each_problem[atpos+1:]).strip()
        operator = each_problem[atpos].strip()

        print("first: " + first)
        print("operacao: " + operator)
        print("second: " + second)

        if len(first) > len(second):
            diference = len(first) - len(second)
            lnsecond = operator + second.rjust(len(second) + diference + 1," ")
            lnfirst  = first.rjust(len(first) + 2," ")  # two space before operator
        else:
            diference = len(second) - len(first)
            lnfirst  = first.rjust(len(first) + diference + 2," ")
            lnsecond = operator + second.rjust(len(second) + 1," ") # one space before operator

        print("length  first: " + str(len(lnfirst)) + " - " + lnfirst)
        print("length second: " + str(len(lnsecond)) + " - " + lnsecond)
        
        lst_first.append(lnfirst.ljust(len(lnfirst) + 4, "."))
        lst_second.append(lnsecond.ljust(len(lnsecond) + 4, "."))
        lst_dashes.append((dashes.rjust(len(lnsecond), "-")).ljust(len(lnsecond) + 4, "."))

        if answer == True:
            if operator == "+":
                lst_answer.append((str(int(first) + int(second)).rjust(len(lnsecond), " ").ljust(len(lnsecond) + 4, ".")))
            else:
                lst_answer.append((str(int(first) - int(second)).rjust(len(lnsecond), " ").ljust(len(lnsecond) + 4, ".")))

    print(lst_first)
    print(lst_second)
    print(lst_dashes)
    print(lst_answer)

    for concat in lst_first:
        arranged_problems += concat
    arranged_problems += '\n'

    for concat in lst_second:
        arranged_problems += concat
    arranged_problems += '\n'
    
    for concat in lst_dashes:
        arranged_problems += concat
    arranged_problems += '\n'

    for concat in lst_answer:
        arranged_problems += concat
    arranged_problems += '\n'

    return arranged_problems


def splitProblem(oneProblem):

    lstOneProblem = []

    pos = re.search("[\+\-]", oneProblem)
    atpos = pos.start()
    print("position = ", atpos)
    
    #first = (oneProblem[:atpos]).strip()
    #second = (oneProblem[atpos+1:]).strip()
    #operator = oneProblem[atpos].strip()

    lstOneProblem.append((oneProblem[:atpos]).strip())
    lstOneProblem.append((oneProblem[atpos]).strip())
    lstOneProblem.append((oneProblem[atpos+1:]).strip())

    print (lstOneProblem)
    return (lstOneProblem)