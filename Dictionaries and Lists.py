# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

def get_path(file_name):
    """
        Returns a string with the absolute path of a given file_name located in the same directory as this script

        # Do not modify this function in any way

        >>> get_path('words.txt')   # HW1.py and words.txt located in HW1 folder
        'G:\My Drive\CMPSC132\HW1\words.txt'
    """
    import os
    target_path = os.path.join(os.path.dirname(__file__), file_name)
    return target_path
''''
Given a rectangle, the code searches for the maximum intger side lengths which are dependent on the perimeter and area. 
The code returns the largest possible width or height of the rectangle to produce the perimeter or area. 
'''
def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    P = perimeter 
    A = area
    widths_lst = []

    for width in range(1, perimeter): # Loops through possible widths starting from 1 because perimeter cannot be 0
        h = (P-2*width)/2 # Calculates the corresponding height based on the perimeter formula
        if h ==int(h) and width * int(h) == A:
            widths_lst.append(max(width, int(h)))
                                   
    if widths_lst: # If list is not empty, return the max width/height
        return max(widths_lst)
    else: 
        return False 


        

    pass

'''
This code converts a given octal number into its decimal equivalent. 
In the octal system, each digit represents a power of 8. 
The code extracts each digit from the octal number, multiplies it by the corresponding power of 8, and sums the results to compute the decimal value.
The code returns the decimal representation of the octal number. 
'''
def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    #- YOUR CODE STARTS HERE
    total_sum = 0 
    variable = 0  # Initializes a tracking variable to keep track of the power of 8
    digits = []  # Initializes a list to store the digits of the octal number
    
    while oct_num > 0: 
        digits.append(oct_num % 10)  # Gets the last digit of the octal number and adds it to the list
        oct_num //= 10
    
    for i in digits:
        total_sum += i * 8**variable # Multiplies the digit by 8, which is raised to the current power and adds it to the total sum
        variable += 1  # Increments the power of 8 for the next digit
    
    return total_sum


    pass

'''
This code takes a number as its input and checks to see if the numbers surrounding some number are the same. 
It returns true if there are two identical numbers sandwiching one number.
It returns false if there are not two identical numberd sandwiching one number.
'''

def has_hoagie(num):
    """
        >>> has_hoagie(737) 
        True
        >>> has_hoagie(35) 
        False
        >>> has_hoagie(-6060) 
        True
        >>> has_hoagie(-111) 
        True
        >>> has_hoagie(6945) 
        False
    """
    #- YOUR CODE STARTS HERE
    if num < 0:  # If a number is negative, the absolute value of the numer is taken 
        num = abs(num)
    
    list = []  # Initializess a list to store the digits of the number
    
   
    while num > 0:  # Extracts the digits of the number and stores them in the list
        list.append(num % 10)
        num //= 10
    
   
    for i in range(1, len(list) - 1): # Checks for duplicates to the left and right 
        if list[i-1] == list[i + 1]:
            return True
    
    return False




    pass
'''
Given two numbers, this code is supposed to look through the first number and search for any repeated digits. 
If repeated digits are found in the first number (num_1), and the first number is the equal to second number(num_2) after removing the repeated digits,
The function will return true.
If num_1 does not equal num 2 after removing the repeated digits, the funciton will return false. 
'''

