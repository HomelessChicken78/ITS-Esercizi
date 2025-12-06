from enum import Enum

class StatoRiparazione(Enum):
    received = "received"
    diagnosing = "diagnosing"
    repairing = "repairing"
    ready = "ready"
    delivered = "delivered"
