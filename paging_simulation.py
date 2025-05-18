class PagingSimulator:
    def __init__(self, capacity):
        self.capacity = capacity

    def simulate(self, pages, algorithm='FIFO'):
        algorithm = algorithm.upper()
        if algorithm == 'FIFO':
            return self.simulate_fifo(pages)
        elif algorithm == 'LRU':
            return self.simulate_lru(pages)
        elif algorithm == 'OPTIMAL':
            return self.simulate_optimal(pages)
        elif algorithm == 'CLOCK':
            return self.simulate_clock(pages)
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

    def simulate_fifo(self, pages):
        memory, history, faults = [], [], 0
        for page in pages:
            if page not in memory:
                faults += 1
                if len(memory) >= self.capacity:
                    memory.pop(0)
                memory.append(page)
            history.append(list(memory))
        return {"algorithm": "FIFO", "frames": memory, "history": history, "page_faults": faults}

    def simulate_lru(self, pages):
        memory, history, faults, recent = [], [], 0, []
        for page in pages:
            if page not in memory:
                faults += 1
                if len(memory) >= self.capacity:
                    lru = recent.pop(0)
                    memory.remove(lru)
                memory.append(page)
            else:
                recent.remove(page)
            recent.append(page)
            history.append(list(memory))
        return {"algorithm": "LRU", "frames": memory, "history": history, "page_faults": faults}

    def simulate_optimal(self, pages):
        memory, history, faults = [], [], 0
        for i in range(len(pages)):
            page = pages[i]
            if page not in memory:
                faults += 1
                if len(memory) < self.capacity:
                    memory.append(page)
                else:
                    future = pages[i+1:]
                    indexes = [(future.index(m) if m in future else float('inf')) for m in memory]
                    to_replace = indexes.index(max(indexes))
                    memory[to_replace] = page
            history.append(list(memory))
        return {"algorithm": "Optimal", "frames": memory, "history": history, "page_faults": faults}

    def simulate_clock(self, pages):
        memory, history, faults, pointer = [], [], 0, 0
        ref_bits, page_table = [], {}
        for page in pages:
            if page not in page_table:
                faults += 1
                if len(memory) < self.capacity:
                    memory.append(page)
                    ref_bits.append(1)
                    page_table[page] = len(memory) - 1
                else:
                    while True:
                        if ref_bits[pointer] == 0:
                            old = memory[pointer]
                            del page_table[old]
                            memory[pointer] = page
                            ref_bits[pointer] = 1
                            page_table[page] = pointer
                            pointer = (pointer + 1) % self.capacity
                            break
                        else:
                            ref_bits[pointer] = 0
                            pointer = (pointer + 1) % self.capacity
            else:
                ref_bits[page_table[page]] = 1
            history.append(list(memory))
        return {"algorithm": "Clock", "frames": memory, "history": history, "page_faults": faults}
