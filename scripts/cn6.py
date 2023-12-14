# 导入requests模块
import requests

# 获取IPv6地址列表
v4China = "https://ispip.clang.cn/all_cn_ipv6.txt"
r = requests.get(v4China)

# 读取原始IPv4地址文件并转换成单独行的IP-CIDR形式
original_content = r.text.split('\n')
ip_cidr_content = []

for ip in original_content:
    if ip.strip() and '.' in ip:
        ip_cidr = "IP-CIDR6," + ip.strip()  # 添加 "IP-CIDR," 前缀
        ip_cidr_content.append(ip_cidr)

# 写入单独行的"IP-CIDR,IP"形式的内容到新文件
with open("China6.list", "w") as cidr_file:
    for line in ip_cidr_content:
        cidr_file.write(line + '\n')
