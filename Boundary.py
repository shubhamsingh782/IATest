def put(position,part,l_part,height,currHeight,output):

	#print("from put:",position,l_part,height,currHeight)

	#print("Received :",output)
	
	while position < l_part:
		x,height = part[position]
		position = position+1

		if currHeight != height:
			currHeight = height

			if not output or output[-1][0] != x:
				output.append([x,height])
			else:
				output[-1][1] = height
	#print("Return :",output)
	


def joinBoundary(part1,part2):

	l_part1 = len(part1)
	l_part2 = len(part2)

	left = right = 0
	currHeight = leftHeight = rightHeight = 0
	output = []

	while left < l_part1  and right < l_part2:
		#print("length :",left,right)
		rect1 = part1[left]
		rect2 = part2[right]

		if rect1[0] < rect2[0]:
			x, leftHeight = rect1
			left = left +1
		else:
			x,rightHeight = rect2
			right = right + 1

		#print("Loop Value :",x,leftHeight,rightHeight,currHeight)
		maxHeight = max(leftHeight,rightHeight)

		if currHeight != maxHeight:
			currHeight = maxHeight

			if not output or output[-1][0] != x:
				output.append([x,maxHeight])
			else:
				output[-1][1] = maxHeight

	#print("data: "+str(left)+" "+str(right)+" "+str(leftHeight)+" "+str(rightHeight)+" "+str(currHeight))
	#print("1st : ")
	#print(output)
	put(left,part1,l_part1,leftHeight,currHeight,output)
	#print("2nd : ")
	#print(output)
	put(right,part2,l_part2,rightHeight,currHeight,output)


	#print("Output: ")
	#print(output)

	return output



def computeBoundary(allRectDims,n):
	if n == 0: 
		return []
	if n == 1:
		x1,x2,y = allRectDims[0]
		return [[x1,y],[x2,0]]

	pivot = n//2

	part1 = computeBoundary(allRectDims[:pivot],pivot)
	part2 = computeBoundary(allRectDims[pivot:],n-pivot)
	
	#print("part1 ",part1)
	#print("part2 ",part2)
	
	return joinBoundary(part1,part2)

		
def main():
	n = int(input())
	allRectDims = []


	for i in range(n):
		dimensions = list(map(int,input().split(" ")))
		allRectDims.append(dimensions)

	outList = computeBoundary(allRectDims,n)

	print(outList)

	

if __name__ == '__main__':
	main()
