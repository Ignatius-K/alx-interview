#!/usr/bin/python3

'''Module defines the island_perimeter method'''


def get_square_perimeter(
    grid,
    height, width,
    row, column
):
    """
    Calculates the perimeter added by one square

    Args:
        grid: the island
    """
    perimeter = 0
    # top
    if row == 0 or grid[row - 1][column] == 0:
        perimeter += 1
    # bottom
    if row == (height - 1) or grid[row + 1][column] == 0:
        perimeter += 1
    # left
    if column == 0 or grid[row][column - 1] == 0:
        perimeter += 1
    # right
    if column == (width - 1) or grid[row][column + 1] == 0:
        perimeter += 1
    return perimeter


def island_perimeter(grid):
    """
    Calculates the perimeter of an island_perimeter

    Args;
        grid: The island as a matrix

    Return:
        (int) The island perimeter
    """
    perimeter = 0
    if grid is None or len(grid) == 0:
        return perimeter
    if len(grid[0]) == 0:
        return perimeter

    height, width = len(grid), len(grid[0])
    for row in range(height):
        for column in range(width):
            if grid[row][column] == 1:
                perimeter += get_square_perimeter(
                    grid,
                    height=height, width=width,
                    row=row, column=column
                )
    return perimeter
