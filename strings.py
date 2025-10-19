
curso = "pYtHon Language"

print(curso.upper())  
# PYTHON LANGUAGE

print(curso.lower())  
# python language

print(curso.capitalize())  
# Python language

print(curso.title())  
# Python Language

print(curso.swapcase())  
# PyThON lANGUAGE

print(curso.strip())  
# pYtHon Language

print(curso.replace("Language", "Programming"))

#--------------------------------------------------------------------------------------

curso2 = "    Python "

print(curso2.strip())  
# Python    
print(curso2.lstrip())  
# Python    
print(curso2.rstrip())  
#     Python

# --------------------------------------------------------------------------------------

curso3 = "Python"

print(curso3.center(10, "#"))
# ##Python##
print(curso3.ljust(10, "#"))
# Python----
print(curso3.rjust(10, "#"))
# ****Python
print(".".join(curso3)) 
# P.y.t.h.o.n

#--------------------------------------------------------------------------------------

