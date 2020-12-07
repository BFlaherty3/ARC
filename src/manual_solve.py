#!/usr/bin/python
"""
    Student Name: Bernadette Flaherty
    Student ID:   20235945
    GitHub URL:  https://github.com/BFlaherty3/ARC
    
    Chosen Tasks:
        
    a3325580.json
    =============
    The input grid contains various irregular-shapes in different colors. 
    The output is required to be an n x m matrix, where: 
        - each column represents one of the colors in the input matrix
        - the number of rows = the maximum count of cells for any given color in the input matrix
        - any colors that do not have sufficient cells to make a full column are discarded from the output
    Thus, not every color in the input matrix will be represented in the output, and the dimensions of the output 
    will not be the same as the input
    
    The description of the solve algorithm and sample imput and output are contained in the solve function description 
    and comments. 
    
    All of the test and training grids are solving correctly in my implementation.
    

    228f6490.json
    =============
    The input grid consists of:
        - one or more grey  parallelograms, each having an irregular black shape within it
        - one or more non-grey colored irregular shapes. 
    The output is required to:
        - The irregular black shape within each grey parallelogram will be replaced with one of the 
          non-grey irregular colored shapes in the grid, where the shapes of the target and source shapes 
          must match. 
        - If there are more than one candidate shapes for a given grey parallelogram, then choose the one closest to
          the grey shape in the matrix
          
    Thus, in the output grid, chosen the non-grey irregular shapes that match the size of the shape within the grey box(es) will
    be moved to be contained within the grey box. The remaining shapes will be retained unchanged in their original position.
     
    The description of the solve algorithm and sample imput and output are contained in the solve function description 
    and comments.   
    
    All of the test and training grids are solving correctly in my implementation.
    
    
    3631a71a.json
    =============
    The input grid represents a multi-colored mosaic pattern. 
    - The center of the pattern is a diamond-like construct and the pattern moves outward from the centre of the pattern.
    - Each row is symmetrical from its centre point, and each column is symmetrical from its centre point. 
    - However, the pattern is positioned off-centre of the input grid. 
        - Thus the centrepoint of the pattern is not the centrepoint of the grid
        - Furthermore, the centerpoint of one row will not be the same centreposition of all rows and similarly for columns, 
          the centerposition of each column will not be the same necessarily
    There are patches of missing squares in the input mosaic. (colored maroon / dark red - 9)
    
    The output is required to complete the missing squares in the input mosaic by finding the centrepoint of the rows and columns 
    and making a symmetrical replacement for any missing squares. 
    
    The description of the solve algorithm and sample imput and output are contained in the solve function description 
    and comments.   
    
    All of the test and training grids are solving correctly in my implementation.  
    
    =======
    SUMMARY
    =======
    I choose three tasks that required very different approaches to the solution. This was intentional, 
    for assignment purposes it was more effort and more challenging for me to tackle three very different problems,
    than three similar problems that could re-use the same techniques. So in my summary of commonalities, rather than 
    discuss simplarities between the solutions for my three chosen puzzles, I will discuss where my solution is 
    similar and could easily be applied to other tasks in the ARC corpus, with some minor enhancements to parameterise 
    the functions. e.g. the set of axis to apply symmetry on.
    
    a3325580.json requires no pattern matching, it is simply an extraction of cells of matching colors in a particular
    order. Simple iteration, comparison and array functions are all that is required to solve. The technique can be 
    applied to other tasks in the corpus: 
     - f8b3ba0a.json : This task involves identifying occurrance of non-blue and non-black
       colors and then output one column, with one cell for each color, in the order of frequency
       of occurrance
     - 4be741c5.json: Find the order of occurrance of each color in the grid and return one cell in one row for
       each, in the order of occurrance
    
    
    
    3631a71a.json is a symmetry problem, where we have a pattern that is symmetrical on both the x 
    and y axix and has missing squares that need to be solved. For this I used reversed arrays and 
    regex pattern matching to solve each row and column for missing cells. There are many other
    symmetrical tasks in the corpus that can be solved using the same approach.
    
    Examples of other symmetrical puzzles that could leverage my solution to 3631a71a.json are: 
    - 1e32b0e9.json: requires symmetrical matching on 2 axis to complete missing cells
    - f25ffba3.json requires symmetrical matching on the X axis only 
    - 3345333e.json requires symmetrical matching on the Y axis only, with offset centre
    - b8825c91.json is an almost identical task, with just a different 'missing square' color to detect and replace
    There are also several tasks that require symmetrical matching, but on a diagonal axis. The solution approach 
    can be extended to apply here.
    - 73251a56.json
    
    
    
    228f6490.json involves identifying sub-shapes within the input matrix and carrying out certain
    operations on them. In this example we had to find all the grey squares and then find
    a non-grey shape that matched the embedded shape within the grey square, and move it.
    Again, this solution does not require any complex matrix operations  -simple iteration, comparison 
    and array functions meet the need, and regex can be applied where required to check overlay
    of irregular shapes.
    
    Other puzzles that could leverage my solution to 228f6490.json are 
    - 09629e4f.json can be solved with a combination of my solution to 228f6490 to extract the grey target shapes, and 
      elements of my solution to a3325580 to determine the order of appearance of the colors in the first non-grey square
      which determines what color the square embedded within each grey shape will take
    - bb43febb.json, Extract the grey parallelograms and color the centre red
    - d9fac9be.json,  Extract the shape contained within another shape 
    - 890034e9.json, Extract an embedded shape and then find a matching shape 
    - 776ffc46.json, Find the shape embedded within a grey square, then find the other shapes
      in the grid that match the embedded shape and turn them the same color
    - d9fac9be.json, Find the square embedded in a non-black shape and return that square
    - fcb5c309.json
    - 3aa6fb7a.json
    - 36d67576.json
    Are more examples, since they all have a common approach to solution which involves extracting and working with 
    embedded shapes within the input matrix, and shapes embedded within other shapes
    
    
    The similarities between the tasks demonstrates what Francois Chollet (https://arxiv.org/abs/1911.01547) 
    meant when he said:
    
        "We argue that solely measuring skill at any given task falls short of measuring intelligence, 
        because skill is heavily modulated by prior knowledge and experience"
    
    Whether it be human or machine, the first time we solve a problem of a particular type, 
    we acquire skills that allow us to more easily solve similar problems. This does not 
    accurately measure true intelligence, which is the ability to solve previously 
    unseen challenges. The three basic techniques outlined in this submission are likely
    capable to solve a large percentage of the tasks within the ARC corpus, without the need for 
    developing new approaches or algorithms. 
    
    It would have been significantly less effort for me to implement three solve functions of 
    the same type, than three problems of different type - because I would not have needed 
    to invent / discover new skills or methods (by skills and methods, I am referring to 
    logical thinking, not python functions or libraries): I simply would have just
    parameterised and re-applied the methods and procedures I had already used.
    
"""

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.
# https://arc-seven.now.sh/testing_interface.html to visualise the puzzles


