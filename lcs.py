def lcs(X, Y, m, n):
    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1): 
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    print(L)
    return L[m][n]

if __name__ == '__main__':
    S1 = "KTO"
    S2 = "KOAN"
    m = len(S1)
    n = len(S2)
    print("Length of LCS is", lcs(S1, S2, m, n))