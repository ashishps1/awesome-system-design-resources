package implementations.java.rate_limiting;

import java.time.Instant;
import java.util.LinkedList;
import java.util.Queue;

public class LeakyBucket {
    private final long capacity;        // Maximum number of requests the bucket can hold
    private final double leakRate;      // Rate at which requests leak out of the bucket (requests per second)
    private final Queue<Instant> bucket; // Queue to hold timestamps of requests
    private Instant lastLeakTimestamp;   // Last time we leaked from the bucket

    public LeakyBucket(long capacity, double leakRate) {
        this.capacity = capacity;
        this.leakRate = leakRate;
        this.bucket = new LinkedList<>();
        this.lastLeakTimestamp = Instant.now();
    }

    public synchronized boolean allowRequest() {
        leak();  // First, leak out any requests based on elapsed time

        if (bucket.size() < capacity) {
            bucket.offer(Instant.now());  // Add the new request to the bucket
            return true;  // Allow the request
        }
        return false;  // Bucket is full, deny the request
    }

    private void leak() {
        Instant now = Instant.now();
        long elapsedMillis = now.toEpochMilli() - lastLeakTimestamp.toEpochMilli();
        int leakedItems = (int) (elapsedMillis * leakRate / 1000.0);  // Calculate how many items should have leaked

        // Remove the leaked items from the bucket
        for (int i = 0; i < leakedItems && !bucket.isEmpty(); i++) {
            bucket.poll();
        }

        lastLeakTimestamp = now;
    }
}
