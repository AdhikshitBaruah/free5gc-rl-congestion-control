"""
Slice Resource Share Controller

Controls per-slice resource allocation weights.
Sum of all slice weights = 1
"""

import numpy as np

class SliceWeightController:
    def __init__(self, slice_ids):
        self.slice_ids = slice_ids
        self.weights = np.ones(len(slice_ids)) / len(slice_ids)

    def apply(self, action):
        """
        action: unbounded real vector (RL output)
        returns: normalized slice weights
        """
        action = np.array(action)
        exp_w = np.exp(action)
        self.weights = exp_w / np.sum(exp_w)

        return {
            slice_id: float(w)
            for slice_id, w in zip(self.slice_ids, self.weights)
        }
