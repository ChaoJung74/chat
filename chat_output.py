#先讀取並寫成data清單，去掉換行
def read_file(filename):
	content = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: #sig是把txt存入時開頭的編碼去掉
		for line in f:
			content.append(line.strip())
	return content
#開始轉換格式
def convert(content):
	new = []
	person = None #此處把person宣告是'不存在的'，這是怕第一行不是人名，程式會當掉
	for line in content:
		if line == 'Allen':
			person = 'Allen' #把Allen指定成person，以便後面存成新的字串
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		new.append(person + '：' + line + '\n')
	return new

#把檔案存出成output.txt
def write_file(filename, content):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for e in content:
			f.write(e)
#建立main function來執行
def main(filename): 
	contents = read_file(filename)
	output_file = convert(contents)
	write_file('output.txt', output_file)
#開始執行
main('input.txt')

	 