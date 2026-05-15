import socket
from datetime import datetime

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        s.close()
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if result == 0:
            print(f"[{time_now}] [✓] {host}:{port} 开放")
        else:
            print(f"[{time_now}] [✗] {host}:{port} 关闭")
    except Exception as e:
        print(f"错误：{e}")

if __name__ == "__main__":
    host = "8.8.8.8"
    ports = [22, 80, 443, 8080]
    for port in ports:
        scan_port(host, port)
