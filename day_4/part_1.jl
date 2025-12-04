function read_grid(filename)
  lines = readlines(filename)
  nrows = length(lines)
  ncols = length(lines[1])
  matrix = zeros(Int, nrows, ncols)
  for (i, line) in enumerate(lines)
    for (j, char) in enumerate(line)
      matrix[i,j] = (char == '@') ? 1 : 0
    end 
  end 
  return matrix
end

function grid_search(grid)  # No colon in Julia function definitions
  accessible = 0
  directions = [(di, dj) for di in -1:1 for dj in -1:1 if !(di == 0 && dj == 0)]
  
  nrows = size(grid, 1)
  ncols = size(grid, 2)
  
  for i in 1:nrows  # Julia is 1-indexed, use 1:n not range()
    for j in 1:ncols
      if grid[i, j] == 1
        adjacent_paper_count = 0
        
        for (di, dj) in directions  # No colon after 'in directions'
          ni, nj = i + di, j + dj
          # Check bounds (1-indexed!)
          if 1 <= ni <= nrows && 1 <= nj <= ncols
            adjacent_paper_count += grid[ni, nj]
          end
        end
        
        if adjacent_paper_count < 4
          accessible += 1
        end
      end
    end
  end
  
  return accessible
end

grid = read_grid("input.txt")
result = grid_search(grid)
println(result)
