#!/usr/bin/env python3
"""
Alternative entry point for VS Code with better error handling
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main import main
    import asyncio
    
    if __name__ == "__main__":
        print("Starting Telegram Monitor for VS Code...")
        asyncio.run(main())
        
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure to install dependencies: pip install telethon")
except Exception as e:
    print(f"Error: {e}")
    input("Press Enter to exit...")