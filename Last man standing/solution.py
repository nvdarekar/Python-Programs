#!/usr/bin/python2.7

def findAlive():
	persons =  range(1, 1001)
	startIndex = 1 
	while len(persons) > 1:
		lastPerson =  persons[-1]
		for person in persons[startIndex::2]:
			persons.remove(person)
		if person == lastPerson:
			startIndex = 1 	#last person is shooted, so in next iteration delete even position persons 
		else:
			startIndex = 0  #second last person is shooted, so in next iteration delete odd position persons 
	return persons[0]

def main():
	print findAlive()

if __name__ == '__main__':
	main();
