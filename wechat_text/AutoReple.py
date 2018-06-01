import itchat
import time
#自动回复
#封装好的装饰器，当接受到的消息是Test，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    #当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        #发送一条提示给助手
        itchat.send_msg(u'[%s]收到好友@%s 的信息: %s\n' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
        msg['User']['NickName'],
        msg['Text']), 'filehelper')
    return u'不在,收到消息:%s\n' % (msg['Text'])

if __name__ == '__main__':
    itchat.auto_login()
    myUserName = itchat.get_friends(update=True)[0]['UserName']
    itchat.run()