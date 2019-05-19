def TowerOfHonoi(n, fromR,toR,auxR):
    if n==1:
        print("Move disk 1", fromR, "to rod", toR)
        return
    TowerOfHonoi(n-1, fromR, auxR, toR)
    print("Move disk ", n, "from rod", fromR, "to rod ", toR)
    TowerOfHonoi(n-1, toR, auxR, fromR)
n=3
TowerOfHonoi(3, 'A', 'C', 'B')
