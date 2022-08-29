def arithmetic_arranger(problems, show_results = False):
  top_line = ""
  bottom_line = ""
  lines = ""
  sum_x = ""
  output = None
  error = False
  error_output = ""

  # loop to split
  for problem in problems:
    problem_array = problem.split(" ")
    x = problem_array[0]
    operator = problem_array[1]
    y = problem_array[2]
      
    # checks for input errors
    if (operator != '+') and (operator != '-'):
      error = True
      error_output = "Error: Operator must be '+' or '-'."
    elif (len(x) > 4) or (len(y) > 4):
      error = True
      error_output = "Error: Numbers cannot be more than four digits."
    elif x.isdigit() == False or y.isdigit() == False:
      error = True
      error_output = "Error: Numbers must only contain digits."
    
    if error == False:  
      # result finder
      sum = ""
      if(operator == "+"):
        sum = str(int(x) + int(y))
      elif(operator == "-"):
        sum = str(int(x) - int(y))
      
      # single problem variables
      length = max(len(x), len(y))
      prob_len = int(length) + 2
      top_num = str(x).rjust(prob_len)
      bottom_num = operator + " " + str(y).rjust(length)
      dashes = "-" * (prob_len)
      result = str(sum).rjust(prob_len)
      
      # adding spaces if it's not the last problem
      if problem != problems[-1]:
        top_line += top_num + "    "
        bottom_line += bottom_num + "    "
        lines += dashes + "    "
        sum_x += result + "    "
      else:  # formatting for last problem
        top_line += top_num
        bottom_line += bottom_num
        lines += dashes
        sum_x += result
        
      if show_results == True:
        output = top_line + "\n" + bottom_line + "\n" + lines + "\n" + sum_x
      else: 
        output = top_line + "\n" + bottom_line + "\n" + lines
  
    # too many problems error
  if (len(problems) > 5):
    error = True
    error_output = "Error: Too many problems."
  
  if error == True:    
    return(error_output)
  else:
    return(output)