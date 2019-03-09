# encoding: utf-8
import requests
import re
from bs4 import BeautifulSoup
import time
import bs4
import xlwt
import xlrd

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

def readFromExcel(id_list, follow_list):
    '''
    从关注者文件夹读取文件，逐项添加到follow_list中
    :param follow_list:
    :return:返回没有重复的名人名称和他们的intro
    '''
    name_list = []
    for i in range(len(id_list)):
        exfile = xlrd.open_workbook("C:/Users/yuyu/Desktop/宝洁challenge/复赛/数据/数据集1_用户关注者信息/"+id_list[i]+".xls")
        sheet1 = exfile.sheet_by_name('#')  # 读取Sheet1的内容，根据实际情况填写表名

        n = sheet1.nrows  # 表的总行数
        for i in range(1, n):
            fan = sheet1.row(i)[4].value
            print("fan:"+fan)
            #名人的粉丝数要大于20000
            if int(fan) > 2000000:
                name = sheet1.row(i)[1].value  # 昵称
                intro = sheet1.row(i)[2].value #简介
                #如果没有存在就添加进去
                print("name:"+name+" intro:"+intro)
                if name not in name_list:
                    follow_list.append({'name':name,'intro':intro})

def PrintToShow(follow_list):
    print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")
    for i in range(len(follow_list)):
        #print(follow_list[i]['name']+"  "+follow_list[i]['intro'])
        name = follow_list[i]['name']
        name = re.sub('[0-9]', '', name)
        print(name)
    print(str(len(follow_list)))

def main():
    follow_list = [] #记录每个名人的昵称和简介
    id_list = []
    id_list = ['1699069543']
    getAvalidID(id_list)
    readFromExcel(id_list, follow_list)
    PrintToShow(follow_list)
main()
