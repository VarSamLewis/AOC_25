import numpy as np


FILENAME = 'input.txt'

def fileread(filename: str, debug: bool = False) -> np.array:
    with open(filename, 'r') as f:
        array = np.array([[1 if char == '@' else 0 for char in line.strip()] 
                      for line in f], dtype=int)
    if debug == True:
        print(f"Array shape: {array.shape}")  # Debug line
        print(f"Array type: {type(array)}")    # Debug line
    return array

def gridsearch(grid: np.array, debug: bool = False) -> int:
    accessible = 0

    directions = [(di, dj) for di in [-1, 0, 1] for dj in [-1, 0, 1] if not (di == 0 and dj == 0)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if debug == True: 
                print(f"Searching cells: {i, j}")
        
            if grid[i][j] == 1:
                adjacent_paper_count = 0
            
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if debug == True:
                        print(f"Searching neighbouring cells: {ni, nj}")
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        adjacent_paper_count += grid[ni][nj]
            
                if adjacent_paper_count < 4:
                    accessible += 1
    
    if debug == True:
        print(f"Accessible cells: {accessible}")
        print(f"Directions to search: {directions}")
    return accessible

def main():
    array = fileread(FILENAME)
    result = gridsearch(array)
    print(f"Accessible paper rolls: {result}")
    return result

if __name__ == '__main__':    
    main()



    

