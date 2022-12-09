def making_change(x, v, k):
    K = [0] * (v+1)
    S = [-1] * (v+1)
    n = len(x)

    K[0] = 1 # base case, coins for '0' amount can always be given

    for w in range(1, v+1, 1):
        for c in range(n):
            # print(f"x[c]: {x[c]}, w: {w}")
            if x[c] <= w and K[w-x[c]] == 1:
                # print(f"--> w = {w}, c = {c}")
                K[w] = 1
                S[w] = c
    
    # print(f"K: {K}")
    # print(f"S: {S}")
    
    # Determine if more than 'k' coins were needed
    # and print which coin was used
    print("Coin(s) used: ", end='')
    i = len(S) - 1
    while i >= 0:
        if S[i] >= 0:
            k = k - 1
            print(f"{x[S[i]]} ", end='')
            
            i -= x[S[i]] # jump to value of next used coin
        else:
            i -= 1
    print()
    print(f"Value of k: {k}")
    
    return True if (k > 0) else False

def main():
    x = [5,10]
    k = 6
    v = 65
    print(f"x: {x}, k: {k}, v: {v}")
    res = making_change(x, v, k)
    print(f"Can make {v} with less than or equal to {k} coins: {res}")
    
    print()
    
    x = [5,10]
    k = 6
    v = 55
    print(f"x: {x}, k: {k}, v: {v}")
    res = making_change(x, v, k)
    print(f"Can make {v} with less than or equal to {k} coins: {res}")
    
    print()
    
    x = [1,5,10,25]
    k = 6
    v = 54
    print(f"x: {x}, k: {k}, v: {v}")
    res = making_change(x, v, k)
    print(f"Can make {v} with less than or equal to {k} coins: {res}")

main()