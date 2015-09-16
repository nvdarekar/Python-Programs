#!/usr/bin/python2.7

import itertools

def giveJuiceCombinations():
	fin = open('sampleinput.txt', 'r');
	#Make output file empty if it already exists
	fout =  open('sampleoutput.txt', 'w');    
	fout.close();
	fout =  open('sampleoutput.txt', 'a');
	lines = fin.readlines()

	#parsing input file to get required data into variables
	lineCount = 0
	while not lines[lineCount].strip():   
		lineCount += 1	
	noOfFriends = int(lines[lineCount].strip())
	lineCount += 1	
	#finding bottle combinations for each friend
	for i in range(noOfFriends):
		#skip blank lines in input file if any	
		while not lines[lineCount].strip():   
			lineCount += 1			
		noOfJuice = lines[lineCount].strip().split()[0]
		calorieContentsOfBottles =  [int(j) for j in lines[lineCount].strip().split()[1:]]
		lineCount += 1
		#skip blank lines in input file	if any	
		while not lines[lineCount].strip():  
			lineCount += 1			
		juiceBottlesInCupboard = list(lines[lineCount].strip())
		lineCount += 1	
	
		#Creating list of lists containing juice info 
		#[bottle name, its calorie content, the number of bottles of that juice in cupboard] 
		juiceInfo = []    		
		k = 0			
		for bottle in sorted(set(juiceBottlesInCupboard)):
			juiceInfo.append([bottle, calorieContentsOfBottles[k], juiceBottlesInCupboard.count(bottle)])
			k += 1
		juiceInfo = sorted(juiceInfo) 
		
		#skip blank lines in input file if any	
		while not lines[lineCount].strip():  
			lineCount += 1	
	
		calorieIntakeOfFriend = int(lines[lineCount].strip())
		lineCount += 1
		
		#Calorie Contents of bottles in cupboard Sorted according to bottle name		
		caloriesOfBottlesInCupboard = []      
		for juice in juiceInfo:
			for k in range(juice[2]):
				caloriesOfBottlesInCupboard.append(juice[1])

		#finding required combination	
		requiredcalorieCombination = findCombination(caloriesOfBottlesInCupboard, calorieIntakeOfFriend)
	
		#Writing required Combinations to output file	
		if len(requiredcalorieCombination) == 0: 	
			fout.write("friend " + str(i + 1) + ": Sorry, Have Water\n")
		else:
			fout.write("friend " + str(i + 1) + ": ");
			for k in range(len(requiredcalorieCombination)):
				for juice in juiceInfo:
					if juice[1] == requiredcalorieCombination[k] and juice[2] > 0:   
						fout.write(juice[0])
						juice[2] -= 1   	#Bottle used so decrement its count in juiceInfo
			fout.write("\n")
	fin.close()
	fout.close()

def findCombination(caloriesOfBottlesInCupboard, calorieIntakeOfFriend):
	requiredCalorieCombination = []
	for i in range(len(caloriesOfBottlesInCupboard)):
		for combination in itertools.combinations(caloriesOfBottlesInCupboard, i + 1):
			if sum(combination) == calorieIntakeOfFriend:	#required combination found
				requiredCalorieCombination = combination
				break;
	return requiredCalorieCombination

def main():
	giveJuiceCombinations()

if __name__ == '__main__':
	main();
