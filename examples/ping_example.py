#!/usr/bin/env python3
"""
Simple example demonstrating scapy-socketlogger by sending an ICMP ping
and logging the traffic to a PCAP file.
"""

import scapy.all as scapy
from scapy_socketlogger import SocketLogger

def main():
    # Create a layer 3 socket for sending IP packets
    sock = scapy.conf.L3socket()

    # Create a PCAP writer to log traffic
    pcap_writer = scapy.PcapWriter("ping.pcap")

    # Wrap the socket with the logger
    logger = SocketLogger(sock, pcap_writer)

    try:
        # Create an ICMP echo request packet
        pkt = scapy.IP(dst="8.8.8.8") / scapy.ICMP()

        print("Sending ping to 8.8.8.8...")

        # Send the packet (this will be logged)
        sock.send(pkt)

        print("Packet sent. Note: Receiving replies may require root/admin privileges on some systems.")

        print("Traffic logged to ping.pcap")

    finally:
        # Close the logger (flushes PCAP and restores socket methods)
        logger.close()

if __name__ == "__main__":
    main()