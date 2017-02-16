

def string_scramble(string_one, string_two):
  list1=[]
  list2=[]
  list1.append(compare_intersect(string_one.lower(),string_two.lower()))
  list2=list(set(string_one.lower()).intersection(set(string_two.lower())))
  return list2
pass


def compare_intersect(x, y):
    return frozenset(x).intersection(y)
    
print (string_scramble("Grass","grilled cheese"))