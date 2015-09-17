
#Find farthest employee from CEO
#Input : file containg record as (employee name, salary, manager)
#manager of CEO is specified as a NOBODY

def findFarthest():
	f = open("data.txt", "r")
	#creating dictionary {employeee:manager}  from file
	empManagerDict = dict()
	for line in f:
		record = line.rstrip().split(",")
		empManagerDict[record[0].strip()] = record[2].strip()

	#finding number of managers of each employee and updating farthest to the employee who has max managers	
	count = 0
	prevCount = 0
	for emp in empManagerDict.keys():
		count = countOfManagers(empManagerDict, emp, 0)
		if count > prevCount:
			farthest = emp
			prevCount = count 
	return farthest

def countOfManagers(empManagerDict, emp, count):
	if empManagerDict[emp] == "NOBODY":
		return count
	count += 1
	return countOfManagers(empManagerDict, empManagerDict[emp], count)

if __name__ == "__main__":
	print findFarthest();
