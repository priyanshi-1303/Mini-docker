from flask import Flask, request, jsonify, render_template
from container import Container
from memory import MemoryManager
from paging_simulation import PagingSimulator

app = Flask(__name__)

# Global in-memory data
containers = []
memory_manager = MemoryManager(total_frames=10)
SUPPORTED_ALGORITHMS = ['FIFO', 'LRU', 'OPTIMAL', 'CLOCK']

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/containers", methods=["GET"])
def list_containers():
    return jsonify({
        "containers": [c.to_dict() for c in containers],
        "memory_map": memory_manager.get_memory_map(),
        "stats": {
            "total_frames": memory_manager.total_frames,
            "used_frames": memory_manager.used_frames(),
            "available_frames": memory_manager.available_frames()
        }
    })

@app.route("/containers", methods=["POST"])
def create_container():
    try:
        data = request.get_json()
        name = data['name']
        memory_pages = int(data['memory_pages'])
        ports = [int(p.strip()) for p in data.get('ports', '').split(',') if p.strip()]
        algorithm = data.get('algorithm', 'FIFO').upper()

        if algorithm not in SUPPORTED_ALGORITHMS:
            return jsonify({"error": "Unsupported algorithm"}), 400

        container = Container(name, memory_pages, ports, algorithm)
        containers.append(container)

        pages = list(range(1, memory_pages + 1))
        frames, faults = memory_manager.allocate(container.id, pages, algorithm)

        return jsonify({
            "message": "Container created",
            "container": container.to_dict(),
            "frames": frames,
            "page_faults": faults
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/containers/<container_id>/delete", methods=["DELETE"])
def delete_container(container_id):
    global containers
    containers = [c for c in containers if c.id != container_id]
    memory_manager.deallocate(container_id)
    return jsonify({"message": "Container deleted", "memory_map": memory_manager.get_memory_map()})

@app.route("/containers/<container_id>/toggle", methods=["POST"])
def toggle_container(container_id):
    for container in containers:
        if container.id == container_id:
            container.is_running = not container.is_running
            return jsonify({"status": "toggled", "is_running": container.is_running})
    return jsonify({"error": "Container not found"}), 404

@app.route("/simulate", methods=["POST"])
def simulate_algorithm():
    try:
        data = request.get_json()
        pages = [int(p.strip()) for p in data['pages'].split(',')]
        capacity = int(data['capacity'])
        algorithm = data.get('algorithm', 'FIFO').upper()

        if algorithm not in SUPPORTED_ALGORITHMS:
            return jsonify({"error": "Unsupported algorithm"}), 400

        simulator = PagingSimulator(capacity)
        result = simulator.simulate(pages, algorithm)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
