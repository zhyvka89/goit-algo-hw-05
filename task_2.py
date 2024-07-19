def binary_search(arr, x):
  low = 0
  high = len(arr) - 1
  count = 0
  upper_x = None

  while low <= high:
    count += 1
    mid = (high + low) // 2

    if arr[mid] < x:
      low = mid + 1

    elif arr[mid] > x:
      high = mid - 1
      upper_x = arr[mid]

    else:
      return (count, arr[mid])
      
  return (count, upper_x)


arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
x = 2.6
result = binary_search(arr, x)
print(result)