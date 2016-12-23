print "--------------------------start--------------------------"
diction={}  
d=1
#Function to parse the bracketed problem statement and put the intermediate results(could be terminal or non terminal) into dictionary.
def parse(expression):
    def _helper(iter):
        items = []
        global d
        for item in iter:
            if item == '(':
                result, closeparen = _helper(iter)
                if not closeparen:
                    raise ValueError("Bad expression: Please check if you missed the parentheses")
                diction["T"+str(d)] = result;
                #print (result)
                if 4 > len(result) > 0  :
                  result="T"+str(d)
                d=d+1
                items.append(result)
                #print (result)
            elif item == ')':
                return items, True
            else:
                items.append(item)

        return items, False
    return _helper(iter(expression))[0]

problem_stmt="-(((p)&(-(q)))|((p)|(r)))"

#Please uncomment one of the following problem and comment above for checking the output.
#Also don't give any spaces or If you want we can write trimming code for handling this condition
#problem_stmt="((p)|(-(q)))"
#problem_stmt="((p)|(q))"
#problem_stmt="-((p)&(q))"
#problem_stmt="(((p)|(q))|(r))"
#problem_stmt="(((p)&(q))|((p)&(r)))|((q)&(r))"
#problem_stmt="(((p)&((q)|(r)))|((q)|(r)))"

problem = parse(problem_stmt)

#adding last/root element
diction["T"+str(d)]=problem;
#print 'Debugging point#1 : '+str(d)

# now performing flipping of operators over the and/or over the 3 length elements
final_dict={}
j=0;
for i in range(len(diction)):
  #print 'Debugging point#2 : '+str(i+1) +' = ' + ' '.join(diction["T"+str(i+1)])
  j=j+1
  
  #if len=3 that means involvement of binary operator
  if len(diction["T"+str(i+1)])==3 :
    #print 'Debugging point#3 : '+''.join(diction[diction["T"+str(i+1)][2]])
    
    # used join in following statement because a single element of dictionary is treated as list
    a=''.join(diction[diction["T"+str(i+1)][0]])
    b=''.join(diction[diction["T"+str(i+1)][2]])
    #resetting the non-terminal symbols with terminal symbols
    if len(a)>1:
      diction["T"+str(i+1)][0]= '('+a+')'
    else :
      diction["T"+str(i+1)][0]= a
    if len(b)>1:
      diction["T"+str(i+1)][2]= '('+b+')'
    else :
      diction["T"+str(i+1)][2]= b
    
    final_dict[j]= ''.join(diction["T"+str(i+1)][0]) +'&'+''.join(diction["T"+str(i+1)][2])
    j=j+1
    final_dict[j]= ''.join(diction["T"+str(i+1)][0]) +'|'+''.join(diction["T"+str(i+1)][2])
  
  #if len=2 that means involvement of unary operator
  elif len(diction["T"+str(i+1)])==2 :
    #since here a would be an operator
    a=''.join(diction["T"+str(i+1)][0])
    #since here b would be a non terminal symbol
    b=''.join(diction[diction["T"+str(i+1)][1]])
    #resetting the non-terminal symbols with terminal symbols
    diction["T"+str(i+1)][1]= '('+b+')'
    final_dict[j]=a+'('+b+')'
    
  else :
    if len(diction) !=i+1:
      final_dict[j]= ''.join(diction["T"+str(i+1)])
  #print str(j)+'Debugging point#4 : '+''.join(final_dict[j])
print "Your problem statement : " + problem_stmt
print "Your plausible ALT solutions are as followed : "
for k in range(len(final_dict)):
  print str(k+1) +' = ' + ''.join(final_dict[k+1])
print "--------------------------end--------------------------"
