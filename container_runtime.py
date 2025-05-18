# container_runtime.py
import os
import subprocess

def create_container(name):
    container_dir = f"containers/{name}"
    try:
        os.makedirs(container_dir, exist_ok=True)
        with open(os.path.join(container_dir, "info.txt"), "w") as f:
            f.write(f"Container: {name}\n")

        result = subprocess.run([
            "unshare", "--mount", "--uts", "--ipc", "--net", "--pid", "--fork", "--mount-proc", "--", "bash", "-c", "echo Container started && sleep 1"
        ], cwd=container_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            raise RuntimeError(f"Unshare failed: {result.stderr.decode().strip()}")
        return True
    except Exception as e:
        print(f"[ERROR] Container creation failed: {e}")
        return False
