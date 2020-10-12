
# String {L = a ^ n b ^ m n + m = even}
 
# dfa = state (zeroth) of DFA 
def start(c): 
	if (c == 'a'): 
		dfa = 1
	elif (c == 'b'): 
		dfa = 2
	
	# -1 is used to check for any 
	else: 
		dfa = -1
	return dfa 

# This function is for the first 
def state1(c): 
	if (c == 'a'): 
		dfa = 0
	elif (c == 'b'): 
		dfa = 5
	else: 
		dfa = -1
	return dfa 

# This function is for the second 
def state2(c): 
	if (c == 'b'): 
		dfa = 3
	else: 
		dfa = -1
	return dfa 

# This function is for the third 
def state3(c): 
	if (c == 'b'): 
		dfa = 4
	else: 
		dfa = -1
	return dfa 

# This function is for the fourth 
def state4(c): 
	if (c == 'b'): 
		dfa = 3
	else: 
		dfa = -1
	return dfa 

# This function is for the fifth 
def state5(c): 
	if (c == 'b'): 
		dfa = 6
	else: 
		dfa = -1
	return dfa 


# This function is for the sixth 
def state6(c): 
	if (c == 'b'): 
		dfa = 5
	else: 
		dfa = -1
	return dfa 

def isAccepted(String): 
	
	l = len(String) 
	
	# with the present dfa = state 
	dfa = 0
	for i in range(l): 
		if (dfa == 0): 
			dfa = start(String[i]) 

		elif (dfa == 1): 
			dfa = state1(String[i]) 

		elif (dfa == 2) : 
			dfa = state2(String[i]) 

		elif (dfa == 3) : 
			dfa = state3(String[i]) 

		elif (dfa == 4) : 
			dfa = state4(String[i]) 

		elif (dfa == 5) : 
			dfa = state5(String[i]) 

		elif (dfa == 6): 
			dfa = state6(String[i]) 

		else: 
			return 0
	if(dfa == 3 or dfa == 5) : 
		return 1
	else: 
		return 0

# Driver code 
if __name__ == "__main__" : 
	String = "aaabbb"
	if (isAccepted(String)) : 
		print("ACCEPTED") 
	else: 
		print("NOT ACCEPTED") 


