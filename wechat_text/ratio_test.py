import itchat
from echarts import Echart, Legend, Pie

#login wechat
itchat.login()
#获取好友列表
friends = itchat.get_friends(update=True)[0:]
male = female = other = 0
#遍历列表
#1 = male 2 = female
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
#计算比例
total = len(friends[1:])
print(u"男性好友：%.2f%%" % float(male/total*100))
print(u"女性好友：%.2f%%" % float(female/total*100))
print(u"其他好友：%.2f%%" % float(other/total*100))
chart = Echart(u'friends%s' % (friends[0]['NickName']), 'from WeChat')
chart.use(Pie('WeChat',
              [{'value': male, 'name': u"male %.2f%%" % float(male/total*100)},
               {'value': female, 'name': u"female %.2f%%" % float(female/total*100)},
               {'value': female, 'name': u"other %.2f%%" % float(female/total*100)}],
              radius=["50%", "70%"]))
chart.use(Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()