def solve_row(row):
    """
    row : Array of characters representing the row containing 9's (missing squares)
    returns: Array of characters representing the corrected row   
    
    Component of solve_3631a71a
    Take a row containing 9's. Solve using symmetry to return a new row replacing the 9's with correct values.
    Procedure:
        1. Find the symmetrical centre of the row by checking 2 shifts left and right of the midpoint
        2. Symmetrical centre is determined by
            a. Divide the row into the left and right side
            b. Only one side can have missing squares for the algoritym to work. If both sides are missing squares, we return the
               row unchanged
            c. Reverse the order of the right side
            d. In the side that contains 9's, replace the 9's with a period (.) Then use this side as the match pattern for a regex check for
               a match to the other side. If there is a match, we have found the symmetrical centre of the row. Additional padding of period (.) may be required
               to the strings depending on where the centre lies
        3. If symmertical centre is found
            a. Populate the missing squares on one side with the corresponding squares on the reversed other side
            b. Undo the reverse of the left side, remove any padding, reconstruct the new row and return it
            
     If any row contains 9's values on both sides of the chosen midpoint, the algorithm will return the row unchanged. 
     When we transpose the matrix and run the procedure again it will solve these via a vertical symmetry
    
     If the symmetrical midpoint is more than 2 shifts left or right of the center, the algorithm will return the row unchanged. The range of the 
     mid-point offset could be increased in this case but for all test and training cases this has been sufficient
     """
    
    match_l = False     # True if the left side of our row will be the regex pattern for this iteration, otherwise false
    match_r = False     # True if the right side of our row will be the regex pattern for this iteration, otherwise false
    match = None
    str_left = ""
    str_right = ""
    midpoint = 0        # The symmetrical midpoint we are currently evaluating
    match_offset = 0    
    
    # Check for symmetrical centre 2 cells left of the row midpoint, at the row midpoint, and 2 cells right of the row midpoint
    # Increase this range if we find a case where the midpoing is offset more than this, but for all test and training examples this
    # is sufficient
    for midpoint_offset in range (-2, 3):
        midpoint = int(len(row) / 2  + midpoint_offset)
        match_l = False 
        match_r = False 
        # When we shift the symmetrical midpoint one cell left or right, we heed to add 2 padding cells on the 'shorter' side for the regrex match to work
        str_padding = "." *  (2 * abs(midpoint_offset)) 
        
        # Split the row based on the midpoint, reverse the order of the rightpart
        l_part = np.array(row[0:midpoint]).astype(str)
        r_part = np.array(np.flipud(row[midpoint:])).astype(str)
        
        # Check which side has the 9's
        if '9' in l_part: match_l = True   # Left part will be the regex pattern
        if '9' in r_part: match_r = True   # Right part will be the regex pattern
            
        if match_l and match_r:
            # This algorithm cannot match wildcards on both sides of the string, continue to the next iteration to shift
            # the midpoint, or return the row unchanged if none of the midpoints result in a solve
            continue 
        
        if midpoint_offset < 0:
            # Add padding to the left string, as this is the shorter side, and replace any 9's with .'s
            # Only one side will have 9's so the replace operation will be redundant on the side with no 9s's
            str_left = str_padding + ''.join(l_part).replace("9",".") 
            str_right = ''.join(r_part).replace("9",".") 
        else:
            if midpoint_offset > 0:
                # Add padding to the right string, as this is the shorter side, and replace any 9's with .'s
                str_left = ''.join(l_part).replace("9",".")
                str_right = str_padding + ''.join(r_part).replace("9",".") # Add padding to the right string
            else:
                 # Both sides are equal length, just replace any 9's with .'s
                str_left = ''.join(l_part).replace("9",".") 
                str_right = ''.join(r_part).replace("9",".")              
        
        # Now see if we have a match ignore the padded spaces during the matching process
        if match_l:
            match = re.match(str_left[2 * abs(midpoint_offset):], str_right[2 * abs(midpoint_offset):])          
        else:
            match = re.match(str_right[2 * abs(midpoint_offset):], str_left[2 * abs(midpoint_offset):])
        
        if match != None: 
            match_offset = midpoint_offset
            break # exit the loop
    
    # Exited the loop - now check if we found a match
    if match == None: 
        # Failed to find a matching pattern, return the row unchanged
        return row
    
    # If we reach this point, then we have the symmetrical midpoint, so replace periods in the target row part with the 
    # corresponding characters in the source row part
    new_str = ""
    
    if match_l:
        # replace all occurrances of . in str_left, with their corresponding value in str_right
        for i in range(len(str_left)):
            if str_left[i] == '.':
                new_str += str_right[i]
            else:
                new_str += str_left[i]     
        str_left = new_str
        
    if match_r:
        # replace all occurrances of . in str_right, with their corresponding value in str_left
        for i in range(len(str_right)):
            if str_right[i] == '.':
                new_str += str_left[i]
            else:
                new_str += str_left[i] 
        str_right = new_str
    
    # Remove the padding that was added because of the offset
    if match_offset < 0:  
        str_left = str_left[abs(match_offset) * 2:]      
    else:
        if match_offset > 0:
            str_right = str_right[abs(match_offset) * 2:]
    
    # Replace the .'s with 9's for any remaining unmatched positions, so that they can be picked up in transposed reprocess
    # And undo the order reversal on the right part
    l_part = ''.join(str_left).replace(".","9")
    r_part = ''.join(str_right)[::-1].replace(".","9")
 
    # Reconstruct the row and return it
    return np.array([int(char) for char in (l_part + r_part)])

