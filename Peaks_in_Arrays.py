def find_peaks(array):
    peak = []
    num = len(array)
    for i in range(1, num - 1):
        if array[i] > array[i -1] and array[i]>array[i+1]:#checking if both left and right element is less than current element
            peak.append(i)
    return peak

input_string = input("Enter a list of numbers separated by spaces: ")
input_list = list(map(int, input_string.split()))
peaks_indices = find_peaks(input_list)
print("Peaks found at indices:", peaks_indices)