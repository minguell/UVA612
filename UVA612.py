# DNA Sorting
import sys

def main():
    T = int(input())
    for t in range(T):
        n, m = map(int, input().split())
        input()  # Consuma a linha em branco após m
        temp = [input() for _ in range(m)]
        dis = [0] * m

        for i in range(m):
            for j in range(n - 1):
                for k in range(j + 1, n):
                    if temp[i][j] > temp[i][k]:
                        dis[i] += 1

        while True:
            min_dis = 10000
            pos = 0
            for i in range(m):
                if dis[i] < min_dis:
                    pos = i
                    min_dis = dis[i]
            dis[pos] = 10000
            if min_dis == 10000:
                break
            print(temp[pos])

        if t < T - 1:
            print()

if __name__ == "__main__":
    main()