def rows_iteration(solve_matrix):
    """ 
    solve_matrix: A 2-D numpy array of integers.
    
    Returns: A 2-D numpy array containing any resolved 9 values
    
    Component of solve_3631a71a
    
    Iterate through each row of solve_matrix and using symmetrical matching between the two 'halves; of the row,
    solve for any 9's that appear in the string"""
    
    # Initialise the return array
    # We build and return a new array rather than modifying the original in-place
    new_array = np.array([])
    mask_val = 9 # We are searching for 9's

    for row in solve_matrix:
        if mask_val in row:
            # The row contains 9's - missing squares. So we have to solve to replace the 9's with another value
            new_row = solve_row(row)
            new_array = np.append(new_array, new_row, axis=0)
        else:
            # The row has no missing squares, so just add it to the return matrix
            new_array = np.append(new_array, row, axis=0)
    
    # reshape and return the new, updated np array
    return new_array.astype(int).reshape(solve_matrix.shape)

def solve_3631a71a(x):
    """ 
    Controlling function to solve 3631a71a
    
    Here is the procedure to solve:
        1. For each row in the input matrix x, that has missing cells (contains value = 9)
            2. Find the midpoint of the row which can be offset by three cells left or right of the centre of the row
            3. Split the row at the midpoint. If there are 9's on both the left and right side of the row, we cannot solve this row so move to the next row.
               Rows of this nature will be solved by the column-wise match in step 2 below
            4. Reverse the order of the second part of the row
            5. The side (left or right) that contains 9's becomes the search string in a regex expression - replace any 9's with a period (.) which will match 
               any character on the opposite side
            6. solve the missing cells by their opposite counterpart in the other half of the row
        2. For each column in the input matrix x, that has missing cells (contains value = 9), repeat the same procecdure.This is achieved by transposing x and 
           running the row-wise algorithym again.
    """ 
    
    # Loop through every row in the input matrix.
    # Solve as many 9's as possible using row symmetrical matching
    new_matrix = rows_iteration(x)

    # Any rows containing 9's on both 'halves', or rows containing 9's in the beginning or end of the row
    # may fail to match depending on where the central offset lies
    # To address this, transpose the resultant matrix and re-run the rows_iteration function to attempt to resolve
    # any remaining 9's
    new_matrix2 = rows_iteration(new_matrix.T).T
    
    return new_matrix2

    
