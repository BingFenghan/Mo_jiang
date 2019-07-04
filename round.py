# Python3 by Bing_Yanchi
# 墨江定制程序——四舍五入篇

# 导入库
import os,shutil,math

# 询问部分
file_dir = input("文件夹路径：\n> ")

# 复制文件夹
destination_file = file_dir + "_round"
shutil.copytree(file_dir,destination_file)

# 获取文件目录
L = []
for root, dirs, files in os.walk(destination_file):
	for file in files:
		if os.path.splitext(file)[1] == '.json':
			L.append(os.path.join(root,file))

# 替换文本
for i in range(len(L)):
	file_data = ""
	with open(L[i],"r",encoding='utf-8') as f:
		for line in f:
			lines = line.strip()
			space = line.split('"uv": [')[0]
			# 如果仅有 uv
			if lines.startswith('"uv": [') == True:
				content = lines.strip('"uv": [')
				content = content.strip('],')
				uv_value = content.split(', ')
				# 判定为 3 及以上
				if len(uv_value) >= 3:
					new_value = []
					new_line = ""
					for m in range(len(uv_value)):
						decimal_part = math.modf(float(uv_value[m]))[0]
						if (0 < decimal_part < 0.05) == True:
							uv_value[m] = round(float(uv_value[m]))
						if (0.95 < decimal_part < 1) == True:
							uv_value[m] = round(float(uv_value[m]))
						new_line = new_line + str(uv_value[m]) + ', '
					line = new_line.strip(', ')
					line = space + '"uv": [' + line + '],' +'\r'
			# 如果比较复杂
			else:
				key = '"uv"'
				result = key in lines
				if result == True:
					begin = lines.find('[')
					end = lines.find(']')
					content = lines[begin+1:end]
					uv_value = content.split(', ')
					# 判定为 3 及以上
					if len(uv_value) >= 3:
						new_value = []
						new_line = ""
						for m in range(len(uv_value)):
						decimal_part = math.modf(float(uv_value[m]))[0]
						if (0 < decimal_part < 0.05) == True:
							uv_value[m] = round(float(uv_value[m]))
						if (0.95 < decimal_part < 1) == True:
							uv_value[m] = round(float(uv_value[m]))
							new_line = new_line + str(uv_value[m]) + ', '
						line_1 = new_line.strip(', ')
						before = line.split('[')[0]
						rear = line.split(']')[1]
						line = before + '[' + line_1 + ']' + rear
			# 处理 from 部分
				key = '"from"'
				result = key in lines
				if result == True:
					space = line.split('"from": [')[0]
					content = lines.strip('"from": [')
					content = content.strip('],')
					uv_value = content.split(', ')
					new_value = []
					new_line = ""
					for m in range(len(uv_value)):
						decimal_part = math.modf(float(uv_value[m]))[0]
						if (0 < decimal_part < 0.05) == True:
							uv_value[m] = round(float(uv_value[m]))
						if (0.95 < decimal_part < 1) == True:
							uv_value[m] = round(float(uv_value[m]))
						new_line = new_line + str(uv_value[m]) + ', '
					line = new_line.strip(', ')
					line = space + '"from": [' + line + '],' +'\r'
			# 处理 to 部分
				key = '"to"'
				result = key in lines
				if result == True:
					space = line.split('"to": [')[0]
					content = lines.strip('"to": [')
					content = content.strip('],')
					uv_value = content.split(', ')
					new_value = []
					new_line = ""
					for m in range(len(uv_value)):
						decimal_part = math.modf(float(uv_value[m]))[0]
						if (0 < decimal_part < 0.05) == True:
							uv_value[m] = round(float(uv_value[m]))
						if (0.95 < decimal_part < 1) == True:
							uv_value[m] = round(float(uv_value[m]))
						new_line = new_line + str(uv_value[m]) + ', '
					line = new_line.strip(', ')
					line = space + '"to": [' + line + '],' +'\r'
			file_data += line
	with open(L[i],"w",encoding='utf-8') as f:
		f.write(file_data)

# 完成
print("Done. 我完成了")
input("> ")