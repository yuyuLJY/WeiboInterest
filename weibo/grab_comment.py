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
    cookie = 'SINAGLOBAL=4742016696836.8.1477481516999; UM_distinctid=166bac7d2f3106-0b4f1162cdeae8-75283355-1fa400-166bac7d2f431e; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFCuMqd_rdh7q_PEUg_rczQ5JpX5KMhUgL.Foq7eoq41heReKn2dJLoIEXLxK-L12BL1KMLxKqLB.2LB-2LxK-LB.-L1hnLxKnLBoBLBoBLxK-LB.qL1het; UOR=,,login.sina.com.cn; ALF=1582778531; SSOLoginState=1551242532; SCF=Aj3y1uTPbfer9jmpp6zz5hb6IzjCFuGz8KBYNMoSXdm6F9-LL4LcJYLqbiWkE5vGk_YOSYBj_8yVGXHJ6WvAGsE.; SUB=_2A25xcmV0DeRhGeBO6VQY-C3EyjSIHXVSBtG8rDV8PUNbmtBeLXj6kW9NSjaarCOlBh8ZYlJpbRDW_D5DExvwlBg7; SUHB=0sqBUcsZuLYp-6; _s_tentry=login.sina.com.cn; Apache=9966830248485.545.1551242533533; ULV=1551242533621:83:5:5:9966830248485.545.1551242533533:1551239427972; webim_unReadCount=%7B%22time%22%3A1551268319906%2C%22dm_pub_total%22%3A3%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D'
    referer = 'https://s.weibo.com/weibo?q=%23%E8%B7%9F%E9%A3%8E%E4%B9%B0%20%E5%8F%A3%E7%BA%A2%E5%A7%A8%E5%A6%88%E5%B7%BE%23&page=2'
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Cookie': cookie, 'Referer': referer}, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        return "---------------无法连接---------------"

def parsePage(ID,commentList,name,html):
    print("调用parsePage")
    try:
        soup = BeautifulSoup(html, 'html.parser')
        for i in soup.findAll(name='div', attrs={'class': 'content', 'node-type': 'like'}):
            divs = i('div')
            print(i)
            infoA = divs[0].find(name='a',attrs = {'target':'_blank'})
            ID.append(infoA.attrs['href'])
            name.append(infoA.attrs['nick-name'])
            print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")
            ps = i('p')[0]
            commentList.append(ps.get_text())
            print(ps)
    except:
        print("解析失败")

    '''
               for i in soup.findAll(name='a', attrs={'class': 'name','target': '_blank'}):
            try:
                print(i) # <a class="name" href="//weibo.com/2102180125?refer_flag=1001030103_" nick-name="汀乔" suda-data="key=tblog_search_weibo&amp;value=seqid:
                #if (j.attrs['nick-name'] != '伊草恋' or j.attrs['nick-name'] != '庹宛白酮'):
                ID.append(i.attrs['href'])
                name.append(i.attrs['nick-name'])
            except:
                print("第一次解析失败")

        for j in soup.findAll(name='p', attrs={'class': 'txt', 'node-type': 'feed_list_content'}):
            # print("解析评论内容")
            try:
                print(j)
                print("评论"+j.get_text())
                # if (j.attrs['nick-name']!='伊草恋' or j.attrs['nick-name']!='庹宛白酮'):
                commentList.append(j.get_text())
            except:
                print("第二次解析失败")
    '''




def printComment(ID,commentList,name):
    # -------------检测解析是否正确--------------------
    print("评论"+str(len(commentList)))
    print("ID" + str(len(ID)))
    print("name" + str(len(name)))
    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('#开年第一剁')
    for i in range(len(ID)):
        worksheet.write(i, 0, name[i], style)  # Outputs 5
        worksheet.write(i, 1, ID[i], style)  # Outputs 2
        worksheet.write(i, 2, commentList[i], style)
    workbook.save('话题人群信息Raw.xls')


def main():
    commentList = []
    ID = []
    name = []
    start_url = "https://s.weibo.com/weibo?q=%23%E5%BC%80%E5%B9%B4%E7%AC%AC%E4%B8%80%E5%89%81%20%E5%8F%A3%E7%BA%A2%E5%A7%A8%E5%A6%88%E5%B7%BE%23&nodup=1"
    for i in range(1,16):
        try:
            url = start_url + '&page={}'.format(str(i))
            print(url)
            html = getHTMLText(url)
            parsePage(ID,commentList,name,html)
            print("name:"+str(name)+" ID:"+ID+" comment:"+commentList)
            #parsePage(commentList, html)
        except:
            continue
    printComment(ID,commentList,name)

main()