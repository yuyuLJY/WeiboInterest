# encoding: utf-8
import requests
import re
from bs4 import BeautifulSoup
import time
import xlwt

def getHTMLText(url):
    # 第一页的
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; x5sec=7b22726174656d616e616765723b32223a223438353466373065653537663539346532333637303933326235656634653937434a75477a2b4d46454e6d43362b2f2b7363793065526f4d4d6a597a4d7a51774d5467304e6a7378227d; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; whl=-1%260%260%260; l=bBOZfxjIviwswLWfBOfgIQhjnmbtnIOb8NVP2FyFKICPOY5y5HUdWZac5_82C3GVZ6ikR3RYGVWzBrTFcyhV.; isg=BHl5BU5bARsNIdnsn3KGwYwhiOX_kjdk6vuISZuv86A_Ipu049fzCKC0pGZxtAVw'
    # 第二页的
    print("函数"+url)
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; whl=-1%260%260%260; x5sec=7b22726174656d616e616765723b32223a226234313136323630316336656330663034663235306532613837356333316565434e65617a2b4d46454c50566b66486b6a4f6e3155426f4d4d6a597a4d7a51774d5467304e6a7378227d; l=bBOZfxjIviwswoijBOfiCQhjnmbt2QAfGNVP2FyFKICPO7BB5HUdWZac8Kx6C3GVa6d6R3RYGVWzBVTityUCh; isg=BFNTkOBVCwlcksO-YYx8M5pH4tfRHL2WHB0yewVymHLVhHYmjdsxGlgSvrRPFj_C'
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; whl=-1%260%260%260; x5sec=7b22726174656d616e616765723b32223a226234313136323630316336656330663034663235306532613837356333316565434e65617a2b4d46454c50566b66486b6a4f6e3155426f4d4d6a597a4d7a51774d5467304e6a7378227d; l=bBOZfxjIviwswkkwBOfiCQhjnmbtzQdfhNVP2FyFKICPOvWe5HUdWZacDttwC3GVa6IvR3RYGVWzBS8gCy4Fh; isg=BIeH88zRl212jBeC3YhwVy4LFjv9mAEyCOHGZ1l3e5QiyKuKYV_Wv_pOasgzJzPm'
    #cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; t=da32d1956bf7359521d4125151e0d4b0; _tb_token_=53811b8a331e1; cookie2=5a5546894533f119e57b81b85300098b; dnk=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; x=__ll%3D-1%26_ato%3D0; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bOTNBpU1g%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzYFlrtS4bkp38%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; uss=""; csg=85d576da; skt=ba4e9478f6ad60a3; x5sec=7b22726174656d616e616765723b32223a226234313136323630316336656330663034663235306532613837356333316565434e65617a2b4d46454c50566b66486b6a4f6e3155426f4d4d6a597a4d7a51774d5467304e6a7378227d; whl=-1%260%260%260; l=bBOZfxjIviwsw29NBOfgRQhjnmb9aIRb81PP2FyFKICP9O5k5Su5WZacqQTDC3GVa6pvJ3RYGVWzBy8UZy4Fh; isg=BFNTiKmJCwlFhMO-YYx8M5pH4tfRHL2WHB0yewVwfXKKhHEmjNn2G5ASv7RPIz_C'
    #cookie = "cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; x=__ll%3D-1%26_ato%3D0; uss=""; t=da32d1956bf7359521d4125151e0d4b0; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _tb_token_=e17dee3f35737; cookie2=187b945d0bd08bb144ac641bfe02848e; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=UIHiLt3xTIkz&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bDckIz0kA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzX1b6pki1eb%2Bg%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=V32FPkk%2Fw0dUvg%3D%3D; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; csg=460e2314; skt=16b3d5180e653663; enc=QJpjaAbnsy%2Bla2eqbqjuOsFiRYan10imHPBCYmXHAWfTFHP4TcXOY73dah5DvF8L5%2BjaDMzl6LFsmgeQEu%2FytA%3D%3D; whl=-1%260%260%260; l=bBOZfxjIviwsw7IABOfwVQhXlk7TEIOfhCVP2FkwMICP_X525955WZakg1YyC3hVa6L9i3RYGVWzB4Ta5y4el; isg=BDg4Q7r9kOwb8_gPtrXX8tWOCeZmtYooQ4RpKnKoznLejd53JLKmulHrRMWY8VQD"
    #referer = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.6.71be5733oSKzQY&id=584936123552&cm_id=140105335569ed55e27b&abbucket=9'
    cookie = 'cna=K4KXEJ5DXFcCAXWIBwbeQZ6l; lid=%E6%B5%81%E5%B9%B4%E4%BC%BC%E9%94%A61800; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; OZ_1U_2061=vid=vabb5080c69980.0&ctime=1532522894&ltime=1532522523; hng=CN%7Czh-CN%7CCNY%7C156; x=__ll%3D-1%26_ato%3D0; uss=""; t=da32d1956bf7359521d4125151e0d4b0; tracknick=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; lgc=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; _tb_token_=e17dee3f35737; cookie2=187b945d0bd08bb144ac641bfe02848e; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=UIHiLt3xTIkz&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bDckIz0kA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzX1b6pki1eb%2Bg%3D&id2=UU6if2Pgh%2Fr0AA%3D%3D&nk2=ogVXy8kmSs2njvV6&lg2=V32FPkk%2Fw0dUvg%3D%3D; _l_g_=Ug%3D%3D; ck1=""; unb=2633401846; cookie1=BxvDGm0wP4wQxbvy7AWrmQRsbnl4W4kvcqea0mUq7%2Bs%3D; login=true; cookie17=UU6if2Pgh%2Fr0AA%3D%3D; _nk_=%5Cu6D41%5Cu5E74%5Cu4F3C%5Cu95261800; csg=460e2314; skt=16b3d5180e653663; enc=QJpjaAbnsy%2Bla2eqbqjuOsFiRYan10imHPBCYmXHAWfTFHP4TcXOY73dah5DvF8L5%2BjaDMzl6LFsmgeQEu%2FytA%3D%3D; x5sec=7b22726174656d616e616765723b32223a226339313735333638383938326639383038353761393538333537633863313937434e507933754d46454f6548783832546d38534330414561444449324d7a4d304d4445344e4459374d513d3d227d; whl=-1%260%260%260; l=bBOZfxjIviwswJXjBOCNqQhXlk7tLIRjMuSJcA-Mi_5B9_Y6-sQOlzAeoEv62j5P9fYp4IFj7TyToFMzJyTf.; isg=BNnZ-7qM4T-edLnM_xImoexB6MUfctsbCtvoKfuOA4BaAvuUQrTR6LdUBYbR6mVQ'
    referer = 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.67c23167BT9R9F&id=523055748201&areaId=230100&standard=1&user_id=2091012777&cat_id=2&is_b=1&rn=ddcc61bacdecaccbf27ac7dbd3176fd8'
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Cookie': cookie, 'Referer': referer}, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        return "---------------无法连接---------------"

