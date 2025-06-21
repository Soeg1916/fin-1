#!/usr/bin/env python3
"""
Telegram Channel Monitor and Auto-Commenter
A script for monitoring Telegram channels and automatically commenting on new posts
while respecting Telegram's Terms of Service and rate limits.
"""

import asyncio
import logging
import os
import sys
from telegram_monitor import TelegramMonitor
from config import Config

def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('telegram_monitor.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )

async def main():
    """Main entry point for the application"""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Load configuration
        config = Config()
        
        # Validate required configuration
        if not config.validate():
            logger.error("Configuration validation failed. Please check your settings.")
            return
        
        # Create and start the monitor
        monitor = TelegramMonitor(config)
        
        logger.info("Starting Telegram Channel Monitor...")
        logger.info("Press Ctrl+C to stop the monitor")
        
        # Start monitoring
        await monitor.start()
        
    except KeyboardInterrupt:
        logger.info("Monitor stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise
    finally:
        logger.info("Telegram Monitor shutdown complete")

if __name__ == "__main__":
    # Check Python version
    if sys.version_info < (3, 7):
        print("Python 3.7 or higher is required")
        sys.exit(1)
    
    # Run the async main function
    asyncio.run(main())
