import pandas as pd
import numpy as np


def entropy(probs):
    return -np.sum(probs * np.log2(probs), where=(probs > 0))

def conditional_entropy(joint_probs, conditional_probs):
    valid_probs = (joint_probs > 0) & (conditional_probs > 0)
    return -np.sum(joint_probs[valid_probs] * np.log2(conditional_probs[valid_probs]))

def main():
    data = pd.read_csv('./task4/example.csv', index_col=0)
    total_count = data.values.sum()
    joint_probs = data / total_count  
    prob_A = joint_probs.sum(axis=1)  
    prob_B = joint_probs.sum(axis=0) 
    H_AB = entropy(joint_probs.values.flatten())
    H_A = entropy(prob_A.values)
    H_B = entropy(prob_B.values)
    conditional_probs = joint_probs.div(prob_A, axis=0)
    Ha_B = conditional_entropy(joint_probs.values.flatten(), conditional_probs.values.flatten())
    I_AB = H_A + H_B - H_AB
    result = [float(round(H_AB, 2)), float(round(H_A, 2)), float(round(H_B, 2)), float(round(Ha_B, 2)), float(round(I_AB, 2))]
    return result

print(main())