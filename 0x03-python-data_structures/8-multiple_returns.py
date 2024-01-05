#!/usr/bin/python3
def multiple_returns(sentence):
    a = None
    if len(sentence) != 0:
        a = sentence[0]
    return (len(sentence), a,)
