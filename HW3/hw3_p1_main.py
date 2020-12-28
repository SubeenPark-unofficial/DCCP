### TODO: hw3_p1.py에서 'mean', 'median', 'mode', stdev', 'variance' function을 완성하세요.

from hw3_p1 import *

if __name__ == "__main__":

    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Standard Deviation")
    print("5. Variance")

    num = int(input("Select Number: "))

    if 'data' not in dir():
        data = [1, 1, 2, 3, 3, 3, 3, 4]


    if num == 1:
        result = mean(data)
    elif num == 2:
        result = median(data)
    elif num == 3:
        result = mode(data)
    elif num == 4:
        result = stdev(data)
    elif num == 5:
        result = variance(data)

    print(result)



