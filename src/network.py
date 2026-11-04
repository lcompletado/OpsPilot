import socket

def resolve_host(host):
    try:
        ip_address = socket.gethostbyname(host)
        return ip_address
    except socket.gaierror:
        return None

def check_tcp(ip_address, port):
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client_socket.settimeout(3)

    try:
        client_socket.connect((ip_address, port))
        return "CONNECTED"
    except socket.timeout:
        return "TIMEOUT"
    except ConnectionRefusedError:
        return "REFUSED"
    except OSError:
        return "ERROR"
    finally:
        client_socket.close()