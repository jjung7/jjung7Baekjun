import sys
​
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}
​
def join_array(ints):
    str_list = list(map(str, ints))
    return " ".join(str_list)
​
class ArrayStack:
​
    def __init__(self):
        self.data = [] 
​
    def size(self): 
        return len(self.data)
​
    def isEmpty(self): 
        return self.size() == 0
​
    def push(self, item): 
        self.data.append(item)
​
    def pop(self):
        return self.data.pop()
​
    def peek(self):
        return self.data[-1]
​
    def serialize(self):
        return join_array(self.data)
​
​
def convert_to_postfix(S): #'3+1'
    opStack = ArrayStack()
    answer = ''
    
    for w in S : 
        if w in prec :
            if opStack.isEmpty() : # +
                opStack.push(w)
            else :
                if w == '(' :
                    opStack.push(w)
                else :
                    while prec.get(w) <= prec.get(opStack.peek()) :
                        answer += opStack.pop()
                        if opStack.isEmpty() : break
                    opStack.push(w)
        elif w == ')' :
            while opStack.peek() != '(' :
                answer += opStack.pop()
            opStack.pop()
        else :
            answer += w #31
        
    while not opStack.isEmpty() : #31+
        answer += opStack.pop()
    
    return answer
​
def calculate(tokens):
    stack = ArrayStack()  
    for token in tokens:
        if token == '+':
            stack.push(stack.pop()+stack.pop())
        elif token == '-':
            stack.push(-(stack.pop()-stack.pop()))
        elif token == '*':
            stack.push(stack.pop()*stack.pop())
        elif token == '/':
            rv = stack.pop()
            stack.push(stack.pop()//rv)
        else:
            stack.push(int(token))
        
    return stack.pop()
​
# infix 수식에서 공백 제거
infix = sys.stdin.readline().replace("\n", "").replace(" ", "") #3+1
​ 
postfix = convert_to_postfix(infix) #'3+1'
​
print(f"postfix : {postfix}")
​
result = calculate(postfix)
​
print(f"result : {result}")
​