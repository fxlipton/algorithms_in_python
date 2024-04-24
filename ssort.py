def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        print(array)

def selectionSort_desc(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] > array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        print(array)

data = [8,19,1,20,2,18,5,11,4]
size = len(data)
selectionSort_desc(data, size)