def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765) 
        False
        >>> is_identical(2023, 20) 
        False
    """
    #- YOUR CODE STARTS HERE
    num1=0
    ph=num_1%10 # Stores last digit in num 1
    num2=0
    placeholder=1
    ph2=1
    while num_1>0: # We take number 1, and see if greater than 0
        num_1=num_1//10 # Taking last digit out of num 1
        placeholder=num_1%10 # Stores second to last digit  
        if ph!=placeholder: # Checks to see if 2 digits are the same. If they are not the same they will not be added 
            num1+=ph*ph2  
            ph2*=10
        ph=placeholder # Second to last number is now the last number
        placeholder=num_1%10
    ph=num_2%10
    placeholder=1
    ph2=1
    while num_2>0: # Same process for num 2 as num 1
        num_2=num_2//10
        placeholder=num_2%10
        if ph!=placeholder:
            num2+=ph*ph2
            ph2*=10
        ph=placeholder
        placeholder=num_2%10
    return num1==num2 # Returns numbers if identical 
        


        


'''
This code takes one number as the input and checks to see if it is even or odd. 
If the number is even, then the next number in the sequence will be the number divided by 2.
If the number is odd, then the next number in the sequence will be the 3 times the number plus 1.
The code will do this until the number equals 1 in the sequence. 
'''

def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    list = [num]

    while num > 1: # Initializes a loop until num is 1
        if num % 2 == 0:
            num = num // 2 # If number is even, divide number by 2
        else:
            num = 3 * num + 1 # If number is odd, multiply number by 3 and add 1
    
        list += [num] 
        
    return list # Returns list 
            


'''
This function iterates through a dictionary looking to add key:value pairs to the dictionary.
If the key does not exist, the function will add the key to the dictionary.
If the key already exists, the function will keep a list of the values for that key in the order they were added. 
'''

def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    #- YOUR CODE STARTS HERE
    if key in d: # Checks to see if the key is in the dictionary 
        if isinstance(d[key], list):
            d[key].append(value) # This appends new value to the list 
        else:
            d[key] = [d[key], value]
    else:
        d[key] = value # If the key does not exist in the dictionary, it adds the key with the value
    
    

'''
This function takes a dictionary d that contains employee information.
It returns a new dictionary that is organized by department, like this {department:[{'emp_id': employee_id, 'name': name, 'position': position}, {'emp_id':employee_id, 'name': name, 'position': position}]}.. 
'''
def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    #- YOUR CODE STARTS HERE
    result = {}
    
    for employee_id, employee_info in d.items():
        department = employee_info['department']
        employee_details = {'emp_id': employee_id, 'name': employee_info['name'], 'position': employee_info['position']} # Stores employee id, employee names, and employee position
        
        if department not in result:
            result[department] = []


        result[department].append(employee_details)
    
    return result
    
'''
The function recieves a text file. 
The purpose of it is to find the successors of each word in the text file.
The keys in the new dictionary are words and the successing word is the value.
The function returns these key values pairs. 
'''
def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better
    # --- YOU CODE STARTS HERE
    contents = list(contents)  # Turn contents into list of characters
    while "\n" in contents: # Checks to see if /n is a character in contents
        contents.remove('\n') # If it is, it gets rid of it 

    for i in range(len(contents)): 
        if not(contents[i].isalnum()) and contents[i] != " ": # checks to see if it is a non alphanumerical symbol 
            contents[i]=" "+contents[i]+" " # Puts spaces around it to separate it from other words
            
    contents.insert(0,".") # Inserts period in index 0
    contents.insert(1, " ") # Puts a space after the period to separate it from other words 


    contents = ''.join(contents) # Joins all the words together 
    contents = contents.split(' ') # Separates them by spaces so all words/symbols are items in the list  

    dict = {} # Initialize emply dictionary 

    for i in range(len(contents)-2): # Loops through every words except the last one and blank character at the end 
        if contents[i] not in dict: 
            dict[contents[i]] = []
        if not(contents[i+1] in dict[contents[i]]): # If its not already in the dictionary and it is a successor, we add it 
            dict[contents[i]].append(contents[i+1])

    return dict # Returns dictionary 










'''
This function takes a dictionary which is a trie and a word which is a string. 
The goal is to add the string to the trie by checking to see if the current letter is in the dictionary.
If it is not, it will add it.
If it is, it will move on. 
'''
def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}
       
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    #- YOUR CODE STARTS HERE
    dict = trie
   
    for i in range(len(word)): # Loops through each letter in the word 
        letter = word[i:i+1]  # Extracts the current letter 
        
        if letter not in dict:
            dict[letter] = {} # Creates a new node if the letter is not already in the current dictionary 
        dict = dict[letter]

    dict['word'] = True # Once all the letters of the word have been iterated through, it marks the end of the word by setting a key (word) to true

    pass

'''
This function takes a file_name.
Then it lowercase every character in the file.
Then it will add it to the trie.
Then the final dictionary will be returned. 
'''

def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better 
    #- YOUR CODE STARTS HERE

    new_trie = {} # Initialize an empty trie

    contents = contents.split('\n') # Splitting the contents into words 

    for word in contents: # Going through each word in the contents
        word = word.lower() # Making words lowercase
        addToTrie(new_trie, word) # Adding the word to trie
    return new_trie


'''
This function takes a word and looks to see if it is in the trie.
Returns True if it is in the trie.
Returns False if it is not in the trie. 
'''

def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    #- YOUR CODE STARTS HERE
    for i in word:
        if i in trie:
            trie = trie[i] 
        else: 
            return False
    if 'word' in trie:
        return True 
    else:
        return False
    
    




def run_tests():
    import doctest
    # Run start tests in all docstrings
    # doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    doctest.run_docstring_examples(createDictionaryTrie, globals(), name='HW1',verbose=True)   

if __name__ == "__main__":
    run_tests()