#!/usr/bin/python
# -*- coding: UTF-8 -*-
# KagurazakaYashi
import sys
import urllib
import urllib2
class Nikkiup2u3word:
    argv =  [] #可以在init前配置此属性以接入使用
    argumentdict = {}
    datasource = ""
    output = ""
    separate = ""
    
    def __init__(self):
        self.argv = sys.argv
        self.argumentdict = {}
        self.systemencoding = sys.getfilesystemencoding()
        #self.datasource = "http://127.0.0.1/nikkiup2u3_data/wardrobe.js"
        self.datasource = "http://seal100x.github.io/nikkiup2u3_data/wardrobe.js"
        self.output = "up2u3word.txt"
        self.separate = "\r\n"
    
    #显示关于信息
    def about(self):
        print "\n奇迹暖暖词库合成脚本 v1.0 for py2\n如需帮助，请加入 -h 参数。\n神楽坂雅詩\n" #,self.argv[0]
    def help(self):
        self.about()
        print "参数说明："
        print "python nikkiup2u3word.py <--help> <--source (url)> <--output (file)> <--separate (string)>"
        print "不加任何参数：全部参数按照默认值进行提取。"
        print "--help 或 -h 或 /? ：显示此帮助文本。"
        print "--source 或 -s 或 /s <网址> ：指定数据源。\n　　默认值："+self.datasource
        print "--output 或 -o 或 /o <文件路径> ：指定输出到文件。\n　　默认值："+self.output
        print "--separate 或 -e 或 /e <分隔符>：修改分隔符。\n　　默认值：Windows换行符（\\r\\n）"

    #程序起点
    def start(self):
        if self.argumentparsing() == False:
            print "\n"
            exit(0)
        self.about()
        print "数据源："+self.datasource
        print "文件路径："+self.output
        print "分隔符："+self.separate
        print "开始下载..."
        data = self.download()
        print "下载完成，正在解析..."
        data = self.analysis(data)
        data = self.compose(data)
        print "解析完成，写入文件..."
        self.save(data)
        print "完成。"

    #写入
    def save(self,data):
        file(self.output, 'wb+').write(data)

    #合成
    def compose(self,data):
        str1 = data[3]
        ii = 0
        for i in range(4, len(data)):
            nstr = data[i]
            if nstr != "":
                str1 = str1+self.separate+data[i]
                ii=ii+1
        print "数量："+str(ii)
        return str1

    #网络操作
    def download(self):
        req = urllib2.Request(self.datasource)
        res_data = urllib2.urlopen(req)
        return res_data.read()

    #解析
    def analysis(self,data):
        larr = data.split(';')
        larr = larr[0].split('\n')
        names = {}
        for i in range(0, len(larr)):
            nstr = larr[i][3:-3]
            darr = nstr.split(",")
            name = darr[0][1:-1]
            names[i] = name
        return names
            #完全解析
            # for j in range(0, len(darr)):
            #     pr = darr[j][1:-1]
            #     print pr

    #处理参数
    def argumentparsing(self):
        argvlen = len(self.argv)
        if (argvlen == 1):
            return True
        nk = "" #当前得到的参数Key
        nv = "" #当前得到的参数value
        if argvlen > 1:
            for i in range(1, len(self.argv)):
                nowp = self.argv[i] #当前参数
                if nk == "": #应输入nk
                    if self.argumentiskey(nowp) == False:
                        return False
                    nk = nowp
                else: #应输入nv
                    if self.argumentiskey(nowp) == True: #这是下一个nk
                        self.argumentdict[nk] = nv
                        nk = nowp
                        nv = ""
                    else:
                        nv = nowp
                    #print "nk =",nk,"nv =",nv
                    self.argumentdict[nk] = nv
                    nk = ""
                    nv = ""
        if nk != "":
            self.argumentdict[nk] = nv
        return self.argumentkv()
    #判断是否为key
    def argumentiskey(self,key):
        onechar = key[0]
        if onechar == "-" or onechar == "/":
            return True
        return False
    #处理nknv
    def argumentkv(self):
        keys = self.argumentdict.keys()
        for ni in range(0, len(keys)):
            nk = keys[ni]
            nv = self.argumentdict[nk]
            if nk == "--help" or nk == "-h" or nk == "/?":
                self.help()
                return False
            elif nk == "--source" or nk == "-s" or nk == "/s":
                self.datasource = nv
            elif nk == "--output" or nk == "-o" or nk == "/o":
                self.output = nv
            elif nk == "--separate" or nk == "-e" or nk == "/e":
                self.separate = nv

#程序执行
pobj = Nikkiup2u3word()
pobj.start()
exit()