def solve_a3325580(x):
    """ 
    Controlling function to solve a3325580
    
    Here is the procedure to solve:
        1. For each non-black cell in x ( cell value <> 0)
            a. Record that color, in the order it was detected
            b count how many cells that color exist in x and record that
       
        2. Find the color with the highest number of cells (there may be multiple) and choose that
           number, H1, as the number of rows in the output
        3. Each color, having the same number of cells = H1 will be output as a complete column in the output matrix
        4. The order of the rows in the output is the same as the order in which the colors were detected in the input matrix

    """ 
    
    # Determine how many unique values in the matrix and the frequency of occurrence of each, ignoring zeros
    val, val_count = np.unique(x, return_counts=True)
    res = {val[i]: val_count[i] for i in range(len(val))if val[i] > 0}
    max_count = max(res.values())
    
    # Find the order of appearance of the colors in the input. We go be column order not row order
    cols,rows = x.shape
    results = np.array([])
    lst = []
    for y in range(cols):
        for val in x[:,y]:        
            if val > 0 and val not in lst and res[val] == max_count:
                lst.append(val)
                if len(lst) == 1:
                    results = np.ones(max_count) * val              
                else:
                    results = np.vstack((results, np.ones(max_count) * val))
    
    return results.T.astype(int)

def get_adjacent_cells(row, color):
    """ 
        row:    A one-D numpy array
        color: The color we want to match
        
        returns: A one-D matrix, of the subset of row that have adjacent cells = color
        For each cell in row, if the cell matches color, add it to the return row
        Component of solution for solve_228f6490
     
        >>> get_adjacent_cells([5,5,5,6,0,0], 5)
            [5,5,5]
        >>> get_adjacent_cells([5,0,5], 5)
            [5]
        >>> get_adjacent_cells([5,0,5], 4)
            []

    """ 
    
    # Initialise the return row
    ret_rw = np.array([])
    for cell in row:    
        if cell != color: 
            # No more adjacent dells, so we are done
            break
        ret_rw = np.append(ret_rw,color).astype(int)
            
    return ret_rw

