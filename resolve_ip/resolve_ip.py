import socket

def resolve_hostname(hostname):
    try:
        ipv4 = socket.gethostbyname(hostname)
    except socket.gaierror:
        ipv4 = 'Not Found'
    
    try:
        ipv6 = socket.getaddrinfo(hostname, None, socket.AF_INET6)
        ipv6 = ipv6[0][4][0] if ipv6 else 'Not Found'
    except socket.gaierror:
        ipv6 = 'Not Found'
    
    return ipv4, ipv6

def main():
    with open('input.txt', 'r') as infile:
        hostnames = infile.read().splitlines()
    
    with open('output.txt', 'w') as outfile:
        outfile.write('Hostname\tIPv4\t\tIPv6\n')
        outfile.write('-' * 50 + '\n')
        
        for hostname in hostnames:
            ipv4, ipv6 = resolve_hostname(hostname)
            outfile.write(f'{hostname}\t{ipv4}\t{ipv6}\n')

if __name__ == "__main__":
    main()
