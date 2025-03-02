We can render an ASCII art pyramid with N levels by printing N rows of asterisks, where the top row has a single asterisk in the center and each successive row has two additional asterisks on either side.

Here's what that looks like when N is equal to 3.

  *  
 *** 
*****
And here's what it looks like when N is equal to 5.

    *    
   ***   
  ***** 
 ******* 
********* 
Can you write a program that generates this pyramid with a N value of 10?



# import requests
# import mysql.connector
# import pandas as pd

print('Hello')


def pyramid(n):
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars + spaces)
        
        
pyramid(20)