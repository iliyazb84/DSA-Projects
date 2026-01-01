def Hanoi(n,source,target,spare):
    if n==1:
        print(f"Move disk 1 from {source} to {target} ")
        return
    Hanoi(n-1,source,spare,target)
    print(f"Move disk {n} from {source} to {target}")
    Hanoi(n - 1, spare, target, source)

disks=4
Hanoi(disks,'A','C','B')