def check_row_below(this_row, row, col, this_color, x, y, matrix):
    """ 
    this_row:   The 'parent' row that we are trying to find adjacent colors in the row below for
    row,col:    The x,y co-ordinates of this_row in the input matrix
    this_color: The color we are trying to match
    x, y:       The width and height of the parent matrix
    
    returns:   Boolean Found True/False depending if there is an adjacent row below
               The adjacent row (row below this_row) which will be empty if Found is False
               The start_col of the color we are seeking in the adjacent row (row below this_row). 
               
    Given a row representing row 1 sub-shape, check the row below for the presence of additional adjacent cells whilst ensuring 
    we stay within the bounds of x,y of the overall input matrix
    
    Component of solution for solve_228f6490
    
    >>> check_row_below([3,3,3], 5, 0, 3, 10, 10, np.array([[ 5, 5, 5, 5, 5, 0, 0, 0, 0, 0 ],
            [ 5, 0, 0, 0, 5, 0, 9, 9, 9, 9 ],
            [ 5, 5, 5, 0, 5, 0, 9, 9, 9, 9 ],
            [ 5, 5, 5, 5, 5, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 6, 0, 6 ],
            [ 3, 3, 3, 0, 0, 0, 6, 6, 0, 0 ],
            [ 0, 0, 3, 5, 5, 5, 5, 5, 5, 0 ],
            [ 0, 0, 0, 5, 0, 0, 0, 0, 5, 0 ],
            [ 6, 6, 0, 5, 0, 0, 0, 0, 5, 0 ],
            [ 6, 6, 0, 5, 5, 5, 5, 5, 5, 0 ]
          ] )
        True, [0,0,3], 0

    >>> check_row_below([6], 4, 7, 6, 10, 10, np.array([[ 5, 5, 5, 5, 5, 0, 0, 0, 0, 0 ],
            [ 5, 0, 0, 0, 5, 0, 9, 9, 9, 9 ],
            [ 5, 5, 5, 0, 5, 0, 9, 9, 9, 9 ],
            [ 5, 5, 5, 5, 5, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 6, 0, 6 ],
            [ 3, 3, 3, 0, 0, 0, 6, 6, 0, 0 ],
            [ 0, 0, 3, 5, 5, 5, 5, 5, 5, 0 ],
            [ 0, 0, 0, 5, 0, 0, 0, 0, 5, 0 ],
            [ 6, 6, 0, 5, 0, 0, 0, 0, 5, 0 ],
            [ 6, 6, 0, 5, 5, 5, 5, 5, 5, 0 ]
          ] )
        True, [6,6], 6
    >>> check_row_below([6], 4, 9, 6, 10, 10, np.array([[ 5, 5, 5, 5, 5, 0, 0, 0, 0, 0 ],
            [ 5, 0, 0, 0, 5, 0, 9, 9, 9, 9 ],
            [ 5, 5, 5, 0, 5, 0, 9, 9, 9, 9 ],
            [ 5, 5, 5, 5, 5, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 6, 0, 6 ],
            [ 3, 3, 3, 0, 0, 0, 6, 6, 0, 0 ],
            [ 0, 0, 3, 5, 5, 5, 5, 5, 5, 0 ],
            [ 0, 0, 0, 5, 0, 0, 0, 0, 5, 0 ],
            [ 6, 6, 0, 5, 0, 0, 0, 0, 5, 0 ],
            [ 6, 6, 0, 5, 5, 5, 5, 5, 5, 0 ]
          ] )
        False, [], 9

    
    """
    # initialise the return variable
    next_row = np.array([])
    
    # Determine the start column
    # If the start column of the first row is column 0 in the overall matrix, then we cannot check for an adjacent cell
    # in the cell below-left
    if col > 0: 
        # Check for one cell below and to the left of this_row start column
        start_col = col  - 1           
    else:
        # Check for one cell below this-row start column - we are already in column 0 so we cannot check below left
        start_col = col 
        
    # Determine the end column
    # If the end column of the first row is the last column in the overall matrix, then we cannot check for an adjacent cell
    # in the cell below-right of the last cell in this_row
    if col < y:
        end_col = col + len(this_row)
    else:
        end_col = col + len(this_row)-1
    
    # Check if the color we are looking for exists in the row below, within the bounds of start_col and end_col
    # If there is not, return False and an empty array
    if not this_color in matrix[row+1,start_col:end_col]:
        return False, next_row, start_col
    
    # We have the matching color between start_col and end_col so we need to extract it
    candidates = matrix[row+1,start_col:end_col+1]

    if start_col != col:
        # Our first candidate cell of the next row is in the column preceeding the first cell of this row 
        if candidates[0] == this_color:
            next_row = np.append(next_row,candidates[0]).astype(int) # If the color matches, add it
        else:
             start_col += 1 # Else, discard this cell as it is not matching
    else:
        # We append the cell, even if it is not matching the color, because we want our shapes to be parallelograms
        next_row = np.append(next_row,candidates[0]).astype(int) 
    
    # Append the mid-section even if it is not matching the color   
    next_row = np.append(next_row, candidates[1:-1]).astype(int)
    
    # Append the last cell, only if the color matches
    if candidates[-1] == this_color:
        next_row = np.append(next_row, candidates[-1]).astype(int)

    return True, next_row, start_col


