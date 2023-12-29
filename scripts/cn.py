import requests

# 获取IPv4和IPv6地址列表
chinaIPList = "https://raw.githubusercontent.com/pmkol/easymosdns/rules/china_ip_list.txt"
r = requests.get(chinaIPList)

# 读取原始地址文件并转换成单独行的IP-CIDR形式
original_content = r.text.split('\n')
ip_cidr_content = []

for ip in original_content:
    if ip.strip() and '.' in ip:
        ip_cidr = "IP-CIDR," + ip.strip()  # 添加 "IP-CIDR," 前缀
        ip_cidr_content.append(ip_cidr)
    elif ip.strip() and ':' in ip:
        ip_cidr_v6 = "IP-CIDR6," + ip.strip()  # 添加 "IP-CIDR6," 前缀
        ip_cidr_content.append(ip_cidr_v6)

# 写入单独行的"IP-CIDR,IP"形式的内容到新文件
with open("IP.list", "w") as cidr_file:
    for line in ip_cidr_content:
        cidr_file.write(line + '\n')
