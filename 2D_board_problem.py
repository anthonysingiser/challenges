# Given a 2D board of characters and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# For example, given the following board:

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# exists(board, "ABCCED") returns true, 
# exists(board, "SEE") returns true, 
# exists(board, "ABCB") returns false.

example_board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

def find_all_coordinates_of_letter_in_grid(grid, letter):
    coordinates_of_letter = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if letter == grid[x][y]:
                coordinates_of_letter.append([x, y])
    return coordinates_of_letter

def find_nearby_coordinates(list_of_coordinates):
    for coordinate in list_of_coordinates:
        print(coordinate)

find_nearby_coordinates(find_all_coordinates_of_letter_in_grid(example_board, 'E'))



