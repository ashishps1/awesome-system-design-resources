import time

class FixedWindowCounter:
    def __init__(self, window_size, max_requests):
        self.window_size = window_size  # Size of the window in seconds
        self.max_requests = max_requests  # Maximum number of requests per window
        self.current_window = time.time() // window_size
        self.request_count = 0

    def allow_request(self):
        current_time = time.time()
        window = current_time // self.window_size

        # If we've moved to a new window, reset the counter
        if window != self.current_window:
            self.current_window = window
            self.request_count = 0

        # Check if we're still within the limit for this window
        if self.request_count < self.max_requests:
            self.request_count += 1
            return True
        return False

# Usage example
limiter = FixedWindowCounter(window_size=60, max_requests=5)  # 5 requests per minute

for _ in range(10):
    print(limiter.allow_request())  # Will print True for the first 5 requests, then False
    time.sleep(0.1)  # Wait a bit between requests

time.sleep(60)  # Wait for the window to reset
print(limiter.allow_request())  # True