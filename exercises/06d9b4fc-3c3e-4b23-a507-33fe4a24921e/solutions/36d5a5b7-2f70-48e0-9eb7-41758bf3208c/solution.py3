if n > 1 and n <= 1000:
	arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	print(sum(arr))
else:
	print ("Wrong input")