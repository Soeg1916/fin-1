"""
Rate Limiter for Telegram API compliance
Ensures we stay within Telegram's rate limits and TOS
"""

import time
import logging
from collections import deque
from typing import Deque

class RateLimiter:
    """Simple rate limiter to prevent API abuse"""
    
    def __init__(self, max_actions: int, time_window: int):
        """
        Initialize rate limiter
        
        Args:
            max_actions: Maximum number of actions allowed in the time window
            time_window: Time window in seconds
        """
        self.max_actions = max_actions
        self.time_window = time_window
        self.action_times: Deque[float] = deque()
        self.logger = logging.getLogger(__name__)
        
        self.logger.info(f"Rate limiter initialized: {max_actions} actions per {time_window} seconds")
    
    def can_perform_action(self) -> bool:
        """
        Check if an action can be performed without exceeding rate limits
        
        Returns:
            True if action is allowed, False otherwise
        """
        current_time = time.time()
        
        # Remove actions outside the time window
        while self.action_times and current_time - self.action_times[0] > self.time_window:
            self.action_times.popleft()
        
        # Check if we're under the limit
        can_act = len(self.action_times) < self.max_actions
        
        if not can_act:
            oldest_action = self.action_times[0]
            wait_time = self.time_window - (current_time - oldest_action)
            self.logger.warning(f"Rate limit reached. Need to wait {wait_time:.1f} seconds")
        
        return can_act
    
    def record_action(self):
        """Record that an action has been performed"""
        current_time = time.time()
        self.action_times.append(current_time)
        
        remaining_actions = self.max_actions - len(self.action_times)
        self.logger.info(f"Action recorded. {remaining_actions} actions remaining in current window")
    
    def get_stats(self) -> dict:
        """Get current rate limiter statistics"""
        current_time = time.time()
        
        # Clean old actions
        while self.action_times and current_time - self.action_times[0] > self.time_window:
            self.action_times.popleft()
        
        return {
            'actions_used': len(self.action_times),
            'actions_remaining': self.max_actions - len(self.action_times),
            'time_window': self.time_window,
            'next_reset': self.action_times[0] + self.time_window if self.action_times else current_time
        }
    
    def wait_time_until_next_action(self) -> float:
        """Calculate how long to wait until the next action is allowed"""
        if self.can_perform_action():
            return 0.0
        
        current_time = time.time()
        oldest_action = self.action_times[0]
        return max(0.0, self.time_window - (current_time - oldest_action))
