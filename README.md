# Ping-Test-using-Python


This is a simple Python Script which takes in the IP addresses as the Input and pings those IP addresses to determine if they are up or not.

Note: The script does not validate the IP address format(for eg 3 octets). Error handling is not embedded in this scrip.



Example Input:
Enter the number of IPs to test 2

('Entern the IP address', 1)
1.1.1.1

('Entern the IP address', 2)
8.8.8.8

Output:

PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=54 time=1.45 ms

--- 1.1.1.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.458/1.458/1.458/0.000 ms
1.1.1.1 is up!
================================

PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=51 time=0.807 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0
8.8.8.8 is up!
