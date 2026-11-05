import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LeastConnectionsTest {
    public static void main(String[] args) {
        List<String> servers = List.of("Server1", "Server2", "Server3");
        LeastConnections loadBalancer = new LeastConnections(servers);
        Map<String, Integer> assignments = new HashMap<>();

        for (int i = 0; i < 6; i++) {
            String server = loadBalancer.getNextServer();
            if (server == null) {
                throw new AssertionError("expected a server assignment");
            }
            assignments.merge(server, 1, Integer::sum);
        }

        if (assignments.size() != servers.size()
                || assignments.values().stream().anyMatch(count -> count != 2)) {
            throw new AssertionError("six active connections should be balanced: " + assignments);
        }

        if (new LeastConnections(List.of()).getNextServer() != null) {
            throw new AssertionError("an empty server list should return null");
        }

        System.out.println("LeastConnections tests passed");
    }
}
