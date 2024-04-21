#-*- coding:utf-8 -*-
def CheckPhonenum(phonenum):
    phonelist = []
    
    if len(phonenum) == 11 and str(phonenum).isdigit() and (int(phonenum[:3]) in phonelist):
        return True
    else:
        return False
    
    
def CheckUserIdNotRepeat(userid):
    #检测账号是否重复
    
    
def CheckIdCard(idcard):
    
    
    
def CheckPassword(password):
    