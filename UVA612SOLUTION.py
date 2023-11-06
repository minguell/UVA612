def main():
    t = int(input())
    while t > 0:
        m, n = map(int, input().split())
        dna = [input() for _ in range(n)]
        D = []

        for i in range(n):
            sum_inversions = 0
            for j in range(m):
                for k in range(j + 1, m):
                    if dna[i][j] > dna[i][k]:
                        sum_inversions += 1
            D.append((i, sum_inversions))

        D.sort(key=lambda x: (x[1], x[0]))

        print("----------")

        for i, _ in D:
            print(dna[i])

        t -= 1
        if t > 0:
            print("")

if __name__ == "__main__":
    main()
    input("Pressione Enter para sair.")
