print "-------------Starting Complete Alt implementation---------------"
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
                #print 'Debugging point In fn Parse #1 :'+''.join(result)
                if 4 > len(result) > 0  :
                  result="T"+str(d)
                d=d+1
                items.append(result)
                #print 'Debugging point In fn Parse #2 :'+(result)
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
#problem_stmt="((((p)&(q))|((p)&(r)))|((q)&(r)))"
#problem_stmt="(((p)&((q)|(r)))|((q)|(r)))"

problem = parse(problem_stmt)

#adding last/root element only if it's case of negation.
if len(problem)==2:
  diction["T"+str(d)]=problem;
#print 'Debugging point#1 : '+str(d)

final_dict={}

for i in range(len(diction)):
  
  #single terminal handling
  if len(diction["T"+str(i+1)])==1 :
    final_dict["T"+str(i+1)] = diction["T"+str(i+1)]
    
  #handling unary operator(negation) based expression
  elif len(diction["T"+str(i+1)])==2 :
    # index =diction["T"+str(i+1)][1]
    final_dict["T"+str(i+1)] = final_dict[diction["T"+str(i+1)][1]]; 
    for l in range(len(final_dict["T"+str(i)])):
      final_dict["T"+str(i+1)].append('-(' + final_dict["T"+str(i)][l] + ')')
  
  #handling binary operator ( & | )  based expression
  elif len(diction["T"+str(i+1)])==3 :
    temp_arr1 = final_dict[diction["T"+str(i+1)][0]]
    temp_arr2 = final_dict[diction["T"+str(i+1)][2]]
    final_dict["T"+str(i+1)] = temp_arr1 + temp_arr2
    
    for x in range(len(temp_arr1)):
      for y in range(len(temp_arr2)):
        final_dict["T"+str(i+1)].append("("+temp_arr1[x] +'|'+ temp_arr2[y]+")")
        final_dict["T"+str(i+1)].append("("+temp_arr1[x] +'&'+ temp_arr2[y]+")")
    #resetting temp_arr1 & temp_arr2
    temp_arr1=temp_arr2=[]
  
  #handling rest of expression which shd not be case
  else:
    print "Please check the dictionary elements as multiple elements encountered:(Should be less than 4)"

print "Your problem statement : " + problem_stmt
print "Your plausible ALT solutions are as followed : "
final_array=final_dict["T"+str(i+1)]

#Removing repeated elements
#final_array=list(set(final_array))
#Sorting out array in ascending order of string length
#final_array.sort(key = len)

for k in range(len(final_array)):
  print str(k+1) +' = ' + final_array[k]


print "--------------------------end--------------------------"
