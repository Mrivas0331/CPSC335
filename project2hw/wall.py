from collections import deque

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_nearest_stronghold(cities, x, y):
  m, n = len(cities), len(cities[0])
  q = deque()
  q.append((x, y, 0))
  while q:
    i, j, distance = q.popleft()
    if cities[i][j] == 0:
      return distance
    for dx, dy in directions:
      # Calculates distance
      new_i, new_j = i + dx, j + dy
      if new_i not in range(m) or new_j not in range(n) or cities[new_i][new_j] == -1:
        continue
      q.append((new_i, new_j, distance + 1))
  return -1


def nearest_cities(cities):
  # Initializes array
  m, n = len(cities), len(cities[0])
  for i in range(m):
    for j in range(n):
      # Runs through the separate function to find nearest stronghold
      if cities[i][j] == float('inf'):
        cities[i][j] = find_nearest_stronghold(cities, i, j)

def test():
  test_input = [
    [0, float('inf'), float('inf')],
    [-1, -1, float('inf')],
    [-1, -1, float('inf')],
  ]
  for r in test_input:
    print(r)
    print("\n")

  print("Output:\n")
  nearest_cities(test_input)
  for r in test_input:
    print(r)

if __name__ == '__main__':
  test()