# encoding: utf-8
import requests
import re
from bs4 import BeautifulSoup
import time
import bs4
import xlwt

def getHTMLText(url):
    print("函数"+url)
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; whl=-1%260%260%260; x5sec=7b22726174656d616e616765723b32223a226234313136323630316336656330663034663235306532613837356333316565434e65617a2b4d46454c50566b66486b6a4f6e3155426f4d4d6a597a4d7a51774d5467304e6a7378227d; l=bBOZfxjIviwswoijBOfiCQhjnmbt2QAfGNVP2FyFKICPO7BB5HUdWZac8Kx6C3GVa6d6R3RYGVWzBVTityUCh; isg=BFNTkOBVCwlcksO-YYx8M5pH4tfRHL2WHB0yewVymHLVhHYmjdsxGlgSvrRPFj_C'
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; whl=-1%260%260%260; x5sec=7b22726174656d616e616765723b32223a226234313136323630316336656330663034663235306532613837356333316565434e65617a2b4d46454c50566b66486b6a4f6e3155426f4d4d6a597a4d7a51774d5467304e6a7378227d; l=bBOZfxjIviwswkkwBOfiCQhjnmbtzQdfhNVP2FyFKICPOvWe5HUdWZacDttwC3GVa6IvR3RYGVWzBS8gCy4Fh; isg=BIeH88zRl212jBeC3YhwVy4LFjv9mAEyCOHGZ1l3e5QiyKuKYV_Wv_pOasgzJzPm'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551254824932%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D; WBStorage=f3685954b8436f62|undefined'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551262022905%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551268319906%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551323307713%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    #cookie = "SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; UOR=,,login.sina.com.cn; SSOLoginState=1551242532; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; ALF=1582865611; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm69uEVvmR0u4W0XlY0i6rYFqhp4ZSlvjoVU-mB1M-0R5A.; SUB=_2A25xcxkdDeRhGeBO6VQY-C3EyjSIHXVSCQ3VrDV8PUNbmtBeLWLjkW9NSjaarFo6SUIMpAa7qfkkB4fF21m-Iqta; SUHB=0qj0bkTHq9ODAk; webim_unReadCount=%7B%22time%22%3A1551330886810%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D"
    #referer = 'https://weibo.com/6026983818/profile?topnav=1&wvr=6&is_all=1'
    referer = 'https://s.weibo.com/weibo?q=%23%E8%B7%9F%E9%A3%8E%E4%B9%B0%20%E5%8F%A3%E7%BA%A2%E5%A7%A8%E5%A6%88%E5%B7%BE%23&page=2'
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Cookie': cookie, 'Referer': referer}, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        return "---------------无法连接---------------"

def getComment(customID,commentList):
    print("调用parsePage")
    count = 1
    while len(commentList) < 400 :
        print(count)
        print(len(commentList))
        try:
            #https: // weibo.com / u / 5129488433?is_search = 0 & visible = 0 & is_all = 1 & is_tag = 0 & profile_ftype = 1 & page = 3  # feedtop
            #url =
            #url = "https://weibo.com/u/"+str(customID)+"?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page="+str(count)+"#feedtop"
            url = "https://weibo.com/u/"+customID+"?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&"+"page="+str(count)+"&sudaref=s.weibo.com&display=0&retcode=6102"
            print(url)
            html = getHTMLText(url)
            print(html)
            html = html.replace("\\t", "").replace("\\n", "").replace("\\r", "").replace("\\", "")
            html = html[html.find("<div class=\"WB_feed WB_feed_v3 WB_feed_v4\""):]
            soup = BeautifulSoup(html, 'html.parser')
            print("。。。。。。。。。。。。。。。。")
            print(html)
            list_a = soup.findAll(name="div", attrs={"class": "WB_detail"})
            if list_a:
                for i in list_a:
                    print(i)
                    comment = i.text
                    comment = comment.replace(" ", "")
                    if comment:
                        commentList.append(comment)
                        print(comment)
            else:
                break
        except:
            print("解析失败")
            pass
        count = count + 1

def getFollow(customID, fanList):
    print("调用getFollow")
    count = 1
    while count < 2 :
        try:
            url = "https://weibo.com/p/100505"+str(customID)+"/follow?page="+str(count)+"&sudaref=s.weibo.com&display=0&retcode=6102"
            print(url)
            html = getHTMLText(url)
            print(html)
            html = html.replace('\\n', '').replace('\\t', '').replace('\\r', '').replace('\\', '')
            html = html[html.find("<!--关注/粉丝列表-->"):html.find("<!--关欧盟隐私协议弹窗-->")]
            print(html)
            soup = BeautifulSoup(html, "html.parser")
            list_a = soup.findAll(name='div', attrs={"class": "info_name W_fb W_f14"})
        except:
            print("关注着解析失败")
            pass
        count = count + 1


        '''
        name = []
        uid = []
        for a in list_a:
            try:
                b = a.find(name="a")
                b = b['usercard']
                b = b[3:13:]
                uid.append(b)
                name.append(a.text)
                print("加入用户:" + a.text)
            except:
                print("No Data")
        dic = {"name": name, "uid": uid}
        return dic
        '''


def commentWriteToExcel(customID, commentList):
    # -------------检测解析是否正确--------------------
    print("评论"+str(len(commentList)))
    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('#')
    for i in range(len(commentList)):
        worksheet.write(i, 0, commentList[i], style)
    workbook.save('comment/'+str(customID)+'.xls')

def followWriteToExcel(customID,fanList):
    print("")


def main():
    commentList = []
    fanList = []
    ID = []
    name = []
    # comment_url = "https://weibo.com/6026983818/profile?topnav=1&wvr=6&is_all=1"
    #TODO 从文件，读取用户的ID列表
    customID = ['2102180125','6026983818']
    for i in range(len(customID)):
        #getComment(customID[i], commentList)  # 获取这个用户的评论
        #commentWriteToExcel(customID[i],commentList)
        #commentList.clear()
        getFollow(customID[i], fanList)


    for j in range(len(commentList)):
        print(commentList[j])
    print(len(commentList))
main()