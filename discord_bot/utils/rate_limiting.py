```python
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests, period):
        self.max_requests = max_requests
        self.period = period
        self.requests = defaultdict(list)

    def is_limited(self, identifier):
        current_time = time.time()
        if identifier in self.requests:
            self.requests[identifier] = [req for req in self.requests[identifier] if req > current_time - self.period]
            if len(self.requests[identifier]) >= self.max_requests:
                return True
        self.requests[identifier].append(current_time)
        return False
```
