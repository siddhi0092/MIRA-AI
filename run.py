"""
run.py  –  MIRA local development launcher
───────────────────────────────────────────
Run from the project root (MIRA/) with:

    python run.py

This script adds the project root to sys.path and starts uvicorn,
ensuring `from backend.xxx import ...` always resolves correctly
regardless of which directory your terminal is in.
"""

import sys
import os

# Make sure the MIRA/ root is on the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["backend"],  # only watch the backend folder
    )
