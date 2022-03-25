

msg ='[ 抖音分享链接批量提取文案工具 ]'
print(msg + '\n')

with open('test.txt','r',encoding='utf8') as file:
    lines = file.readlines()
    txt = []
    for line in lines:
        # 去除空行
        if line == '\n':
            continue
        # 开始逐行处理
        # 去除多余部分
        start = line.find(':/')
        end = line.find('https://v.douyin.com')

        # 判断是否需要去除多余部分处理
        if start == -1:
            line = line.strip()
        else:
            line = line[start+2:end].strip()

        txt.append(line)

    print('共计处理 '+ str(len(txt)) + ' 条内容')

    with open('file_ok.txt','w',encoding='utf8') as file:
        for i in txt:
            file.write(i + '\n\n')

