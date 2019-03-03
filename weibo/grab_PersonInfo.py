# encoding: utf-8
import requests
import re
from bs4 import BeautifulSoup
import time
import bs4
import xlwt
import xlrd

def getHTMLText(url):
    print("函数"+url)
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; whl=-1%260%260%260; x5sec=7b22726174656d616e616765723b32223a226234313136323630316336656330663034663235306532613837356333316565434e65617a2b4d46454c50566b66486b6a4f6e3155426f4d4d6a597a4d7a51774d5467304e6a7378227d; l=bBOZfxjIviwswoijBOfiCQhjnmbt2QAfGNVP2FyFKICPO7BB5HUdWZac8Kx6C3GVa6d6R3RYGVWzBVTityUCh; isg=BFNTkOBVCwlcksO-YYx8M5pH4tfRHL2WHB0yewVymHLVhHYmjdsxGlgSvrRPFj_C'
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; whl=-1%260%260%260; x5sec=7b22726174656d616e616765723b32223a226234313136323630316336656330663034663235306532613837356333316565434e65617a2b4d46454c50566b66486b6a4f6e3155426f4d4d6a597a4d7a51774d5467304e6a7378227d; l=bBOZfxjIviwswkkwBOfiCQhjnmbtzQdfhNVP2FyFKICPOvWe5HUdWZacDttwC3GVa6IvR3RYGVWzBS8gCy4Fh; isg=BIeH88zRl212jBeC3YhwVy4LFjv9mAEyCOHGZ1l3e5QiyKuKYV_Wv_pOasgzJzPm'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551254824932%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D; WBStorage=f3685954b8436f62|undefined'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551262022905%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551268319906%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    # cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551323307713%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    #cookie = "SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; UOR=,,login.sina.com.cn; SSOLoginState=1551242532; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; ALF=1582865611; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm69uEVvmR0u4W0XlY0i6rYFqhp4ZSlvjoVU-mB1M-0R5A.; SUB=_2A25xcxkdDeRhGeBO6VQY-C3EyjSIHXVSCQ3VrDV8PUNbmtBeLWLjkW9NSjaarFo6SUIMpAa7qfkkB4fF21m-Iqta; SUHB=0qj0bkTHq9ODAk; webim_unReadCount=%7B%22time%22%3A1551330886810%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D"
    #referer = 'https://weibo.com/6026983818/profile?topnav=1&wvr=6&is_all=1'
    #referer = 'https://s.weibo.com/weibo?q=%23%E8%B7%9F%E9%A3%8E%E4%B9%B0%20%E5%8F%A3%E7%BA%A2%E5%A7%A8%E5%A6%88%E5%B7%BE%23&page=2'
    # 爬取评论
    #TODO
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SSOLoginState=1551399840; _s_tentry=login.sina.com.cn; UOR=,,www.baidu.com; Apache=2387478572198.8535.1551399807393; ULV=1551399807544:84:1:6:2387478572198.8535.1551399807393:1551242533621; ALF=1582935900; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6XRMEyc0lYTYaNwArH_3Qg7VEdT-kpAjSR6sYdzYHiBU.; SUB=_2A25xfAuNDeRhGeBO6VQY-C3EyjSIHXVSCHpFrDV8PUNbmtBeLRjHkW9NSjaarBopvFfRuSvpnUFYiQk-p2XvSgOv; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KzhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; SUHB=0G0u2Zg9LzJDbL; webim_unReadCount=%7B%22time%22%3A1551422510734%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    #TODO
    referer = 'https://weibo.com/p/1005052102180125/follow?page=1&sudaref=s.weibo.com&display=0&retcode=6102' # follow
    #爬取follow
    cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; wb_view_log_6026983818=1920*10801.25; YF-Page-G0=8fee13afa53da91ff99fc89cc7829b07; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; ALF=1582958822; SSOLoginState=1551422823; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm62flbDF2MYl7HFYpVeHt8fDflvKwcF_lI2w1BnUkIhWw.; SUB=_2A25xfKU3DeRhGeBO6VQY-C3EyjSIHXVSC5H_rDV8PUNbmtBeLWvtkW9NSjaarCj62vanI83T_gatIyWYZXAK5RN_; SUHB=0qj0bkTHq9OB5h; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=9828838594195.492.1551422825431; ULV=1551422825554:85:2:7:9828838594195.492.1551422825431:1551399807544; YF-V5-G0=5468b83cd1a503b6427769425908497c; Ugrow-G0=7e0e6b57abe2c2f76f677abd9a9ed65d; webim_unReadCount=%7B%22time%22%3A1551442102726%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    #cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; UOR=,,login.sina.com.cn; SSOLoginState=1551242532; YF-V5-G0=020421dd535a1c903e89d913fb8a2988; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; YF-Page-G0=ed0857c4c190a2e149fc966e43aaf725; Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; wb_view_log_6026983818=1920*10801.25; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; ALF=1582865611; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm69uEVvmR0u4W0XlY0i6rYFqhp4ZSlvjoVU-mB1M-0R5A.; SUB=_2A25xcxkdDeRhGeBO6VQY-C3EyjSIHXVSCQ3VrDV8PUNbmtBeLWLjkW9NSjaarFo6SUIMpAa7qfkkB4fF21m-Iqta; SUHB=0qj0bkTHq9ODAk; webim_unReadCount=%7B%22time%22%3A1551363574686%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    #cookie = 'YF-Page-G0=46f5b98560a83dd9bfdd28c040a3673e'
    #referer = 'https://weibo.com/p/1005052102180125/follow?page=1&sudaref=s.weibo.com&display=0&retcode=6102'
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Cookie': cookie, 'Referer': referer,'Connection': 'keep-alive','Accept-Encoding': 'gzip, deflate', 'Accept': '*/*'}, timeout=10)
        print(r.request.headers)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        return "---------------无法连接---------------"

def getComment(customID,commentList,pushTime,errorList):
    print("调用parsePage")
    count = 1
    while len(commentList) < 400 :
        print(count)
        print(len(commentList))
        try:
            #https: // weibo.com / u / 5129488433?is_search = 0 & visible = 0 & is_all = 1 & is_tag = 0 & profile_ftype = 1 & page = 3  # feedtop
            #url =
            #url = "https://weibo.com/u/"+str(customID)+"?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page="+str(count)+"#feedtop"
            #url = "https://weibo.com/p/1005051562697291/home?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page="+str(count)+"#feedtop"
            #url = 'https: // weibo.com / fyy1211?is_search = 0 & visible = 0 & is_all = 1 & is_tag = 0 & profile_ftype = 1 & page = '+str(count)+'  # feedtop'
            #TODO 字母开头的
            url = "https://weibo.com/"+customID+"?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page="+str(count)+"#feedtop"
            url = "https://weibo.com/u/2841734211?profile_ftype=1&is_all=1# _0"
            #大部分的url
            #url = "https://weibo.com/u/"+customID+"?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&"+"page="+str(count)+"&sudaref=s.weibo.com&display=0&retcode=6102"
            print(url)
            html = getHTMLText(url)
            # print(html)
            html = html.replace("\\t", "").replace("\\n", "").replace("\\r", "").replace("\\", "")
            html = html[html.find("<div class=\"WB_feed WB_feed_v3 WB_feed_v4\""):]
            soup = BeautifulSoup(html, 'html.parser')
            # print(html)
            list_a = soup.findAll(name="div", attrs={"class": "WB_detail"})
            if list_a:
                for i in list_a:
                    print("评论")
                    print(i)
                    comment = i.text
                    print(comment)
                    comment = comment.replace(" ", "")
                    if comment:
                        time = re.findall(r'[0-9][0-9]\:[0-9][0-9]', comment)[0]
                        pushTime.append(time)
                        #comment = re.findall(r'来自.*',comment)[0]
                        commentList.append(comment)
                        print(comment)
            else:
                break
        except:
            print("解析失败")
            errorList.append(customID)
            pass
        count = count + 1

def getFollow(customID, followList,errorList):
    print("调用getFollow")

    count = 1
    while True:
        try:
            #https://weibo.com/p/1005052102180125/follow?pids=Pl_Official_HisRelation__59&page=2
            #url = "https://weibo.com/p/100505"+str(customID)+"/follow?page="+str(count)+"&sudaref=s.weibo.com&display=0&retcode=6102"
            url = "https://weibo.com/p/100505"+str(customID)+"/follow?pids=Pl_Official_HisRelation__59&page="+str(count)+"&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fp%2F1005052102180125%2Ffollow%3Fpage%3D1%26sudaref%3Ds.weibo.com%26display%3D0%26retcode%3D6102&_t=FM_155136356143614"
            print(url)
            html = getHTMLText(url)
            soup = soup = BeautifulSoup(html, 'html.parser')
            print(html)
            print("。。。。。。。。。。。。。。。。。。")

            area = re.findall(r'<li class=\\"follow_item S_line2\\".*?class=\\"info_from\\">',html)
            # 先大范围的抽取信息
            if len (area) > 0 :
                for a in area:
                    name = ''
                    id = ''
                    intro = ''
                    fan = '0'
                    follow = '0'
                    neirong = '0'
                    # 提取名字
                    followName = re.findall(r'<li class=\\"follow_item S_line2\\".*?>', a)
                    if len(followName) > 0:
                        name = re.findall(r'[0-9]{5,}', followName[0])[0]
                        print(name)
                        id = re.findall(r'fnick=.*?&', followName[0])[0]
                        id = id.replace('fnick=', '')
                        id = id.replace('&', '')
                        print(id)

                    # 提取简介
                    followIntro = re.findall(r'<div class=\\"info_intro\\">.*?<\\/span>', a)
                    if len(followIntro) > 0:
                        intro = re.findall(r'<span>.*?<\\/span>', followIntro[0])[0]
                        intro = intro.replace('<span>', '').replace('<\/span>', '')
                        print(intro)

                    # 粉丝、关注量、发微博数目
                    followPower = re.findall(r'<span class=\\"conn_type.*?<\\/span>', a)
                    # 关注者
                    print(len(followPower))
                    if len(followPower) == 3:
                        follow = re.findall(r'>[0-9]+<', followPower[0])[0]
                        follow = follow.replace('>', '').replace('<', '')
                        # 粉丝
                        fan = re.findall(r'>[0-9]+<', followPower[1])[0]
                        fan = fan.replace('>', '').replace('<', '')
                        # 微博
                        neirong = re.findall(r'>[0-9]+<', followPower[2])[0]
                        neirong = neirong.replace('>', '').replace('<', '')
                        print(follow)
                        print(fan)
                        print(neirong)
                        print('。。。。。。。。。。。。。。。。')

                    followList.append(
                        {'name': name, 'id': id, 'intro': intro, 'follow': follow, 'fan': fan, 'content': neirong})
            else:
                break
        except:
            print("关注着解析失败")
            if not errorList.__contains__(customID):
                errorList.append(customID)
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


def commentWriteToExcel(customID, commentList,pushTime):
    # -------------检测解析是否正确--------------------
    print("评论"+str(len(commentList)))
    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('#')
    for i in range(len(commentList)):
        worksheet.write(i, 0, pushTime[i], style)
        worksheet.write(i, 1, commentList[i], style)
    workbook.save('comment/1/'+str(customID)+'.xls')

def followWriteToExcel(customID,followList):
    # -------------检测解析是否正确--------------------
    print("评论"+str(len(followList)))
    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('#')
    worksheet.write(0, 0, 'name', style)
    worksheet.write(0, 1, 'id', style)
    worksheet.write(0, 2, 'intro', style)
    worksheet.write(0, 3, 'follow', style)
    worksheet.write(0, 4, 'fan', style)
    worksheet.write(0, 5, 'concent', style)
    for i in range(1,len(followList)):
        worksheet.write(i, 0, followList[i]['name'], style)
        worksheet.write(i, 1, followList[i]['id'], style)
        worksheet.write(i, 2, followList[i]['intro'], style)
        worksheet.write(i, 3, followList[i]['follow'], style)
        worksheet.write(i, 4, followList[i]['fan'], style)
        worksheet.write(i, 5, followList[i]['content'], style)
    workbook.save('follow/'+str(customID)+'.xls')

# 得到两个话题筛选出来的有效ID
def getAvalidID(avalidID):
    exfile = xlrd.open_workbook("C:/Users/yuyu/Desktop/宝洁challenge/复赛/数据/cleanData/#掌心包话题用户ID.xlsx")
    sheet1 = exfile.sheet_by_name('Sheet1')  # 读取Sheet1的内容，根据实际情况填写表名

    n = sheet1.nrows  # 表的总行数
    for i in range(1, n):
        text = sheet1.row(i)[2].value  # 从第0行开始计数，第0行是栏目，第1行是要的内容
        # //weibo.com/1796405533?refer_flag=1001030103_
        cleanText = re.findall(r'[0-9]+', text)[0]
        if not avalidID.__contains__(cleanText):
            avalidID.append(cleanText)



#把提取出来的有效ID，写进表格
def writeAvalidID(avalidID):
    for i in avalidID:
        print(i)
    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('Sheet1')
    for i in range(len(avalidID)):
        worksheet.write(i, 0, avalidID[i], style)
    workbook.save('用户的有效ID.xls')


def main():
    '''
    #提取出用户的有效ID
    customID = []
    getAvalidID(customID)
    writeAvalidID(customID)
    '''

    '''
    
    '''
    customID = [] #用户的ID
    pushTime = [] #发表的时间
    commentList = [] #评论的列表
    errorList = [] #出错的列表
    followList = []
    ID = []
    name = []
    #TODO 从文件，读取用户的ID列表
    #customID = ['3256809975']
    getAvalidID(customID)
    for i in range(len(customID)):
        '''
        # 抓取每个用户的微博内容
        getComment(customID[i], commentList,pushTime,errorList)  # 获取这个用户的评论
        commentWriteToExcel(customID[i],commentList,pushTime)
        commentList.clear()
        pushTime.clear()        
        '''
        # 抓取每个用户的follow
        getFollow(customID[i],followList,errorList)
        followWriteToExcel(customID[i], followList)
        followList.clear()
    for i in errorList:
        print(i)
main()