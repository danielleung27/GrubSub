import pandas as pd
import numpy as np
import heapq
import sys
import re
import numpy as np

class FoodSearch:
    def __init__(self):
        t_nutrition = pd.read_csv('polls/food_data.csv', header=0,
                                  names=['id', 'food_group', 'long_descr', 'short_descr', 'water',
                                         'energy', 'protein', 'lipid', 'carbohydrate', 'fiber',
                                         'sugar', 'ca', 'sat_fat', 'cholesterol', 'v_b', 'na'])
        self.nut_arr = np.array(t_nutrition.as_matrix())

    def compare(self, f_item, f_that, nut = False):
        weights = np.random.rand(12)
        weights = weights/sum(weights)
        if(nut == "cpf"):
            diff = (self.nut_arr[f_item][6:8] - self.nut_arr[f_that][6:8]) ** 2
            return sum(diff)
        elif(nut):
            return (self.nut_arr[f_item, nut] - self.nut_arr[f_that, nut]) ** 2
        else:
            diff = (self.nut_arr[f_item, 4:] - self.nut_arr[f_that, 4:]) ** 2
            return np.dot(weights, diff)

    def interpret(self, f_item_string):
        list_idx = []
        no_match_max = 0;
        no_match_shortest = sys.maxsize;
        no_match_idx = -1;
        tuple = 0
        max = 0
        heapq.heapify(list_idx)
        key_words = re.split("\W+", f_item_string)
        for i in range(self.nut_arr.shape[0]):
            targets = re.split("\W+", self.nut_arr[i][2])
            for j in range(len(targets)):
                targets[j] = targets[j].lower()
            count = 0
            for j in range(len(key_words)):
                key_words[j] = key_words[j].lower()
                if (key_words[j] in targets):
                    count += 1
            if (count):
                if(self.nut_arr[i][2].split(", ")[0].lower() == key_words[len(key_words) - 1].lower()):
                    heapq.heappush(list_idx, (-count, i))
            if (count != 0 and count == no_match_max and len(targets) < no_match_shortest or count > no_match_max):
                no_match_idx = i
                no_match_max = count
                no_match_shortest = len(targets)
        candidates = []
        if(len(list_idx) == 0):
            if(no_match_idx != -1):
                print(self.nut_arr[no_match_idx][2])
            return no_match_idx, False
        else:
            tuple = heapq.heappop(list_idx)
            candidates.append(tuple[1])
            max = tuple[0]

        while(tuple[0] == max and len(list_idx) != 0):
            candidates.append(heapq.heappop(list_idx)[1])
        print(candidates)
        print(self.nut_arr[candidates[0]][2])
        return candidates[0], True

    def similar_entries(self, n, f_item_string, nut = None):
        f_item, f_item_match = self.interpret(f_item_string)
        f_item_plural, f_item_plural_match = self.interpret(f_item_string + "s")
        f_item_plural_plus, f_item_plural_plus_match = self.interpret(f_item_string + "es")

        if(f_item_match or f_item_plural_match or f_item_plural_plus_match):
            if(not f_item_match):
                f_item = -1
            if(not f_item_plural_match):
                f_item_plural = -1
            if(not f_item_plural_plus_match):
                f_item_plural_plus = -1

        # not found go to error:
        if(f_item + f_item_plural + f_item_plural_plus == -3):
            return []

        best_matches_idx = []
        heapq.heapify(best_matches_idx)
        for i in range(self.nut_arr.shape[0]):
            if(i == f_item or i == f_item_plural or i == f_item_plural_plus):
                continue
            if (len(best_matches_idx) == n):
                if(f_item != -1):
                    heapq.heappushpop(best_matches_idx, (-self.compare(f_item, i, nut), i))
                if (f_item_plural != -1):
                    heapq.heappushpop(best_matches_idx, (-self.compare(f_item_plural, i, nut), i))
                if (f_item_plural_plus != -1):
                    heapq.heappushpop(best_matches_idx, (-self.compare(f_item_plural_plus, i, nut), i))
            else:
                if (f_item != -1):
                    heapq.heappush(best_matches_idx, (-self.compare(f_item, i, nut), i))
                if (f_item_plural != -1):
                    heapq.heappush(best_matches_idx, (-self.compare(f_item_plural, i, nut), i))
                if (f_item_plural_plus != -1):
                    heapq.heappush(best_matches_idx, (-self.compare(f_item_plural_plus, i, nut), i))
                while (len(best_matches_idx) > n):
                    heapq.heappop(best_matches_idx)
        best_matches = []
        for i in range(len(best_matches_idx)):
            best_matches.append(self.nut_arr[best_matches_idx[i][1]][2])
        return best_matches
