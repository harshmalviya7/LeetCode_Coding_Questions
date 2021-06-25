
def tower(n,source,destination,helper):
    if n==0:
        return

    tower(n-1,source,helper,destination)
    print(f"Move from {source} to {destination}")
    tower(n-1,helper,destination,source)

tower(3,"A","C","B")