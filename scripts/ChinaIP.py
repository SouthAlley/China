import requests

# 获取IPv4地址列表
v4China = "https://raw.githubusercontent.com/pmkol/easymosdns/rules/china_ip_list.txt"
r = requests.get(v4China)

# 读取原始IPv4地址文件并转换成单独行的IP-CIDR形式
original_content = r.text.split('\n')
ip_cidr_content = []

for ip in original_content:
    if ip.strip() and '.' in ip:
        ip_cidr = "IP-CIDR," + ip.strip()  # 添加 "IP-CIDR," 前缀
        ip_cidr_content.append(ip_cidr)

# 获取IPv6地址列表
v6China = "https://raw.githubusercontent.com/pmkol/easymosdns/rules/china_ip_list.txt"
r_v6 = requests.get(v6China)

# 读取原始IPv6地址文件并转换成单独行的IP-CIDR6形式
original_content_v6 = r_v6.text.split('\n')

for ip_v6 in original_content_v6:
    if ip_v6.strip() and ':' in ip_v6:
        ip_cidr_v6 = "IP-CIDR6," + ip_v6.strip()  # 添加 "IP-CIDR6," 前缀
        ip_cidr_content.append(ip_cidr_v6)

# 写入单独行的"IP-CIDR,IP"形式的内容到新文件
with open("IP.China.list", "w") as cidr_file:
    for line in ip_cidr_content:
        cidr_file.write(line + '\n')
