import subprocess
import platform
from datetime import datetime

def ping_host(host):
    system = platform.system()
    if system == "Windows":
        cmd = ["ping", "-n", "1", "-w", "1000", host]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", host]
    
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if result.returncode == 0:
        msg = f"[{time_now}] [✓] {host} 在线"
    else:
        msg = f"[{time_now}] [✗] {host} 离线或不可达"
    
    print(msg)
    
    with open("ping_log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

if __name__ == "__main__":
    hosts = [
        "8.8.8.8",
        "114.114.114.114",
        "baidu.com",
        "google.com",
    ]
    for host in hosts:
        ping_host(host)
