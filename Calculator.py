# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
     
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if len(self) <= 0:
            return True
        else:
            return False
        

    def __len__(self): 
        # YOUR CODE STARTS HERE
        currNode=self.top
        num=0
        while (currNode!=None):
            num+=1
            currNode=currNode.next
        return num
       
    '''
    receives value and makes it the new top node
    '''
    def push(self,value):
        # YOUR CODE STARTS HERE
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

     
    '''
    pops out the top value of the Stack
    '''
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():      #no top node when empty
            return None
        else:
            top_value = self.top.value
            self.top = self.top.next 
            return top_value
        
    '''
    returns top node value
    '''
    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        else:
            return self.top.value
        


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    '''
    receives txt and uses try and except to determine if it's a float or not
    '''
    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True
        except ValueError:
            return False 

    '''
    receives an infix expression txt and converts it to postfix, returning the postfix expression
    '''
    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('     2 ^       4')
            '2.0 4.0 ^'
            >>> x._getPostfix('          2 ')
            '2.0'
            >>> x._getPostfix('2.1        * 5        + 3       ^ 2 +         1 +             4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2*5.34+3^2+1+4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( .5 )')
            '0.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('(2 * ( ( 5 + 3) ^ 2 + (1 + 4 )))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('((2 *((5 + 3) ^ 2 + (1 +4 ))))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2* (       -5 + 3 ) ^2+ ( 1 +4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expresions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            #>>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            #>>> x._getPostfix('     2 * 5 + 3  ^ * 2 + 1 + 4')
            #>>> x._getPostfix('2    5')
            #>>> x._getPostfix('25 +')
            #>>> x._getPostfix(' 2 * ( 5      + 3 ) ^ 2 + ( 1 +4 ')
            #>>> x._getPostfix(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            #>>> x._getPostfix('2 *      5% + 3       ^ + -2 +1 +4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()
        txt = ''.join(txt.split())
        done = False
        exp = '^'
        left = -1000
        right = -1000
        count1 = 0
        count2 = 0
        paren = True
        output = []
        for i in range(len(txt)):
            if txt[i] == '(':
                count1 += 1
            elif txt[i] == ')':
                count2 += 1
        if count1 != count2:
            return None
        i = 0
        while i < len(txt):
            if self._isNumber(txt[i]) or txt[i] == '.' or (txt[i] == '-' and (i == 0 or txt[i - 1] in '+-*/^(')):
                num = []
                if txt[i] == '-':
                    num.append('-')
                    i += 1
                while i < len(txt) and (self._isNumber(txt[i]) or txt[i] == '.'):
                    num.append(txt[i])
                    i += 1
                output.append(str(float(''.join(num))))
                i -= 1
            elif txt[i] in '^*/+-':
                while (not postfixStack.isEmpty() and postfixStack.peek() != '(' and
                    ((txt[i] in '*/' and postfixStack.peek() in '^*/') or
                        (txt[i] in '+-' and postfixStack.peek() in '^*/+-'))):
                    output.append(postfixStack.pop())
                postfixStack.push(txt[i])
            elif txt[i] == '(':
                postfixStack.push('(')
            elif txt[i] == ')':
                while not postfixStack.isEmpty() and postfixStack.peek() != '(':
                    output.append(postfixStack.pop())
                if not postfixStack.isEmpty() and postfixStack.peek() == '(':
                    postfixStack.pop()
            i += 1
        while not postfixStack.isEmpty():
            output.append(postfixStack.pop())
        return ' '.join(output)

                    
                
                                
                        

                
    '''
    calculates the expression stored by converting it to postfix and
    calculating it using a stack. the result is returned
    '''
    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4        + 3 -       2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 +          3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('      4 +           3.65  - 2        / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25      * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('2-3*4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7^2^3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ((( 10 - 2*3 )) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('      8 / 4 * (3 - 2.45 * ( 4   - 2 ^ 3 )       ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 +        2 * (         5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 +         3 * (2 + ( 3.0) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            #>>> x.setExpr(" 4 ++ 3+ 2") 
            #>>> x.calculate
            #>>> x.setExpr("4  3 +2")
            #>>> x.calculate
            #>>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            #>>> x.calculate
            #>>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            #>>> x.calculate
            #>>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            #>>> x.calculate
            #>>> x.setExpr('(    3.5 ) ( 15 )') 
            #>>> x.calculate
            #>>> x.setExpr('3 ( 5) - 15 + 85 ( 12)') 
            #>>> x.calculate
            #>>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))") 
            #>>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        expr=self._getPostfix(self.getExpr)
        num=0
        numTot=0
        if expr==None:
            return None
        for i in range(0,len(expr)):
            j=i+numTot
            if not(j>=len(list(expr))):
                if self._isNumber(expr[j]):
                    num=0
                    while  not(j+num>=len(list(expr))) and (self._isNumber(expr[j+num]) or expr[j+num]=='.'):
                        num+=1
                    calcStack.push(float(expr[j:j+num]))
                    numTot+=num
                elif expr[j]=='-' and not(j+1>=len(list(expr))) and self._isNumber(expr[j+1]):
                    num=1
                    while not(j+num>=len(list(expr))) and (self._isNumber(expr[j+num]) or expr[j+num]=='.'):
                        num+=1
                    calcStack.push(float(expr[j:j+num]))
                    numTot+=num
                elif expr[j]=='-':
                    curr=calcStack.pop()
                    curr2=calcStack.pop()
                    calcStack.push(curr2-curr)
                elif expr[j]=='+':
                    curr=calcStack.pop()
                    curr2=calcStack.pop()
                    calcStack.push(curr2+curr)
                elif expr[j]=='/':
                    curr=calcStack.pop()
                    curr2=calcStack.pop()
                    if curr==0:
                        return None
                    calcStack.push(curr2/curr)
                elif expr[j]=='*':
                    curr=calcStack.pop()
                    curr2=calcStack.pop()
                    calcStack.push(curr2*curr)
                elif expr[j]=='^':
                    curr=calcStack.pop()
                    curr2=calcStack.pop()
                    calcStack.push(curr2**curr)
                elif expr[j]=='%':
                    curr=calcStack.pop()
                    curr2=calcStack.pop()
                    calcStack.push(curr2%curr)

        return calcStack.pop()


#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    '''
    checks to see if word is a valid variable name and returns bool
    '''
    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if word!='' and word[0].isalpha() and word.isalnum():
            return True
        else:
            return False
       
    '''
    receives an expression expr and returns the expression with the variables stored in self.states replaced
    '''
    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        exprList=expr.split(' ')
        for i in exprList:
            if self._isVariable(i) and (i not in self.states):  
                return None
        for key in self.states:
            if key in expr:
                expr=expr.replace(key,str(self.states[key]))
        return expr
        

    '''
    calculates the expressions in self.expressions and updates self.states
    returns a dictionary containing how self.states is updated with each expression
    '''
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()
        states2 = {}
        expressions2 = self.expressions.split(';')
        
        for i in range(len(expressions2)):
            i2 = expressions2[i].strip()
            
            if i2.startswith('return '):
                i2 = i2[7:].strip()
                i2 = self._replaceVariables(i2)
                if i2 is None:
                    self.states={}
                    return None
                calcObj.setExpr(i2)
                i2 = calcObj.calculate
                if i2 is None:
                    self.states={}
                    return None
                states2['_return_'] = i2 #return statement

            else:  
                i2 = i2.split('=')
                if len(i2) != 2:
                    self.states={}
                    return None
                variable = i2[0].strip()
                expr2 = i2[1].strip()
                if not self._isVariable(variable):
                    self.states={}
                    return None
                expr2 = self._replaceVariables(expr2)
                if expr2 is None:   #checking for when expression is invalid
                    self.states={}
                    return None
                calcObj.setExpr(expr2)
                result = calcObj.calculate
                if result is None:
                    self.states={}
                    return None
                self.states[variable] = result
                states2[expressions2[i].strip()] = self.states.copy()
        return states2
        



def run_tests():
    import doctest

    # Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    doctest.run_docstring_examples(AdvancedCalculator, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()