# 求2+4+6+8……+100 的和
#range(start, stop[, step])
sum = 0
for num in range(0,102,2):
	sum += num
print(sum)