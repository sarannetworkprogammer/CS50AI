

s ="aaa"
count = 0

for i in range(len(s)):
    print(f" {i} th iteration")
    l, r = i,i
    print(f"l ={l}, r={r}")

    print(f"s[l]={s[l]}, s[r] ={s[r]}")

    while l >= 0 and r < len(s) and s[l] == s[r]:
        count = count + 1
        l -= 1
        r += 1

        print(f"l ={l}, r={r}")

    l, r = i , i +1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        count = count + 1
        l -= 1
        r += 1

        print(f"l ={l}, r={r}")




    # even palidronmes

 
