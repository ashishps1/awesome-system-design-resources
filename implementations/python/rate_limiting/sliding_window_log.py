import time
from collections import deque

class SlidingWindowLog:
    def __init__(self, window_size, max_requests):
        self.window_size = window_size  # Size of the sliding window in seconds
        self.max_requests = max_requests  # Maximum number of requests per window
        self.request_log = deque()  # Log to keep track of request timestamps

    def allow_request(self):
        now = time.time()
        
        # Remove timestamps that are outside the current window
        while self.request_log and now - self.request_log[0] >= self.window_size:
            self.request_log.popleft()

        # Check if we're still within the limit
        if len(self.request_log) < self.max_requests:
            self.request_log.append(now)
            return True
        return False

# Usage example
limiter = SlidingWindowLog(window_size=60, max_requests=5)  # 5 requests per minute

for _ in range(10):
    print(limiter.allow_request())  # Will print True for the first 5 requests, then False
    time.sleep(0.1)  # Wait a bit between requests

time.sleep(60)  # Wait for the window to slide
print(limiter.allow_request())  # True