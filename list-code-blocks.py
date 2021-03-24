#### LIST CODE BLOCKS ####

# Passing a list as an argument to a function
    def main_example():
        numbers = [1,2,3,4,5]
        print('Total:', get_totals(numbers))

    def get_totals(value_list):
        total = 0
        for num in value_list:
            total += num
        return total

    main_example()

# Working with lists and files.

# Writelines Method
    # NOTE: writelines method writes an entire list to a file and
    # doesn't add a newline ('\n') at the end of each item.
    # ex New YorkBostonAtlantaDallas

    # use the for loop to iterate through the list

    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    outfile = open('cities.txt', 'w')
    for item in cities:
        outfile.write(item + '\n')
    outfile.close()

#### READ ITEMS FROM FILE TO A LIST ####

    infile = open('studenttest.txt', 'r')
    
    # Read the contents of the file into a list.
    student_test = infile.readlines()
    
    # Close the file.
    infile.close()

    # Strip newline character from list.
    index = 0
    while index < len(student_test):
        student_test[index] = student_test[index].rstrip('\n')
        index += 1

    # student_test list is now good to go.

# Two Dementional Lists
    grid = [[1,2,3],[4,5,6],[7,8,9]]

    # to reference the elements in the list:
    #        col 0:     col 1:     col 2:
    # row 0: grid[0][0] grid[0][1] grid[0][1]
    # row 1: grid[1][0] grid[1][1] grid[1][2]
    # row 2: grid[2][0] grid[2][1] grid[2][2]

    # sum all values in first row.
    base_row = int(grid[0][0]) + int(grid[0][1]) + int(grid[0][2])

    # Example of iterating through rows then columns to check values:
    def is_row_sum(grid, base_row, 3, 3): # Determine if row sums are equal.
        rowSum = 0
        for rowIndex in range(3): # iterated horizontally, rows to columns.
            for colIndex in range(3):
                rowSum += grid[colIndex][rowIndex] 
            if rowSum != base_row: # compare each row to base sum.
                return False
            else:
                rowSum = 0

        return True

    # Example of iterating through columns then rows to check values:
    def is_col_sum(grid, base_row, 3, 3):
    colSum = 0
    for colIndex in range(3): # iterated vertically, columns to rows.
        for rowIndex in range(3):
            colSum += grid[rowIndex][colIndex]
        if colSum != base_row:
            return False
        else:
            colSum = 0

    return True