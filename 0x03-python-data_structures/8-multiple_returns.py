#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_2 = (0, None)
    else:
        tuple_2 = (len(sentence), sentence[0])
    return (tuple_2)
