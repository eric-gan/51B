import networkx as nx
import os
import numpy as np
import copy
import multiprocessing
from output_scorer import score_output

paths_outputs = ["./goat", "./goatvm"] #, "./outputs_test", "./outputs"]
path_to_inputs = "./all_inputs"
#path_to_outputs = "./outputs_test"
#path_to_outputs2 = "./outputs"
size_categories = ['medium'] #["small", "medium"]

def score_all_outputs(output_folder, silent=True):
    all_scores = {}
    for size in size_categories:
        category_scores = {}
        category_path = path_to_inputs + "/" + size
        output_category_path = output_folder + "/" + size
        
        loaded_cached = False
        '''
        cached_filename = output_folder + "/" + size + "_cached_scores.json"
        try:
            print("Looking for cached file: {}".format(cached_filename))
            with open(cached_filename, "r") as cached_file:
                print("Loading from cached evaluation scores for " + size + "...")
                category_scores = json.load(cached_file)
                print("Read {} successfully.".format(cached_filename))
                loaded_cached = True
        except FileNotFoundError as e:
            pass
        '''
        
        if not loaded_cached:
        
            category_dir = os.fsencode(category_path)
            
            if not os.path.isdir(output_category_path):
                os.mkdir(output_category_path)

            for input_folder in os.listdir(category_dir):
                input_name = os.fsdecode(input_folder) 
                #print(input_name)
                score, msg = score_output(category_path + "/" + input_name, output_category_path + "/" + input_name + ".out")
                #if not silent:
                    #print("{}-{} scored {}".format(size, input_name, score))
                category_scores[input_name] = max(score, 0)
            '''
            with open(cached_filename, "w") as cached_file:
                json.dump(category_scores, cached_file)
            '''
        all_scores[size] = category_scores
    return all_scores

def compute_better(all_scores):
    ret = []
    for size in size_categories:
        ret_curr = []
        #category_scores = all_scores[size]
        #category_scores2 = all_scores2[size]
        for instance in all_scores[0][size].keys():
            all_instance = [all_scores[p][size][instance] for p in range(len(all_scores))]
            best = np.argmax(all_instance)
            print(paths_outputs[best], ' did best')
            ret_curr.append(paths_outputs[best] + '/' + size + '/' + instance + '.out')
            #if category_scores[instance] >= category_scores2[instance]:
            #    print('first better')
            #    ret_curr.append(path_to_outputs + '/' + size + '/' + instance + '.out')
            #else:
            #    print('second better')
            #    ret_curr.append(path_to_outputs2 + '/' + size + '/'  + instance + '.out')
        ret.append(ret_curr)
    return ret

all_scores = [score_all_outputs(path, silent=True) for path in paths_outputs]
#all_1 = score_all_outputs(path_to_outputs, silent=True)
#all_2 = score_all_outputs(path_to_outputs2, silent=True)
#best = compute_better(all_1, all_2)
best = compute_better(all_scores)
with open('betters2.txt', 'w') as f:
    for size in best:
        for item in size:
            f.write("%s " % item)