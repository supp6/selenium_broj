# coding=utf-8
import requests
import time
'''一下实现博客园 采用cookies 绕过登录步骤，直接写博客随笔'''

s=requests.session()
# 未登录系统直接打开编写随笔界面，系统会自动返回登录界面：
url='https://i.cnblogs.com/EditPosts.aspx?opt=1'
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0"
        }
r1=s.get(url,headers=header)
print(r1.text)
print('添加cookies前-----------------')
print(r1.cookies)

t=time.strftime('%Y_%m_%d %H:%M:%S')
title="我的随笔新增 "+t
text='添加随笔内容 '+ t
url2='https://i.cnblogs.com/EditPosts.aspx?opt=1'
body={"__VIEWSTATE": "",
      "__VIEWSTATEGENERATOR": "FE27D343",
      "Editor$Edit$txbTitle": title,
      "Editor$Edit$EditorBody": text,
      "Editor$Edit$Advanced$ckbPublished": "on",
      "Editor$Edit$Advanced$chkDisplayHomePage": "on",
      "Editor$Edit$Advanced$chkComments": "on",
      "Editor$Edit$Advanced$chkMainSyndication": "on",
      "Editor$Edit$Advanced$txbEntryName": "",
      "Editor$Edit$Advanced$txbExcerpt": "",
      "Editor$Edit$Advanced$tbEnryPassword": "",
      "Editor$Edit$lkbDraft": "存为草稿",

}

#添加登录后的cookies，登录后的cookies可以通过抓包去获取
c = requests.cookies.RequestsCookieJar()
c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8FHXRRtkJWRFtU30nh_M9mCP3Nnu51dGyhNA0NC1zBbSbAAtCbjLseQgijdRUZ4Yay2406gcj_ZVOvmQe2iiS33QtSL-b_whCeBrDsC6cOumO8G8GssO1I2j0rxIZVlCcmc-0RzbHGB_Z3tYo1dioB-tOJ0RMBhlRzo1xYr2lc-ypA0NYgIEl1P0pMJ3EThx2qW-IEhUVcCZ2nJpnos2ohIpTRc7ptQ_3eFjAnmTfQSE6ibQnxVx0wC3jvmPhgg0mexRWhctjOnktUgnCCSuxJeYz1jL3syNorqKUU0uwCAk")
c.set(".CNBlogsCookie","1E9DBE16C18FDDE691E3ECAB585CE1E55129A97FBD7BDB27515B2D61DCB971C2A6126BB17A5726EA3EE50B9DE875ED4C894A8F034501B8AFCE15FBCDD18ED3C860E0228FE3E9C636C5B44A9CED39322CCD87C4D9")
s.cookies.update(c)      #更新cookies
print('更新后的cookies-----------')
print(s.cookies)

#添加登录cookies后，进行添加博客随笔：
r2=s.post(url2,data=body,verify=False)