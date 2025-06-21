#!/usr/bin/env python3
"""
Generate session string for cloud deployment
Run this locally to get your session string
"""

import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

async def generate_session_string():
    print("Session String Generator for Cloud Deployment")
    print("=" * 50)

    # Get credentials
    api_id = input("Enter your API ID: ").strip()
    api_hash = input("Enter your API Hash: ").strip() 
    phone = input("Enter your phone number: ").strip()

    try:
        api_id = int(api_id)
    except:
        print("Invalid API ID")
        return

    client = TelegramClient(StringSession(), api_id, api_hash)

    try:
        await client.start(phone=phone)
        session_string = client.session.save()

        print("\n" + "="*60)
        print("SESSION STRING GENERATED!")
        print("="*60)
        print(session_string)
        print("="*60)
        print("\nCopy this string and use as TELEGRAM_SESSION environment variable")
        print("This replaces the need for session files on cloud platforms")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(generate_session_string())