n = int(input())

tower = [list(range(1, n+1))[::-1], [], []]

def move(initial, end):
    tower[end].append(tower[initial].pop())
    print(initial + 1, end=" ")
    print(end+ 1)

initial = 0
end = 2
aux = 1

def solve(n, initial, aux, end):
    if n == 1:
        move(initial, end)
    else:
        solve(n-1, initial, end, aux)
        move(initial, end)
        solve(n-1, aux, initial, end)

solve(n, initial, aux, end)