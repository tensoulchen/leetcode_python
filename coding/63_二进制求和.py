# 进位加法原理

def addBinary(a: str, b: str) -> str:
    if len(a) < len(b):
        a, b = b, a  # 限定b为位数少
    b = '0' * (len(a) - len(b)) + b  # 给b的补上位数，如a为11，则b为01
    res = ''
    carry = 0
    for i in range(len(a)):
        aNum = int(a[-i - 1])
        bNum = int(b[-i - 1])
        res = str((aNum + bNum + carry) % 2) + res  # 计算每次模拟最后的结果值
        carry = (aNum + bNum + carry) // 2  # 计算每次模拟的进位

    if carry == 1:          #判断最后是否要进位
        res = '1' + res
    return res

a='1010'
b='1011'
print(addBinary(a,b))