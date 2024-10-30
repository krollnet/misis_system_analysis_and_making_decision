import json
import numpy as np

def ranking_matrix(arr_):
    arr = np.zeros((10, 10))
    for i in arr_:
        for j in range(1, 11):
            if type(i) is list:
                for x in i:
                    for y in i:
                        arr[int(x)-1,int(y)-1] = 1
                    if int(x) >= j:
                        arr[j-1,int(x)-1] = 1

            else:
                temp = int(i)
                if temp>=j:
                    arr[j-1,temp-1] = 1
    return arr

def main(file1, file2):
    with open(file1) as file_A:
        ranking_A = json.load(file_A)
    with open(file2) as file_B:
        ranking_B = json.load(file_B)

    arr_A = list(ranking_A["rank"].values())
    arr_B = list(ranking_B["rank"].values())
    result_matrix = ranking_matrix(arr_A) * ranking_matrix(arr_B)
    max_sum_cols = np.where(result_matrix.sum(axis=0) == result_matrix.sum(axis=0).max())[0] + 1
    result = json.dumps(max_sum_cols.tolist())
    return result

print(main("task5/range_A.json", "task5/range_B.json"))
