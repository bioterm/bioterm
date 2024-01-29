from queue import Queue

from ...common.models.control.base_models import Datapoint


class DatapointQueue(Queue):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def put(self, item: Datapoint, block=True, timeout=None):
        super().put(item, block, timeout)
