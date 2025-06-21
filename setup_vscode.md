# Setting Up Telegram Monitor in Visual Studio Code

## Prerequisites
1. Install Python 3.7 or higher
2. Install Visual Studio Code
3. Install Python extension for VS Code

## Setup Instructions

### 1. Create Project Folder
```bash
mkdir telegram-monitor
cd telegram-monitor
```

### 2. Copy Files
Copy these files to your project folder:
- `main.py`
- `config.py` 
- `telegram_monitor.py`
- `rate_limiter.py`
- `config.ini`
- `requirements.txt`

### 3. Setup Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Your Credentials
Edit `config.ini` and add your Telegram credentials:
```ini
[api]
api_id = YOUR_API_ID
api_hash = YOUR_API_HASH
phone_number = YOUR_PHONE_NUMBER
session_name = telegram_monitor_session

[monitor]
comment_messages = hey this is me
comment_delay_min = 1
comment_delay_max = 3
max_comments_per_hour = 10
target_channel = Sport_433et
```

### 6. VS Code Configuration
Create `.vscode/launch.json` for debugging:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Telegram Monitor",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}
```

### 7. Running the Monitor

#### Option A: Run in Terminal
1. Open VS Code terminal (Ctrl+`)
2. Make sure virtual environment is activated
3. Run: `python main.py`

#### Option B: Use VS Code Debugger
1. Open `main.py`
2. Press F5 or go to Run > Start Debugging
3. Select "Python: Telegram Monitor"

## Project Structure
```
telegram-monitor/
├── main.py                 # Entry point
├── config.py              # Configuration management
├── telegram_monitor.py    # Core monitoring logic
├── rate_limiter.py        # Rate limiting
├── config.ini            # Configuration file
├── requirements.txt       # Dependencies
├── .vscode/
│   └── launch.json       # VS Code debug config
└── venv/                 # Virtual environment (if used)
```

## Troubleshooting

### Common Issues:
1. **Module not found**: Make sure virtual environment is activated and dependencies installed
2. **Permission errors**: Ensure you have proper Telegram API credentials
3. **Connection issues**: Check internet connection and Telegram API status

### Getting Telegram API Credentials:
1. Go to https://my.telegram.org
2. Log in with your phone number
3. Go to "API Development Tools"
4. Create a new application
5. Copy `api_id` and `api_hash`

## Features
- Real-time channel monitoring
- Automatic commenting on new posts
- Rate limiting (10 comments/hour)
- Session persistence
- Error handling and logging
- 1-3 second comment delay