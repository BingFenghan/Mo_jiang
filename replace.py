# Python3 by Bing_Yanchi
# 墨江定制程序——替换篇

# 导入库
import os

# 询问部分
file_dir = input("文件夹路径：\n> ")
key = input("改的键为：\n> ")
value = input("设定的值为：\n> ")

# 创建新文件夹
os.mkdir(file_dir +"_replace")

# 获取文件目录
L = []
for root, dirs, files in os.walk(file_dir):
	for file in files:
		if os.path.splitext(file)[1] == '.json':
			L.append(os.path.join(root, file))

# 替换文本
for i in range(len(L)):
	infile = open(L[i], "r",encoding='utf-8')
	outfile = open(file_dir + "_replace/" + os.path.split(L[i])[1], "w",encoding='utf-8')
	# 逐行处理
	for line in infile:
		lines = line.strip()
		space = line.split('"'+ key +'":')[0]
		# 当键存在
		if lines.startswith('"'+ key +'":') == True:
			if lines.endswith('",') == True:
				line = space + '"name": "' + value + '",' +'\r'
		# 写出行
		outfile.write(line)
# 保存
infile.close()
outfile.close()

# 完成
print("Done. 我完成了")
input("> ")