import sys
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

import uvicorn
import os

print("run.py STARTED")
print("Starting AI Assistant Backend on http://127.0.0.1:8000")

# Add project root so 'backend' can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    uvicorn.run(
        "backend.app:app",
        host="127.0.0.1",
        port=8000
    )
