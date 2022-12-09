def johnDoeWoe():
    list = []
    for x in range (4):
        list.append(input())

    print(list[1])
    print(list[0])
    print(list[2])
    print(list[3])

def squidGame():
    dict = {"RED LIGHT, GREEN LIGHT" : 1, "DALGONA CANDY" : 2, "TUG OF WAR" : 3, "MARBLES" : 4, "GLASS BRIDGE" : 5, "SQUID GAME" : 6}
    n = input().upper()

    if n in dict:
        print("$", (2**(dict[n]-1) * 5000))

def fib():
    n = int(input())
    i = 1
    j = 1
    for x in range(n - 2):
        z = i
        i = i + j
        j = z

    print(i)
