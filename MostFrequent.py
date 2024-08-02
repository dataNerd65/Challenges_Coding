def mostFrequent(arr, n):
    maxCount = 0
    elementMaxFrequency = 0

    for i in range(0, n):
        count = 0
        for j in range(0, n):
            if (arr[i] == arr[j]):
                count += 1
        if (count > maxCount):
            maxCount = count
            elementMaxFrequency = arr[i]
    return elementMaxFrequency, maxCount

arr = [40, 50, 30, 40, 50, 30, 30]
n = len(arr)
element, frequency = mostFrequent(arr, n)
print(f"The most frequent element is {element} and it appears {frequency} times.")


        