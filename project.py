def arithematic_operatoion(problems,show_answer=False):
    if len(problems) >5:
        return ('Error: Too many problems.')
        
    first=[]
    second=[]
    dash=[]
    answer=[]

    for i in problems:
            parts=i.split()\
            
            if len(parts) !=3 :
                print("parts should be equal to 3")
            
            num1,operator,num2=parts
            if operator not in ('+','-'):
                return ("Error: Operator must be '+' or '-'.")
            if not num1.isdigit() and num2.isdigit():
                return ('Error: Numbers must only contain digits.')
            if len(num1)>4 or (num2)>4:
                return("Error: Numbers cannot be more than four digits.")
            
            width=max(len(num1),len(num2))*2

            first.append(num1.rjust(width))
            second.append(operator+num2.rjust(width-1))
            dash.append('-'*width)

            if show_answer:
                if operator=='+':
                    result=str(int(num1)+int(num2))
                else:
                    result=str(int(num1)-int(num2))

                answer.append(result.rjust(width))

    arrange='    '.join(first)+'\n'+\
    '    '.join(second)+'\n'+\
    '    '.join(dash)
       
    if show_answer:
        arrange +='\n' + '   '.jon(answer)

        return arrange
