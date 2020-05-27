password = 'a123456'
count = 3
while count > 0:
	count = count - 1
	get_password = input('請輸入密碼：')
	if get_password == password:
		print('登入成功！')
		break
	else:
		print('密碼錯誤！')
		if count > 0:
			print('你還有', count, '次機會！')
		else:
			print('你沒機會了！')