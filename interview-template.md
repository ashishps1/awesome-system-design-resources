A 7-Step Framework to answer most System Design Interview Problems:

![Template](diagrams/interview-template.png)

𝐒𝐭𝐞𝐩 1: 𝐂𝐥𝐚𝐫𝐢𝐟𝐲 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬:



𝐅𝐮𝐧𝐜𝐭𝐢𝐨𝐧𝐚𝐥 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬:

- What is the scope of the system? 

- What use cases / key features we need to support?



𝐍𝐨𝐧-𝐟𝐮𝐧𝐜𝐭𝐢𝐨𝐧𝐚𝐥 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐦𝐞𝐧𝐭𝐬:

- Consistency vs Availability?

- How big is the user base? 

- What is the read/write ratio?

- What is the expected latency and throughput?



𝐒𝐭𝐞𝐩 2: 𝐂𝐚𝐩𝐚𝐜𝐢𝐭𝐲 𝐄𝐬𝐭𝐢𝐦𝐚𝐭𝐢𝐨𝐧

- Estimate the number of read and write requests.

- Estimate the amount of database and cache storage required.

- Estimate the network bandwidth required.



𝐒𝐭𝐞𝐩 3: 𝐀𝐏𝐈 𝐃𝐞𝐬𝐢𝐠𝐧

- List the System APIs expected from the system based on the use cases.

- Define the API endpoints and request/response format.



𝐒𝐭𝐞𝐩 4: 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐃𝐞𝐬𝐢𝐠𝐧

- Choose the database type based one the needs. For example: SQL or NoSQL.

- Define the Database schema.



𝐒𝐭𝐞𝐩 5: 𝐇𝐢𝐠𝐡-𝐋𝐞𝐯𝐞𝐥 𝐃𝐞𝐬𝐢𝐠𝐧

- Sketch out the block diagram of the system.

- Identify major components like Databases, Servers, Clients, Load Balancers, CDN, Cache, Message Queues etc.



𝐒𝐭𝐞𝐩 6: 𝐃𝐢𝐯𝐞 𝐈𝐧𝐭𝐨 𝐊𝐞𝐲 𝐂𝐨𝐦𝐩𝐨𝐧𝐞𝐧𝐭𝐬

- Go into the specifics of each component. Discuss how each part will work and interact with others.

- Address how each component will scale and perform under load.

- What data structures and algorithms we need to use?



𝐒𝐭𝐞𝐩 7: 𝐀𝐝𝐝𝐫𝐞𝐬𝐬 𝐒𝐜𝐚𝐥𝐚𝐛𝐢𝐥𝐢𝐭𝐲, 𝐅𝐚𝐮𝐥𝐭 𝐓𝐨𝐥𝐞𝐫𝐚𝐧𝐜𝐞 & 𝐑𝐞𝐥𝐢𝐚𝐛𝐢𝐥𝐢𝐭𝐲

- Discuss how the system can scale using concepts like sharding, replication, and partitioning.

- Talk about caching strategies and where caching could be implemented.

- Discuss strategies for handling component failures, like using replicas, fallbacks, and retries.

- Discuss possible performance bottlenecks and how to address them.

- Do we need to throttle requests?

- Discuss authentication, authorization, data encryption, and other security best practices.



This approach works well for most problems but may not be ideal for every type of problem, so feel free to adapt it according to the specific nuances of the interview question.