def extract_grey_shapes(x):
    """
    x: Numpy array,
    
    Take a 2 dimensional array.  Parse it as follows:,
    1. Ignore black space (value 0),
    2. For every grey shape present in the grid, extract an n x m matrix to represent that shape as a sub-grid, along with the position of that grey
       shape in the input matrix x
    3. Along with each grey parent shape, extract the color, position and size of the sub-shape within the grey shape, this is the shape we will 
       use to match against the candidate non-grey shapes later
   
    Returns: 
        (1) An array for each grey shape found  in x: 
                x and y co-ordinate of top left corner
                Color
                matrix representing the grey subshape
                An array representing the non-grey sub-shape embedded in the grey shape
                    x and y co-ordinate of top left corner (with respect to the grey sub-shape, as opposed to x)
                    Color
                    matrix representing the non-grey sub-shape. This will be a parallelogram with 0 for cells that are not in the color of the sub-shape
          (2) An updated copy of the input x, where each grey sub-shape has been removed and replaced with zeros          
    
       Component of solution for solve_228f6490
    
    >>> extract_grey_shapes(np.array([[ 5, 5, 5, 5, 5, 0, 0, 0, 0, 0 ],
            [ 5, 0, 0, 0, 5, 0, 9, 9, 9, 9 ],
            [ 5, 5, 5, 0, 5, 0, 9, 9, 9, 9 ],
            [ 5, 5, 5, 5, 5, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 6, 0, 6 ],
            [ 3, 3, 3, 0, 0, 0, 6, 6, 0, 0 ],
            [ 0, 0, 3, 5, 5, 5, 5, 5, 5, 0 ],
            [ 0, 0, 0, 5, 0, 0, 0, 0, 5, 0 ],
            [ 6, 6, 0, 5, 0, 0, 0, 0, 5, 0 ],
            [ 6, 6, 0, 5, 5, 5, 5, 5, 5, 0 ]]))
    
    [[0, 0, 5, array([[5, 5, 5, 5, 5],
          [5, 0, 0, 0, 5],
          [5, 5, 5, 0, 5],
          [5, 5, 5, 5, 5]]), [[1, 1, 1, array([[1, 1, 1],
            [0, 0, 1]])]]], [6, 3, 5, array([[5, 5, 5, 5, 5, 5],
          [5, 0, 0, 0, 0, 5],
          [5, 0, 0, 0, 0, 5],
          [5, 5, 5, 5, 5, 5]]), [[1, 1, 1, array([[1, 1, 1, 1],
            [1, 1, 1, 1]])]]]], 
    array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 9, 9, 9],
        [0, 0, 0, 0, 0, 0, 9, 9, 9, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0, 6],
        [3, 3, 3, 0, 0, 0, 6, 6, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 6, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 6, 0, 0, 0, 0, 0, 0, 0, 0]]
          
    
    

    """
    # Take a copy of X. Each time we extract a shape, we will set the cells of its location black in our copy, this way we know,
    # to ignore it next time around
    e_x = np.copy(x)
    x,y = e_x.shape 
    return_shapes = []
    grey = 5
    
    # Repeat until we have no grey shapes left to extract (all cells in e_x are <> 5) 
    while grey in e_x:
        
        # Find the first row with a grey value
        for i in range(x):
            if grey in e_x[i]:  
                row = i
                break

        for col in range(y):
            if e_x[row,col] != grey: 
                continue
            # We have found a grey shape. Now we need to determine its height and width
            # initialise the attributes
            this_color = grey
            x_ind = row
            y_ind = col

            this_shape = np.array([])

            # Get the top row - this will give us the length
            top_row = get_adjacent_cells(e_x[row,col:], grey)
            # Get the left side - this will give us the height
            left_col = get_adjacent_cells(e_x[row:,col], grey)
            
            # Extract the grey matrix - this_shape - from the input matrix
            width = len(top_row)
            height = len(left_col)
            this_shape = np.array(e_x[x_ind:height + x_ind, y_ind:width + y_ind])
            
            # Set the cells occupied by this_shape to 0's on the parent matrix, so we don't try to include it again
            e_x[x_ind:height + x_ind, y_ind:width + y_ind] = 0
            
            # find the dimensions and position of the subshape within the grey matrix
            tmp_shape = np.where(this_shape==0, 1, this_shape)
            tmp_shape = np.where(tmp_shape==5, 0, tmp_shape)
            embedded_shape, z = extract_non_grey_shapes(tmp_shape)
        
        # Add this grey matrix, and its embedded shape, to our return array
        return_shapes.append([x_ind,y_ind,this_color, this_shape, embedded_shape])
        
    return return_shapes, e_x

