
one="""
    ###
  #####
 ##  ##
##   ##
     ##
     ##
     ##
     ##
     ##
"""

two = """
  ###   
 ##  ## 
##    ##
     ## 
    ##  
   ##   
  ##    
 ##     
########
"""

three = """
  ####   
 ##  ##  
      ## 
     ##  
    ##   
     ##  
     ##  
##  ##   
 ####    
"""


four = """
    ###
  ## ##
 ##  ##
##   ##
#######
     ##
     ##
     ##
     ##
"""


five = """
#######
##     
##     
#####  
     ##
     ##
     ##
    ## 
####   
"""

six = """
    ##
   ## 
  ##  
 ##   
######
##  ##
##  ##
##  ##
######
"""

seven = """
#######
     ##
     ##
    ## 
   ##  
  ##   
 ##    
##     
##     
"""

eight = """
 ##### 
##   ##
##   ##
##   ##
 ##### 
##   ##
##   ##
##   ##
 ##### 
"""

nine = """
 ##### 
##   ##
##   ##
##   ##
#######
     ##
     ##
     ##
#######
"""

zero = """
 ##### 
##   ##
##   ##
##   ##
##   ##
##   ##
##   ##
##   ##
 ##### 
"""


digit_dictionary = {'0': zero, '1': one, '2':two, '3':three, '4':four, '5':five, '6':six, '7':seven, '8':eight, '9':nine}

your_digit = 8901234567

def get_line_of_multiline_string(your_string, number):
  '''
    returns specific line of your string
  '''
  your_lines = your_string.split('\n')
  return your_lines[number]

def convert_number_to_hashes(digit):

  '''
    Function converts
    digit in int to hashed looking digits
  '''
  if not type(digit) is int:
    raise TypeError

  all_digits = """"""
  for line in range(1,11):
    for that_digit in str(digit):
      all_digits += get_line_of_multiline_string(digit_dictionary[that_digit], line) + "   "
    all_digits = all_digits + "\n"

  print (all_digits)

convert_number_to_hashes(your_digit)