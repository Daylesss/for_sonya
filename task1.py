def fact(n: int):
    if n <= 1:
        return 1
    return n * fact(n - 1)

def exp(x: float, eps: float, n: int = 0):
    if eps <= 0: 
        print("eps must be positive")
        raise Exception
    value = x**n/(fact(n)) 
    if value <= eps:
        return 0
    return value + exp(x, eps, n+1)
 
def main():
    with open("1.txt") as f:
        x = float(f.readline().strip().replace(",", "."))
        for i in range(6):
            print(exp(x, float(f.readline().strip().replace(",", "."))))

main()