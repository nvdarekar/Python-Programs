#!/usr/bin/python2.7

#Answer to the question 1
def rotate(array, rotateBy):
	i = 0
	while i < rotateBy:
		array.insert(0, array.pop())  #remove last element and insert it at first place
		i += 1	
	return array		

def main():
	array = [1, 2, 3, 4, 5, 6]
	print rotate(array, 2);


if __name__ == '__main__':
	main();


