📦 Mini Docker: OS-Level Virtualization with Paging
A simplified simulation of Docker container management and memory paging, built using Flask (Python) and Chart.js. This project allows users to create containers, simulate memory paging (FIFO, LRU, OPTIMAL, CLOCK), and visualize memory frame usage dynamically through an interactive web interface.

🧠 Key Features
Create, delete, and toggle "containers"

Assign memory pages and ports to containers

Apply paging algorithms (FIFO, LRU, OPTIMAL, CLOCK)

Real-time visualizations with Chart.js

Web UI using Flask, HTML, JS, and inline CSS

Designed for educational use (OS & virtualization concepts)


🛠️ Technologies Used
Backend: Python, Flask

Frontend: HTML, JavaScript, Chart.js

Architecture:

container.py – Manages container structure and lifecycle

memory.py – Allocates memory using selected algorithm

paging_simulation.py – Simulates paging logic (FIFO, LRU, etc.)

app.py – Flask routes and API endpoints

dashboard.html – Web UI with embedded form, charts, and AJAX

🚀 How to Run
Clone the repository

bash
Copy
Edit
git clone https://github.com/priyanshi-1303/Mini-docker
cd mini-docker
Install dependencies

bash
Copy
Edit
pip install flask
Run the app

bash
Copy
Edit
python app.py
Open in browser
Visit http://127.0.0.1:5000

📁 Project Structure
cpp
Copy
Edit
mini-docker/
├── app.py
├── container.py
├── memory.py
├── paging_simulation.py
├── container_runtime.py
├── requirements.txt
├── templates/
│   └── dashboard.html
├── static/              (optional if separated)
│   ├── style.css
│   └── script.js
└── README.md
✅ Status
💻 Completed core simulation and UI
📊 Charts and visual stats integrated
📦 Ready for report, viva, or submission
🧪 Advanced features (like unshare, export logs) – pending
