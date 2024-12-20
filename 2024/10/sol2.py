import collections
import timeit

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def traverse_head(head):
    q = collections.deque()
    q.append([head])
    paths = set()
    while q:
        curr_path = q.popleft()
        curry, currx = curr_path[-1]
        curr_val = grid[curry][currx]
        if curr_val == 9:
            paths.add(tuple(curr_path))
            continue

        for dy, dx in dirs:
            nexty, nextx = curry + dy, currx + dx
            if nexty in range(Y) and nextx in range(X):
                next_val = grid[nexty][nextx]
                if next_val == ".":
                    continue
                if grid[nexty][nextx] == curr_val + 1:
                    next_paths = curr_path.copy()
                    next_paths.append((nexty, nextx))
                    q.append(next_paths)

    return len(paths)


def f():
    global grid, Y, X
    with open('input.txt') as f:
        lines = f.read().splitlines()
        grid = [[int(x) if x.isdigit() else x for x in list(l)] for l in lines]
        # print(grid)
        Y = len(grid)
        X = len(grid[0])
        heads = []
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == 0:
                    heads.append((y, x))
        # print(heads)


    count = 0
    for head in heads:
        count += traverse_head(head)

    print(count)
    return count


if __name__ == '__main__':
    iters = 1000
    x = timeit.timeit(lambda: f(), number=iters)
    print(f"{x / iters: 0.4f} s")
