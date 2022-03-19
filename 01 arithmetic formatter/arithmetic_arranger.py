
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
        print("1 - checkProblem")
        print(checkProblem)
        lstProblem = splitProblem(checkProblem) 

        if lstProblem[3] == False:  # regex invalid
            print("---------------------- Retorno do splitProblem ")
            print(lstProblem[0])
            print(lstProblem[1])
            print(lstProblem[2])
            first = lstProblem[0]
            operator = lstProblem[1]
            second = lstProblem[2]

            #---------------------- ">>>>>>>>>>>>>>>>>>> checking the operator '+' and '-'"       
            #retOperator = (re.findall('[^0-9]+', checkProblem))
            #if (retOperator[0]).strip() != "+" and (retOperator[0]).strip() != "-":

            if operator != "+" and operator != "-":
                return("Error: Operator must be '+' or '-'.")

            #---------------------- ">>>>>>>>>>>>>>>>>>> Numbers must only contain digits"  
            print(">>>>>>>>>>>>>>>>>>> Numbers must only contain digits" ) 
    
            #if type(lstProblem[0]) != int or type(lstProblem[2]) != int:
            if type(first) != int or type(second) != int:
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

    pattern = r"\d{1,4}[0-9]\s\W\s\d{1,4}[0-9]"
    pattern = r"\d[0-9]{1,4}\s\-\s\d{1,4}[0-9]|\d[0-9]{1,4}\s\+\s\d{1,4}[0-9]"
    bMatch = bool(re.match(pattern, oneProblem))

    print(bMatch)

    if bMatch == True:
        pos = re.search("[\+\-]", oneProblem)
        atpos = pos.start()
        print("position bMatch True = ", atpos)

    else:
        pattern = r"\s\W\s"
        retOperator = (re.findall(pattern, oneProblem))
        pos = re.findall(pattern, oneProblem)
        atpos = oneProblem.index(pos[0].strip())
        print("position bMatch False = ", atpos)
        print("================================================= here")

    print(oneProblem[:atpos].strip())   # first
    print(oneProblem[atpos].strip())   # operator
    print(oneProblem[atpos+1:].strip()) # second
            
          
    lstOneProblem.append((oneProblem[:atpos]).strip())   # first
    lstOneProblem.append((oneProblem[atpos]).strip())    # operator
    lstOneProblem.append((oneProblem[atpos+1:]).strip()) # second
    lstOneProblem.append(bMatch)

    print("---------------------------- saindo da funcao ")
    print (lstOneProblem)
    return (lstOneProblem)