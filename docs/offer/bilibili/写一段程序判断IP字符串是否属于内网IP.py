ip = input().split('.')
# 链接：https://www.nowcoder.com/questionTerminal/80ce674313ff43af9d7ac7a41ae21527
# 来源：牛客网

#     // A类地址：10.0.0.0--10.255.255.255
#     // B类地址：172.16.0.0--172.31.255.255 
#     // C类地址：192.168.0.0--192.168.255.255
if ip[0] == '10':
    print(1)
elif ip[0] == '172':
    if ip[1] >= '16' and ip[1] <= '32':
        print(1)
    else:
        print(0)
elif ip[0] == '192' and ip[1] == '168':
    print(1)
else:
    print(0)