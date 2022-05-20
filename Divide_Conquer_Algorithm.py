import random as rd # importing random module

lista = [rd.randint(-300, 300) for i in range(15)] # Setting random list in range 15 between numbers -300 and 300

print(lista) # list without sorting

# Divide and Conquer Algorithm

# implementing merging function 
def merge(a, b): # adding a and b elements
    index_a, index_b = 0, 0 # startup indexes
    len_a, len_b = len(a), len(b) # count of elements in a and b variables
    c = [] # empty result list
    while index_a < len_a and index_b < len_b:
        if a[index_a] >= b[index_b]: # Sorting Variants (from the smallest to the highest a <= b), (from the highest to the smallest a >= b)
            c.append(a[index_a])    # \\
            index_a += 1            #  \\
        else:                       #   How we choose the option it will start from the highest or the lowest
            c.append(b[index_b])    #  //
            index_b += 1            # //
    while index_a != len_a:         # \\
        c.append(a[index_a])        #  \\
        index_a += 1                #   \\ Here we implementing the rest of data for example: in the first loop we choosen "a", so in this loop
    while index_b != len_b:         #   // index_a and len_a has 1 so they are equal and index_b because it has 0 It will be added to c list
        c.append(b[index_b])        #  //
        index_b += 1                # //
    return c    # 

def conquer(t, a, b):
    if a == b:
        return [t[a]]
    else:
        sr = (a+b)//2 # variable which sets the middle point of the list
        return merge(conquer(t, a, sr), conquer(t, sr+1, b)) # Uses recursion to merge divided elements. For the first conquer function it takes from start to the half of line and second function takes half plus 1 and the last list

print(conquer(lista, 0, 15-1))