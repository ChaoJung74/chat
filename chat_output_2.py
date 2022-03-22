#先讀取並寫成data清單，去掉換行
def read_file(filename):
	content = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: #sig是把txt存入時開頭的編碼去掉
		for line in f:
			content.append(line.strip())
	return content

#開始轉換格式
def convert(content):
	allen_word_count = 0
	allen_picture_count = 0
	allen_sticker_count = 0
	viki_word_count = 0
	viki_picture_count = 0
	viki_sticker_count = 0
	for line in content:
		s = line.split(' ')
		name = s[1]
		
		if s[1] == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_picture_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif s[1] == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_picture_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen傳了', allen_word_count, '個字，', allen_sticker_count, '張貼圖，', allen_picture_count, '張圖片')
	print('Viki傳了', viki_word_count, '個字，', viki_sticker_count, '張貼圖，', viki_picture_count, '張圖片')


#建立main function來執行
def main(filename): 
	contents = read_file(filename)
	convert(contents)
	
main('LINE-Viki.txt')
