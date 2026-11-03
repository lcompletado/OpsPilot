import socket

def check_tcp(host, port):
    client_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client_socket.settimeout(3)

    try:
        client_socket.connect((host, port))
        return "CONNECTED"
    except socket.gaierror:
        return "DNS_ERROR"
    except socket.timeout:
        return "TIMEOUT"
    except ConnectionRefusedError:
        return "REFUSED"
    except OSError:
        return "ERROR"
    finally:
        client_socket.close()

result = check_tcp("google.com", 443)
print(result)