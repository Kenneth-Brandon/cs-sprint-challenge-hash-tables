"""
    desired output: tuple in form (zero, one)
    linear time
    example from README:
    input: weights [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ] # since these are the indices of weights 15 and 6 whose sum equals 21
"""


def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    if length < 2:
        return None
    wt_tbl = {}
    for i in range(len(weights)):
        if weights[i] in wt_tbl:
            wt_tbl[weights[i]].append(i)
        else:
            wt_tbl[weights[i]] = [i]

    for wt in weights:
        if (limit - wt) in wt_tbl:
            print(f"Found: {wt}, {limit-wt}")
            for i in wt_tbl[wt]:
                for j in wt_tbl[limit-wt]:
                    if i != j:
                        return (max(i, j), min(i, j))
    return None
