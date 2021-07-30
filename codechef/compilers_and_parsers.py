n = int(input())
while (n):
    l = list(input())
    a = c = 0
    ans = 0
    st = []
    for i in l:
        if i == "<":
            c += 1
            st.append(i)
        elif i == ">":
            if not st:
                break
            elif st:
                st.pop()
                if not st:
                    ans = ans + c * 2
                    c = 0

    print(ans, end="")
    n -= 1
    if n:
        print()