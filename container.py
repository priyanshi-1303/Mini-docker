# === container.py ===
import uuid

class Container:
    def __init__(self, name, memory_pages, ports=None, algorithm='FIFO'):
        self.id = str(uuid.uuid4())
        self.name = name
        self.memory_pages = memory_pages
        self.ports = ports or []
        self.algorithm = algorithm.upper()
        self.is_running = True

    def stop(self):
        self.is_running = False

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "memory_pages": self.memory_pages,
            "ports": self.ports,
            "algorithm": self.algorithm,
            "is_running": self.is_running
        }
