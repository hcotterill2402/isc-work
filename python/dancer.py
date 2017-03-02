#creating a script to run a function from the Linux command line

import sys                          #importing system library
from dancing.dance import boogie    #importing function boogie 

moves=sys.argv[1:] # variable 'moves' will take whatever is in the command line
                   # after you call the function

boogie(moves)      # then runs the function with the command line input as the 
                   # arguement
