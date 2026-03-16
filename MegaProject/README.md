# 30-Day DevOps Challenge: The Grand Finale 🚀

This project is the culmination of 30 days of intensive DevOps learning. It features a self-healing, resource-optimized, multi-tier architecture.

## ✨ Features
- **Self-Healing:** Docker Healthchecks ensure 99.9% uptime for the web tier.
- **Security:** Custom bridge networking to isolate the database.
- **Efficiency:** Strict resource limits (50MB RAM cap) for the frontend.
- **Persistence:** Named volumes to ensure data survives container restarts.

## 🛠️ How to Run
```bash
docker-compose up -d
