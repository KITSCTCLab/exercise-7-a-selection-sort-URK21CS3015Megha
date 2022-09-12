from typing import List

def selectionSort(arr, size) -> List[int]:
  for i in range(len(arr)):
    minimum = i
    for j in range(i+1,len(arr)):
      if arr[minimum]>arr[j]:
        minimum=j
    arr[i],arr[minimum] = arr[minimum],arr[i]
  return arr

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
