import subprocess
import platform

def ping_host(host):
    system = platform.system()
    if system == "Windows":
        cmd = ["ping", "-n", "1", "-w", "1000", host]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", host]
    
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if result.returncode == 0:
        print(f"[✓] {host} 在线")
    else:
        print(f"[✗] {host} 离线或不可达")

if __name__ == "__main__":
    hosts = [
        "8.8.8.8",
        "114.114.114.114",
        "baidu.com",
        "google.com",
    ]
    for host in hosts:
        ping_host(host)