def extract_non_grey_shapes(x):
    """
    x: Numpy array,
    
    Take a 2 dimensional array.  Parse it as follows:,
    1. Ignore black space (value 0)
    2. For every shape present in the grid, extract an n x m matrix to represent that shape as a sub-grid, along with the position of that 
       shape in the input matrix x

   
    Returns: 
        (1) An array for each  shape found  in x: 
                x and y co-ordinate of top left corner
                Color
                matrix representing the subshape
                
          (2) An updated copy of the input x, where each sub-shape has been removed and replaced with zeros          
    
       Component of solution for solve_228f6490
       
       >>> extract_non_grey_shapes(np.array(array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   
        [0, 0, 0, 0, 0, 0, 9, 9, 9, 9],
        [0, 0, 0, 0, 0, 0, 9, 9, 9, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0, 6],
        [3, 3, 3, 0, 0, 0, 6, 6, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 6, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 6, 0, 0, 0, 0, 0, 0, 0, 0]]))
    
        [[1, 6, 9, array([[9, 9, 9, 9],
         [9, 9, 9, 9]])], 
         [4, 6, 6, array([[0, 6], [6, 6]])], 
         [4, 9, 6, array([6])], 
         [5, 0, 3, array([[3, 3, 3],[0, 0, 3]])], 
         [8, 0, 6, array([[6, 6],[6, 6]])]]
    
         array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    """

    # Take a copy of X. Each time we extract a shape, we will set the cells of its location black in our copy, this way we know,
    # to ignore it next time around,
    e_x = np.copy(x)
    x,y = e_x.shape 
    return_shapes = []
    
    # Repeat until we have no shapes left to extract (all cells in e_x are zero) 
    while np.sum(e_x) > 0:

        # Find the first row with a non-zero value
        for i in range(x):
            if np.sum(e_x[i]) > 0:  
                row = i
                break

        for col in range(y):
            if e_x[row,col] == 0: 
                continue

            # We have found a non-black shape. Now we need to determine its matrix and color,
            # initialise the attributes
            this_color = e_x[row,col]
            x_ind = row
            y_ind = col
            this_shape = np.array([])

            # We know there are never any cases more than 2 rows from the test data
            # This could be enhanced in future to cater for shapes more than 2 rows in height but for now we assume only 1 or 2 row height max
            # Search the rest of this row for matching adjacent color cells
            this_row = get_adjacent_cells(e_x[row,col:], this_color)
            next_row = []

            if row < x-1: # Check for adjacent cells in the row below
                is_another_row, next_row, start_col = check_row_below(this_row, row, col, this_color, x,y, e_x)
            break
        
        # Check if we need padding
        if is_another_row:
            if start_col < y_ind:
                # pad one space to the left of this_row and adjust y_ind
                y_ind -= 1
                this_row = np.append([0], this_row)
    
            if len(this_row) - len(next_row) < 0: 
                this_row = np.append(this_row, np.array([0] * (abs(len(this_row) - len(next_row)))))
                
            this_shape = np.append(this_row, next_row)
            this_shape = np.reshape(this_shape,(2,len(this_row)))
        else:       
            this_shape = this_row

        e_x [x_ind,y_ind:len(this_row)+ y_ind] = 0 
        
        if len(next_row) > 0:
            e_x [x_ind+1,y_ind:len(this_row)+ y_ind] = 0 
        
        return_shapes.append([x_ind,y_ind,this_color, this_shape])
       
    return return_shapes, e_x

