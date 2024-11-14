import json
import numpy as np

def flatten_with_groups(array):
    flat_list = []
    index = 0
    for item in array:
        if isinstance(item, list):
            flat_list.extend([(x, index) for x in item]) 
        else:
            flat_list.append((item, index))
        index += 1
    return flat_list

def ranking_matrix(arr_):
    flat_list = flatten_with_groups(arr_)
    arr = np.zeros((10, 10), dtype=int)
    for i in range(10):
        for j in range(10):
            if flat_list[i][1] == flat_list[j][1] or flat_list[i][1] > flat_list[j][1]:
                arr[flat_list[i][0]-1, flat_list[j][0]-1] = 1
            
    return arr.T

def main(file1, file2):
    with open(file1) as file_A:
        ranking_A = json.load(file_A)
    with open(file2) as file_B:
        ranking_B = json.load(file_B)

    arr_A = list(ranking_A)
    arr_B = list(ranking_B)
    result_matrix = ranking_matrix(arr_A) * ranking_matrix(arr_B) + ranking_matrix(arr_A).T * ranking_matrix(arr_B).T
    result = []
    for i in range(10):
        for j in range(10):
            if result_matrix[i][j] == 0:
                result.append(i+1)

    result = json.dumps(result)
    return result

print(main("task5/range_A.json", "task5/range_B.json"))
