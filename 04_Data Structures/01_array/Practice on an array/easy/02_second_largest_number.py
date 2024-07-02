def findSecondLargest(sequenceOfNumbers):
    ele = set(sequenceOfNumbers)
    last = sorted(ele)
    if len(last) == 1:
        return -1
    else:
        return last[len(last) - 2]
    pass


# Taking input using fast I/O.
def takeInput():
    n = int(input())
    sequenceOfNumbers: list[int] = list(map(int, input().strip().split(" ")))
    return sequenceOfNumbers, n


# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t - 1
