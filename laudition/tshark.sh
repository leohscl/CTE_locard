tshark -R icmp -r capture.pcap -2 -T fields -e data > out
