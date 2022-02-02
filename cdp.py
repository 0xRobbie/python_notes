import re

with open("cdpNeighborsDetails.txt", "r") as file:
    for line in file:

        device_id = re.search(r'(Device ID: )(.*)', line)
        if device_id:
            print(device_id.group())

        ip_address = re.search(r'(IP address: )(.*)', line)
        if ip_address:
            print(ip_address.group())

        interface_and_port = re.search(r'(Interface: )([a-zA-Z0-9]*/[0-9]*, )( Port ID \(outgoing port\):)( [a-zA-Z0-9]*/[0-9]*)', line)
        if interface_and_port:
            print(interface_and_port.group())
        
        
####################
## Device ID:
## IP address:
## Interface:
## Port ID (outgoing port):