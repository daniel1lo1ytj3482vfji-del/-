import paramiko

# 你的服务器信息
hostname = "39.105.70.21"
username = "root"
password = " "  # 替换成你设置的密码

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=22, username=username, password=password, timeout=10)
    
    # 执行一个简单命令验证
    stdin, stdout, stderr = client.exec_command("echo '连接成功' && whoami")
    print(stdout.read().decode())
    
    client.close()
    print("SSH登录测试通过 ✅")

except Exception as e:
    print(f"连接失败 ❌：{e}")
