import datetime

def addRest(x_pos,lst,l_lst,height,currHeight, output):
	while x_pos < l_lst:
		x,height = lst[x_pos]
		x_pos += 1

		if currHeight != height:
			currHeight = height
			if not output or output[-1][0] != x:
				output.append([x,height])
			else:
				output[-1][1] = height


def merge(l1,l2,output):
	l_l1,l_l2 = len(l1),len(l2)
	x_pos_1 = x_pos_2 = 0
	currHeight = leftHeight = rightHeight = 0

	#print("val :",l1,l2,output)

	while x_pos_1 < l_l1 and x_pos_2 < l_l2:
		point1 ,point2 = l1[x_pos_1], l2[x_pos_2]

		if point1[0] < point2[0]:
			x,leftHeight = point1
			x_pos_1 += 1
		else:
			x,rightHeight = point2
			x_pos_2 += 1

		maxHeight = max(leftHeight,  rightHeight)

		if currHeight != maxHeight:
			currHeight = maxHeight
			if not output or output[-1][0] != x:
				output.append([x, maxHeight])
			else:
				output[-1][1] = maxHeight

	#print("First: ",output)

	addRest(x_pos_1,l1,l_l1,leftHeight,currHeight, output)
	#print("second: ",output)

	addRest(x_pos_2,l2,l_l2,rightHeight,currHeight,output)

	#print("Return: ",output)


	return output

def Approach2(allRectDims,n):

	x01,x02,y0 = allRectDims[0][0],allRectDims[0][1],allRectDims[0][2]
	x11,x12,y1 = allRectDims[1][0],allRectDims[1][1],allRectDims[1][2]

	
	l1 = [[x01,y0],[x02,0]]

	#a = datetime.datetime.now()

	for i in range(1,n):
		output = []
		x1,x2,y = allRectDims[i][0],allRectDims[i][1],allRectDims[i][2]
		l2 = [[x1,y],[x2,0]]
		output = merge(l1,l2,output)
		l1 = output

	#b = datetime.datetime.now()
	#print(b-a)

	return output


def main():
	n = int(input())
	allRectDims = []


	for i in range(n):
		dimensions = list(map(int,input().split(" ")))
		allRectDims.append(dimensions)

	outList = Approach2(allRectDims,n)

	print(outList)

	

if __name__ == '__main__':
	main()