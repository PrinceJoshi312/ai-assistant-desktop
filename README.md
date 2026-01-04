# AI Virtual Assistant (Desktop Version)

An intelligent, cross-platform desktop assistant built by integrating a **Python-based AI engine** with an **Electron.js GUI**. This project evolved from a terminal-based bot into a full-fledged desktop application.

## 🚀 Current Project Status: Phase 1 Complete
- [x] Backend FastAPI server operational.
- [x] Electron frontend successfully communicating with Python.
- [x] Real-time intent processing (JSON handshake).
- [ ] OS Action Mapping (Opening apps, browser control).
- [ ] UI/UX Polishing.

## 🛠 Tech Stack
- **Frontend:** Electron.js, HTML5, CSS3, JavaScript.
- **Backend:** Python, FastAPI, Uvicorn.
- **AI/ML:** TensorFlow/Keras (Intent Recognition), NLTK (NLP).
- **Communication:** IPC Bridge & REST API.

## 📂 Project Structure
- `/electron`: Contains the desktop window logic, preload scripts, and UI files.
- `/backend`: The core AI engine, intent models, and FastAPI routes.
- `run.py`: The main entry point to launch both the backend and frontend simultaneously.

## ⚙️ How to Run (Development)
1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   npm install