def solve_228f6490(x):
    """
    Controlling function to solve_228f6490 
    
    Here is the procedure to solve: 
        1. Identify all of the grey squares or rectangles in the input matrix x
        2. For each one, note:
            a.its location in x - co-ordinates of cell (0,0) with respect to x
            b the sub-matrix that represents it
            c.the embedded target shape within it as
                - the embedded shape location in the grey shape, co-ordinates of (0,0) with respect to the grey container shape
                - the sub-matrix that represents the embedded shape. This is forced to be an n x m matrix with any extra cells holding the value 0
        3. Identify all of the non-grey shapes in the input matrix x
        4. For each one, note:
            a.its location in x - co-ordinates of cell (0,0) with respect to x
            b the sub-matrix that represents it. This is forced to be an n x m matrix with any extra cells holding the value 0
        5. For each grey square or triangle
            a. Find the list of candidate non-grey shapes that match the embedded target shape within the grey parallelogram
            b. For each candidate, calculate the euclidian distance between point 0,0 of the grey shape, and point 0,0 of the candidate shape, with respect to x
            c. Choose the candidate that matches the target shape and is closed to the grey square
        6. Replace the cells of the embedded shape in the grey parallelogram with the cells of the chosen candidate shape
        7. Remove the chosen candidate shape from the list of non-grey shapes
        8. When all of the grey parallelograms have been solved, re-construct the x matrix for output, which will show the moved shapes as required. 
        
    """
    
    # Extract the grey shapes 
    grey_shapes, x = extract_grey_shapes(x)
    # Extract the grey shapes 
    non_grey_shapes, x = extract_non_grey_shapes(x)
    # x will now be a xero-filled matrix  

    # For each grey shape, find the candidate non-grey shape whose x,y size will fit within its sub-shape
    for g_shape in grey_shapes:
        candidates = []
        target = g_shape[4][0]
        target_shape = target[3].shape
        
        # Find the candidate matches
        # Loop through all the non-grey shapes. Find any whose shape matches the shape of the sub-shape within the grey we are trying to solve
        for i in range(len(non_grey_shapes)):
            candidate = non_grey_shapes[i]
            candidate_shape = candidate[3].shape    
            if candidate_shape != target_shape:
                continue
            # We have a candidate. In case there are more than one candidate we will choose the one closest to the grey shape
            # Calculate euclidian distance from the grey target shape to our candidate sub-shape and add to our candidate list
            dist = np.linalg.norm(  np.array([target[0], target[1]]) - np.array([candidate[0], candidate[1]]))
            candidates.append([i, dist])
        
        # If none of the sub-shapes match, we cannot solve this grey_shape, so continute to the next iteration
        if (len(candidates)) == 0:
            continue
        
        # If we have more than one candidate, choose the one that is closest to the target
        chosen_candidate = candidates[0]
        dist = chosen_candidate[1]
        for candidate in candidates:
            if candidate[1] < dist:
                chosen_candidate = candidate
                dist = chosen_candidate[1]
        
        # Replace the target sub-shape in the grey shape with the chosen candidate   
        if len(target_shape) == 1:
            width = target[3].shape[0]
            height = 1
        else:
            height, width = target[3].shape
            
        # Overlay the chosen non-grey shape into the target area within the grey
        g_shape[3][target[0]:target[0] + height,target[1]:target[1] + width] = non_grey_shapes[chosen_candidate[0]][3]
        
        # Reset any 0's introduced  - where the candidate shape is not a parallelogram there will be 0's padding the matrix
        # So set these back to grey
        g_shape[3][target[0]:target[0] + height,target[1]:target[1] + width] = np.where(g_shape[3][target[0]:target[0] + height,target[1]:target[1] + width]==0, 5, g_shape[3][target[0]:target[0] + height,target[1]:target[1] + width])
        
        # Remove the candidate shape from the non_grey_shapes array, because we don't want to re-draw that when we reconstruct the matrix
        # And we cannot re-use it to solve a future grey shape
        non_grey_shapes = np.delete(non_grey_shapes, chosen_candidate[0], axis = 0)
    
        # Add the updated grey shape, with its new color sub-shape, back into the original matrix
        height, width = g_shape[3].shape
        x[g_shape[0]:g_shape[0] + height, g_shape[1]:g_shape[1] + width] = g_shape[3]
    
    
    # Add the remaining non-grey shapes back into the original matrix 
    for shape in non_grey_shapes:
        if len(shape[3].shape) == 1:
            width = shape[3].shape[0]
            height = 1
        else:
            height, width = shape[3].shape
    
        x[shape[0]:shape[0] + height, shape[1]:shape[1] + width] = shape[3]
    
    return x


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()

