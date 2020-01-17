import numpy as np
from flask import jsonify

def nparray_to_json(arr):
    return jsonify(arr)


# ------------------------------------- user function
def testdata():
    res = np.array(10)
    return nparray_to_json(res)