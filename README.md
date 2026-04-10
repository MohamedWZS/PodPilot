# PodPilot 🚀

PodPilot is a minimal FastAPI-based job management API designed to explore DevOps workflows, containerization, Kubernetes (k3s), and CI/CD pipelines.

## 🧰 Tech Stack

- Python + FastAPI
- PostgreSQL
- Docker
- Kubernetes (k3s)
- GitHub Actions (CI/CD)

## ⚙️ Features

- Create jobs
- List jobs
- Simple job status tracking

## 📁 Project Structure

app/
├── main.py
├── models.py
├── schemas.py
├── database.py
└── routes/
    └── jobs.py

## ▶️ Run Locally

```bash
uv sync
uv run uvicorn app.main:app --reload


---

## 🟢 6. API Endpoints

```markdown
## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| POST   | /jobs   | Create a job |
| GET    | /jobs   | List all jobs |

## 🚀 Future Improvements

- Dockerize the application
- Deploy on Kubernetes (k3s)
- Add CI/CD pipeline using GitHub Actions
- Add Ingress and domain routing
- Add monitoring (Prometheus + Grafana)