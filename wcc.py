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

def art():
	for name in areaOfClass.keys():
		if '，艺美' in areaOfClass[name]:
			areaOfClass[name]=areaOfClass[name].replace("，艺美"," (艺美)")
			# print(areaOfClass[name])
			if '艺美' not in classOfArea.keys():
				classOfArea.update({'艺美': [name]})
			else:
				classOfArea['艺美'].append(name)

def read_op():
	while True:
		op = input("[INFO] 请选择操作(1.搜索课程类别 2.搜索类别下课程 3.搜索您的所有课程类别 4.退出)\n>>> ")
		opInt = 0
		try:
			opInt = int(op)
			if opInt < 1 or opInt > 4:
				raise '[ERROR] 请输入1|2|3|4！'
		except:
			raise '[ERROR] 请输入正确的数字!'
		if opInt == 1:
			while True:
				className = input("[INFO] 请输入课程名，若想退出此环节请输入#:\n>>> ")
				if className=='#':
					break
				elif className in areaOfClass.keys():
					print(f'======================================= {className}: {areaOfClass[className]}')
				else:
					print(f'[ERROR] {className}并非通选课.')
		elif opInt == 2:
			while True:
				areaID = input("[INFO] 请输入领域名称(A|B|C|D|E|F|艺美)，若想退出此环节请输入#:\n>>> ")
				if areaID == '#':
					break
				elif areaID in ("a", "b", "c", "d", "e", "f"):
					areaID = areaID.upper()
				elif areaID in ("美","艺"):
					areaID = '艺美'
				if areaID in ("A", "B", "C", "D", "E", "F", "艺美"):
					print(f"==================以下为分类{areaID}的所有课程==================")
					for className in classOfArea[areaID]:
						print(className)
					print(f"=====================共计{len(classOfArea[areaID])} 门{areaID}类课程=====================")
				else:
					print('[ERROR] 请输入正确的类别!')
		elif opInt == 3:
			with open('classes.csv', 'r', encoding='gbk') as f:
				for className in f.read().splitlines():
					if className in areaOfClass.keys():
						print(f'======================================= {className}: {areaOfClass[className]}')
					else:
						print(f'[ERROR] {className}并非通选课.')
		else:
			break

if __name__ == '__main__':
	init()
	art()
	read_op()