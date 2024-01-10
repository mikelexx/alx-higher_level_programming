#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    best = ""
    for key in a_dictionary:
        best = key
        break
    for key in a_dictionary:
        if a_dictionary[key] >= a_dictionary[best]:
            best = key
    return best
