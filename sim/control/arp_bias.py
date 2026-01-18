"""
ARP Bias Controller

Controls session preemption priority under congestion.
Higher bias => higher chance to survive.
"""

class ARPBiasController:
    def __init__(self, slice_ids):
        self.slice_ids = slice_ids
        self.bias = {s: 0.0 for s in slice_ids}

    def apply(self, action):
        """
        action: real-valued bias per slice
        returns: slice -> ARP bias
        """
        for i, s in enumerate(self.slice_ids):
            self.bias[s] = float(action[i])

        return self.bias
