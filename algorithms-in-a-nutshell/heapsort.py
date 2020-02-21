import math

def sort(arr):
  buildHeap(arr)
  for i in range(len(arr) - 1, 0, -1):
    temp = arr[0]
    arr[0] = arr[i]
    arr[i] = temp
    heapify(arr, 0, i)
    
  return arr

def buildHeap(arr):
  
  for i in range(len(arr), -1, -1):
    heapify(arr, i, len(arr))

def heapify(arr, index, max):
  largest = index
  left = 2 * index + 1
  right = 2 * index + 2
  print("left: " + str(left) + "\tright: " + str(right) + "\tlargest: " + str(largest))
  print(arr)
  print('heapifying ' + str(index) + ',' + str(max))
  if (left < max and arr[left] > arr[index]):
    largest = left
  if(right < max and arr[right] > arr[largest]):
    largest = right
  if(largest != index):
    temp = arr[index]
    arr[index] = arr[largest]
    arr[largest] = temp
    heapify(arr, largest, max)

def printHeap(arr):
  #because of the shape property the depth is always log2(n)
  depth = math.ceil(math.log2(len(arr)))
  shouldBreak = False
  for i in range(0, depth):
    for j in range(0, 2 ** i):
      index = j + ( 2 ** i) - 1
      if(index >= len(arr)):
        shouldBreak = True
    
    if shouldBreak:
      break

    
    print()

  return

arr = [8, 11, 9, 2, 10, 16]
sort(arr)
print(arr)
printHeap(arr)


