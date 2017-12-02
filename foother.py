import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import heapq

t_nutrition = pd.read_csv('food_data.csv', header=0, names=['id', 'food_group', 'long_descr', 'short_descr', 'water',
                                                            'energy', 'protein', 'lipid', 'carbohydrate', 'fiber',
                                                            'sugar', 'ca', 'sat_fat', 'cholesterol', 'v_b', 'na'])
# normal numpy array
nut_arr = np.array(t_nutrition.as_matrix())

# difference of only one nutrient
def compare(f_item, f_that, nut = False):
    if(nut == "cpf"):
        diff = (nut_arr[f_item][6:8] - nut_arr[f_that][6:8]) ** 2
        return sum(diff)
    elif(nut):
        return (nut_arr[f_item, nut] - nut_arr[f_that, nut]) ** 2
    else:
        diff = (nut_arr[f_item, 4:] - nut_arr[f_that, 4:]) ** 2
        return sum(diff)

def interpret(f_item_string):
    list_idx = []
    tuple = 0 # NEW
    max = 0 # NEW
    heapq.heapify(list_idx)
    key_words = f_item_string.split(" ")
    for i in range(nut_arr.shape[0]):
        targets = nut_arr[i][2].split(", ")
        for j in range(len(targets)):
            targets[j] = targets[j].lower()
        count = 0
        for j in range(len(key_words)):
            key_words[j] = key_words[j].lower()
            if (key_words[j] in targets):
                count += 1
        if (count):
            if(nut_arr[i][2].split(", ")[0].lower() == key_words[len(key_words) - 1].lower()):
                heapq.heappush(list_idx, (-count, i))

    # NEW
    candidates = []
    if(len(list_idx) == 0):
        return -1
    else:
        tuple = heapq.heappop(list_idx)
        candidates.append(tuple[1])
        max = tuple[0]

    while(tuple[0] == max and len(list_idx) != 0):
        candidates.append(heapq.heappop(list_idx)[1])
    print(candidates)
    return candidates[0]

def similar_entries(n, f_item_string, nut = None):
    f_item = interpret(f_item_string)
    f_item_plural = interpret(f_item_string + "s")
    f_item_plural_plus = interpret(f_item_string + "es")

    # not found go to error:
    if(f_item + f_item_plural + f_item_plural_plus == -3):
        return "match not found for " + f_item_string

    if(f_item != -1):
        print(nut_arr[f_item][2])
    if(f_item_plural != -1):
        print(nut_arr[f_item_plural][2])
    if (f_item_plural_plus != -1):
        print(nut_arr[f_item_plural_plus][2])
    best_matches_idx = []
    heapq.heapify(best_matches_idx)
    for i in range(nut_arr.shape[0]):
        if(i == f_item or i == f_item_plural or i == f_item_plural_plus):
            continue
        if (len(best_matches_idx) == n):
            if(f_item != -1):
                heapq.heappushpop(best_matches_idx, (-compare(f_item, i, nut), i))
            if (f_item_plural != -1):
                heapq.heappushpop(best_matches_idx, (-compare(f_item_plural, i, nut), i))
            if (f_item_plural_plus != -1):
                heapq.heappushpop(best_matches_idx, (-compare(f_item_plural_plus, i, nut), i))
        else:
            if (f_item != -1):
                heapq.heappush(best_matches_idx, (-compare(f_item, i, nut), i))
            if (f_item_plural != -1):
                heapq.heappush(best_matches_idx, (-compare(f_item_plural, i, nut), i))
            if (f_item_plural_plus != -1):
                heapq.heappush(best_matches_idx, (-compare(f_item_plural_plus, i, nut), i))
    best_matches = []
    for i in range(len(best_matches_idx)):
        best_matches.append(nut_arr[best_matches_idx[i][1]][2])
    return best_matches

print(similar_entries(5, "apple"))