def parsePage(ilt, html):
    try:
        commentAll = re.findall(r'\"rateContent\"\:\".*?\"',html)
        for i in range(len(commentAll)):
            print(i)
            passenge = commentAll[i].split(':')[1]
            passengeRemove = re.sub('"','',passenge)
            print(passengeRemove)
            ilt.append(passengeRemove)
    except:
        print("失败")

def printComment(ilt):
    # -------------检测解析是否正确--------------------
    '''
    for i in range(len(ilt)):
        print(str(i)+"   "+ilt[i])
    '''

    style = xlwt.XFStyle()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('My Sheet')
    for i in range(len(ilt)):
        worksheet.write(i, 0, ilt[i], style)  # Outputs 5
    workbook.save('苏菲淘宝评价1.xls')

def main():
    commentList = []
    # start_url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=584936123552&spuId=1137528922&sellerId=217101303&order=3' #掌心包的
    # https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.67c23167BT9R9F&id=523055748201&areaId=230100&standard=1&user_id=2091012777&cat_id=2&is_b=1&rn=ddcc61bacdecaccbf27ac7dbd3176fd8
    start_url = "https://rate.tmall.com/list_detail_rate.htm?itemId=523055748201&spuId=272420083&sellerId=2091012777&order=3"
    for i in range(1, 102):
        try:
            url = start_url + '&currentPage={}'.format(str(i))
            print(url)
            html = getHTMLText(url)
            print(html)
            parsePage(commentList, html)
        except:
            continue
    printComment(commentList)

main()