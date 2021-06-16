import numpy as np

def calculate(list):
    if len(list)!=9:
      raise ValueError("List must contain nine numbers.")
    arr=np.reshape(list,(3,3))
    calculations={
     "mean": [arr.mean(0).tolist(),arr.mean(1).tolist(),arr.mean()],
     "variance":[arr.var(0).tolist(),arr.var(1).tolist(),arr.var()],
     "standard deviation":[arr.std(0).tolist(),arr.std(1).tolist(),arr.std()],
     "max": [arr.max(0).tolist(),arr.max(1).tolist(),arr.max()],
     "min": [arr.min(0).tolist(),arr.min(1).tolist(),arr.min()],
     "sum": [arr.sum(0).tolist(),arr.sum(1).tolist(),arr.sum()]
    }
    return calculations