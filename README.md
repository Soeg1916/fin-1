# Telegram Channel Monitor & Auto-Commenter

A Python script using Telethon for automated Telegram channel monitoring and commenting while maintaining compliance with Telegram's Terms of Service.

## Features

- 🔐 **Secure Authentication**: Uses your official Telegram API credentials
- 📱 **Session Persistence**: Saves login session for automatic reconnection
- 🎯 **Real-time Monitoring**: Detects new posts instantly using Telegram's event system
- 💬 **Smart Commenting**: Automatically replies to new posts with customizable messages
- ⚡ **Rate Limiting**: Built-in rate limiting to respect Telegram's API limits
- 🛡️ **TOS Compliance**: Designed to operate within Telegram's Terms of Service
- 📝 **Comprehensive Logging**: Detailed logs for monitoring and debugging
- ⚙️ **Easy Configuration**: Simple configuration via file or environment variables

## Requirements

- Python 3.7 or higher
- Telethon library (installed automatically)
- Telegram API credentials (api_id and api_hash)

## Setup

### 1. Get Telegram API Credentials

1. Visit [https://my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Go to "API Development Tools"
4. Create a new application
5. Note down your `api_id` and `api_hash`

### 2. Install Dependencies

The script will prompt you to install required dependencies if they're not available.

### 3. Configuration

You can configure the script in three ways:

#### Option A: Interactive Configuration (Recommended)
Run the script and it will guide you through the setup:
```bash
python main.py
