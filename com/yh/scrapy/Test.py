import requests
#使用python爬去图片
pic = requests.get('http://pics.sc.chinaz.com/files/pic/pic9/201801/zzpic9947.jpg')
# pic = requests.get('https://github.com/lonelyCoder-jrbing/pythonDemo')
with open('picfile.jpg', 'wb') as f:
    f.write(pic.content)
