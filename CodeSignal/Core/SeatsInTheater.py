# Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since the exit is located right behind your row to the left. All you need to do is climb over your seat and make your way to the exit.

# The main problem is your shyness: you're afraid that you'll end up blocking the view (even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns to your left. To gain some courage, you decide to calculate the number of such people and see if you can possibly make it to the exit without disturbing too many people.

# Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.

# Example

# For nCols = 16, nRows = 11, col = 5, and row = 3, the output should be
# solution(nCols, nRows, col, row) = 96.

# Here is what the theater looks like:


def solution(nCols, nRows, col, row):
    totalSeats = nCols * nRows;
    
    newColNumber = nCols - col + 1;
    newRowNumber = nRows - row;
    
    peopleBehindMe = newColNumber * newRowNumber;
    
    return peopleBehindMe
