# coding:utf-8
from urllib import parse

# a= "中文"
# url = "http://zzk.cnblogs.com/s/blogpost?Keywords=%s"%a
# print(url)
#
# b= parse.quote(a)      # quote是对字符串转码成url科识别的编码
# print(b)
# url1 = "http://zzk.cnblogs.com/s/blogpost?Keywords=%s"%b
# print(url1)

####
import urllib.parse
print(urllib.parse.quote("中文"))      #编码
print(urllib.parse.unquote("%E4%B8%AD%E6%96%87"))       #解码
url2 = "http://zzk.cnblogs.com/s/blogpost?Keywords=%E4%B8%AD%E6%96%87"
print(urllib.parse.unquote(url2))

import requests
url11 = "http://zzk.cnblogs.com/s/blogpost"
par = {"Keywords":"中文"}    # 参数存字典
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ",
      "Cookie": "UM_distinctid=15d6981cb266f-084faa778153e4-c393062-15f900-15d6981cb271ba; _ga=GA1.2.1776787901.1500036947",
          }
res1= requests.get(url=url11, params=par, hearders=header)
print(res1.url)
print(res1.encoding)
print(urllib.parse.unquote(res1.url))