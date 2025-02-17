import hashlib
import bisect

class ConsistentHashing:
    def __init__(self, servers, num_replicas=3):
        """
        Initializes the consistent hashing ring.

        - servers: List of initial server names (e.g., ["S0", "S1", "S2"])
        - num_replicas: Number of virtual nodes per server for better load balancing
        """
        self.num_replicas = num_replicas  # Number of virtual nodes per server
        self.ring = {}  # Hash ring storing virtual node mappings
        self.sorted_keys = []  # Sorted list of hash values (positions) on the ring
        self.servers = set()  # Set of physical servers (used for tracking)

        # Add each server to the hash ring
        for server in servers:
            self.add_server(server)

    def _hash(self, key):
        """Computes a hash value for a given key using MD5."""
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_server(self, server):
        """
        Adds a server to the hash ring along with its virtual nodes.

        - Each virtual node is a different hash of the server ID to distribute load.
        - The server is hashed multiple times and placed at different positions.
        """
        self.servers.add(server)
        for i in range(self.num_replicas):  # Creating multiple virtual nodes
            hash_val = self._hash(f"{server}-{i}")  # Unique hash for each virtual node
            self.ring[hash_val] = server  # Map hash to the server
            bisect.insort(self.sorted_keys, hash_val)  # Maintain a sorted list for efficient lookup

    def remove_server(self, server):
        """
        Removes a server and all its virtual nodes from the hash ring.
        """
        if server in self.servers:
            self.servers.remove(server)
            for i in range(self.num_replicas):
                hash_val = self._hash(f"{server}-{i}")  # Remove each virtual node's hash
                self.ring.pop(hash_val, None)  # Delete from hash ring
                self.sorted_keys.remove(hash_val)  # Remove from sorted key list

    def get_server(self, key):
        """
        Finds the closest server for a given key.

        - Hash the key to get its position on the ring.
        - Move clockwise to find the nearest server.
        - If it exceeds the last node, wrap around to the first node.
        """
        if not self.ring:
            return None  # No servers available

        hash_val = self._hash(key)  # Hash the key
        index = bisect.bisect(self.sorted_keys, hash_val) % len(self.sorted_keys)  # Locate nearest server
        return self.ring[self.sorted_keys[index]]  # Return the assigned server

# ----------------- Usage Example -------------------

# Step 1: Initialize Consistent Hashing with servers
servers = ["S0", "S1", "S2", "S3", "S4", "S5"]
ch = ConsistentHashing(servers)

# Step 2: Assign requests (keys) to servers
print(ch.get_server("UserA"))  # Maps UserA to a server
print(ch.get_server("UserB"))  # Maps UserB to a server

# Step 3: Add a new server dynamically
ch.add_server("S6")
print(ch.get_server("UserA"))  # Might be reassigned if affected

# Step 4: Remove a server dynamically
ch.remove_server("S2")
print(ch.get_server("UserB"))  # Might be reassigned if affected