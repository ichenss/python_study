#-*- coding:utf-8 -*-
import Config
import AccountCfg
import re

def CheckPhonenum(phonenum):
    phonelist = [139, 138, 137, 136, 134, 135, 147, 150, 151, 152, 157, 158, 159, 172, 178,
            130, 131, 132, 140, 145, 146, 155, 156, 166, 185, 186, 175, 176, 196,
            133, 149, 153, 177, 173, 180, 181, 189, 191, 193, 199,
            162, 165, 167, 170, 171]
    
    if len(phonenum) == 11 and str(phonenum).isdigit() and (int(phonenum[:3]) in phonelist):
        return True
    else:
        return False
    
    
def CheckUserIdNotRepeat(userid):
    #检测账号是否重复
    pass
    
def CheckIdCard(idcard):
    stridcard = str(idcard)
    stridcard = stridcard.strip()
    idcard_list = list(stridcard)
    # 地区校验
    if (stridcard)[0:2] not in AccountCfg.AREAID:
        return False

    # 15位身份号码检测
    if len(stridcard) == 15:
        if ((int(stridcard[6:8]) + 1900) % 400 == 0 or (
                (int(stridcard[6:8]) + 1900) % 100 != 0 and (int(stridcard[6:8]) + 1900) % 4 == 0)):
            pattern = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')  # //测试出生日期的合法性
        else:
            pattern = re.compile(
                '[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')  # //测试出生日期的合法性
        if re.match(pattern, stridcard):
            return True
        else:
            return False
    # 18位身份号码检测
    elif len(stridcard) == 18:
        # 出生日期的合法性检查
        # 闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
        # 平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
        if (int(stridcard[6:10]) % 400 == 0 or (int(stridcard[6:10]) % 100 != 0 and int(stridcard[6:10]) % 4 == 0)):
            # 闰年出生日期的合法性正则表达式
            pattern = re.compile(
                '[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')
        else:
            # 平年出生日期的合法性正则表达式
            pattern = re.compile(
                '[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')
        # 测试出生日期的合法性
        if re.match(pattern, stridcard):
            # 计算校验位
            ten = ['X', 'x']
            ID = ["10" if x in ten else x for x in idcard_list]     #将字母X/x替换为10
            IDWeight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            Checkcode = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
            sum = 0
            for i in range(17):
                sum += int(ID[i]) * IDWeight[i]
            if Checkcode[sum % 11] == int(ID[17]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

    
    
def CheckPassword(password):
    #字母和数字组合，8-16位
    pattern = re.compile('^(?=.*[0-9])(?=.*[A-z])[0-9a-zA-Z]{8,16}$')
    if re.match(pattern, password):
        return True
    return False
