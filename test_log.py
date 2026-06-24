import socket
import csv

def check_port(host, port, timeout=3):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            print(f"[✓] {host}:{port} 端口开放")
        else:
            print(f"[✗] {host}:{port} 端口关闭或不可达")
    except Exception as e:
        print(f"[!] 检测失败：{e}")

if __name__ == "__main__":
    targets = [
        ("8.8.8.8", 53),
        ("baidu.com", 80),
        ("baidu.com", 443),
    ]
    for host, port in targets:
        check_port(host, port)
