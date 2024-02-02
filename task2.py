#проще работать с матрицей, если ее транспонировать (просто с индексами понятнее)
import copy

def main():
    a = [0 for i in range(17)]
    matrix = [copy.copy(a) for i in range(10)]

    with open("2.txt") as f:
        for n, b in enumerate(map(float, f.readlines())):
            matrix[0][n+1] = b

    # print(matrix)
    for j in range(9):
        for i in range(15):
            matrix[j+1][i+1] = (matrix[j][i+2] + matrix[j][i])/2
            
    print(matrix)

main()