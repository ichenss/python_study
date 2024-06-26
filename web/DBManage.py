#-*- coding:utf-8 -*-
import Config

def InsertRegisterUser(phonenum, password, nick, sex, idcard, now):
    Config.gdb.insert(
        "user",
        userid = int(phonenum),
        password = password,
        secpassword = Config.DEFAULT_SECPASSWORD,
        nick = nick,
        phonenum = phonenum,
        sex = sex,
        idcard = idcard,
        status = Config.USER_STATUS_NORMAL,
        createtime = now,
        lastlogintime = now,
    )

