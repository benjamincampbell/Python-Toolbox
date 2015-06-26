class mergesorter:

    def __init__(self, array):
        self._array = array
        self.sort(self._array, 0, len(self._array) - 1)

    def sort(self, array, low, high):
        if (low < high):
            mid = low + (high - low) // 2
            self.sort(array, low, mid)
            self.sort(array, mid + 1, high)
            self.merge(array, low, mid, high)

    def merge(self, array, low, mid, high):
        i = low
        j = mid + 1
        temp = list(array)
        #array will be the final array, temp will be the original to compare against
        #loop the number of times between low and high
        for k in range(low, high + 1):
            #if i (low) is greater than mid, we are at the end of the first subarray
            if (i > mid):
                array[k] = temp[j]
                j += 1
            else:
                #if j (mid+1) is greater than high, it means we are at the end of the second subarray
                if (j > high):
                    array[k] = temp[i]
                    i += 1
                else:
                    #if the element at j is less than the element at i, insert j
                    if (temp[j] < temp[i]):
                        array[k] = temp[j]
                        j += 1
                    #else (the element at j is greater or equal to element at i, insert i
                    else:
                        array[k] = temp[i]
                        i += 1

    def __str__(self):
        return str(self._array)

if __name__ == "__main__":
    unsorted_array = [7, 4, 5, 1, 3, 9, 2, 0]
    print("Before sort:")
    print(unsorted_array)
    print("After sort:")
    sorted_array = mergesorter(unsorted_array)
    print(sorted_array)