#-*- coding:utf-8 -*-
import web
import Account
import json
import ErrorCfg
import Error

urls = (
    '/(.*)', 'hello',
    '/register', 'Register'
)

app = web.application(urls, globals())
application = app.wsgifunc()

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello,' + name
    
class Register:
    def POST(self):
        req = web.input(phonenum='', password='', nick='', sex='', idcard='')
        phonenum = req.phonenum
        password = req.password
        nick = req.nick
        sex = req.sex
        idcard = req.idcard
        # 检测手机号格式
        if not Account.CheckPhonenum(phonenum):
            return Error.ErrResult(ErrorCfg.EC_REGISTER_PHONENUM_TYPE_ERROR, ErrorCfg.ER_REGISTER_PHONENUM_TYPE_ERROR)
        
        # 检测账号是否重复
        if not Account.CheckUserIdNotRepeat(phonenum):
            return Error.ErrResult(ErrorCfg.EC_REGISTER_USERID_REPEAT, ErrorCfg.ER_REGISTER_USERID_REPEAT)

        # 检测身份证号格式
        if not Account.CheckIdCard(idcard):
            return Error.ErrResult(ErrorCfg.EC_REGISTER_IDCARD_TYPE_ERROR, ErrorCfg.ER_REGISTER_IDCARD_TYPE_ERROR)

        # 检测密码格式
        if not Account.CheckPassword(password):
            return Error.ErrResult(ErrorCfg.EC_REGISTER_PASSWORD_TYPE_ERROR, ErrorCfg.ER_REGISTER_PASSWORD_TYPE_ERROR)

        # 注册账号
        
        return json.dumps({'code':0})
        
# if __name__ == "__main__":
#     app.run()
