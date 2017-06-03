import urllib.request
import requests
import os
urlForwd = input('请输入搜索网站日期以前的信息（复制进来即可）：')
urlAft = input('请输入搜索网站日期以后的信息：')
yearlow = int(input('请输入搜索起始年份：'))
yearup = int(input('请输入搜索结束年份：'))
test = 1
while test:
    ifDown = input('如果搜索到文件，是否下载到本地？Y/N：')
    if ifDown == 'Y' or ifDown == 'y':
        address1 = input('请问你要创建在那个盘？：') + ':/'
        address = address1 + input('请输入你要创建文件夹名称：')
        if not os.path.exists(address):
            os.mkdir(address)
        test = 0
    elif ifDown == 'N' or ifDown == 'n':
        test = 0
    else:
        print('输入不正确，请重新输入')
        test = 1

availableData = [] #可用的日期集合
for m in range(yearlow,yearup+1):        #年循环
    for j in range(1,13):                #月循环
        for i in range(1,32):            #日循环
            date = str(m).zfill(2)+str(j).zfill(2)+str(i).zfill(2)
            url = urlForwd+date+urlAft
            try:
                urllib.request.urlopen(url)
                availableData.append(url)
                if ifDown == 'Y' or ifDown == 'y':
                    r = requests.get(url)
                    with open(address+'/'+date+'Report'+'.pdf','wb') as f:
                        f.write(r.content)
                        print(date+'这个日期的文件已成功下载')
            except urllib.error.HTTPError:
                print(date+'这个日期没有内容')
            except urllib.error.URLError:
                print('这个网页有问题')
print(availableData)

