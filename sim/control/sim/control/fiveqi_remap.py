"""
5QI Re-Mapping Controller

Dynamically maps service classes to 5QI levels
during congestion events.
"""

class FiveQIRemapController:
    def __init__(self, service_classes, valid_5qi):
        self.service_classes = service_classes
        self.valid_5qi = valid_5qi

    def apply(self, action):
        """
        action: list of indices into valid_5qi
        returns: service -> 5QI mapping
        """
        mapping = {}
        for i, service in enumerate(self.service_classes):
            q_idx = int(action[i])
            q_idx = max(0, min(q_idx, len(self.valid_5qi) - 1))
            mapping[service] = self.valid_5qi[q_idx]

        return mapping
