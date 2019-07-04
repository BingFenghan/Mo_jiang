# Python3 by Bing_Yanchi
# 墨江定制程序——删除篇

# 导入库
import os,shutil

# 询问部分
file_dir = input("文件夹路径：\n> ")

# 创建新文件夹
# os.mkdir(file_dir +"_del_name")

# 复制文件夹
destination_file = file_dir + "_del_name"
shutil.copytree(file_dir,destination_file)

# 获取文件目录
L = []
for root, dirs, files in os.walk(destination_file):
	for file in files:
		if os.path.splitext(file)[1] == '.json':
			L.append(os.path.join(root,file))

# 替换文本
'''
for i in range(len(L)):
	infile = open(L[i],"w",encoding='utf-8')
	outfile = open(L[i],"r",encoding='utf-8')
	# 逐行处理
	for line in infile:
		key = '"name"'
		result = key in line
		if result == True:
			line = ""
		# 写出行
		outfile.write(line)
'''

for i in range(len(L)):
	file_data = ""
	with open(L[i],"r",encoding='utf-8') as f:
		key = '"name"'
		for line in f:
			result = key in line
			if result == True:
				line = ""
			file_data += line
	with open(L[i],"w",encoding='utf-8') as f:
		f.write(file_data)

# 保存
f.close()

# 完成
print("Done. 我完成了")
input("> ")