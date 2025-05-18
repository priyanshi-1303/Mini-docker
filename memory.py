# === memory.py ===
from paging_simulation import PagingSimulator

class MemoryManager:
    def __init__(self, total_frames):
        self.total_frames = total_frames
        self.allocated = {}  # container_id -> (frames, faults)

    def allocate(self, container_id, pages, algorithm='FIFO'):
        simulator = PagingSimulator(self.total_frames)
        result = simulator.simulate(pages, algorithm)
        self.allocated[container_id] = result
        return result['frames'], result['page_faults']

    def deallocate(self, container_id):
        if container_id in self.allocated:
            del self.allocated[container_id]

    def get_memory_map(self):
        return {cid: data['frames'] for cid, data in self.allocated.items()}

    def used_frames(self):
        return sum(len(data['frames']) for data in self.allocated.values())

    def available_frames(self):
        return self.total_frames - self.used_frames()