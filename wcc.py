
classOfArea = {}
areaOfClass = {}

def init():
	with open('./data/infoText', 'r', encoding='utf-8') as f:
		data = f.read().splitlines()
		for line in data[1:]:
			cells = line.split()
			areaOfClass.update({cells[2]: cells[5]})
			for area in cells[5].replace("，艺美", "").split('、'):
				if area not in classOfArea.keys():
					classOfArea.update({area: [cells[2]]})
				else:
					classOfArea[area].append(cells[2])
		return
	raise '[ERROR] 请检查同目录下是否存在data/infoText!'

def read_op():
	op = input("[INFO] 请选择操作(1.搜索课程类别 2.搜索类别下课程 3.搜索您的所有课程类别)\n>>> ")
	opInt = 0
	try:
		opInt = int(op)
		if opInt < 1 or opInt > 3:
			raise '[ERROR] 请输入1|2|3！'
	except:
		raise '[ERROR] 请输入正确的数字!'
	if opInt == 1:
		while True:
			className = input("[INFO] 请输入课程名:\n>>> ")
			if className in areaOfClass.keys():
				print(f'======================================= {className}: {areaOfClass[className]}')
			else:
				print(f'{className}并非通选课.')
	elif opInt == 2:
		areaID = input("[INFO] 请输入领域名称(A|B|C|D|E|F):\n>>> ")
		if areaID in ("A", "B", "C", "D", "E", "F"):
			for className in classOfArea[areaID]:
				print(className)
			print(f"[INFO] 以上即为分类{areaID}的所有课程.")
	elif opInt == 3:
		with open('classes.csv', 'r', encoding='gbk') as f:
			for className in f.read().splitlines():
				if className in areaOfClass.keys():
					print(f'======================================= {className}: {areaOfClass[className]}')
				else:
					print(f'{className}并非通选课.')

if __name__ == '__main__':
	init()
	read_op()