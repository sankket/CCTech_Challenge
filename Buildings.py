# Python3 program to count buildings  
# exposed to the sunlight. 
  
# Returns count buildings that 
# exposed sunlight. 
def countBuildings(arr, n): 
  
    # Initialuze result (Note that first  
    # building always sees sunlight) 
    count = 1
  
    # Start traversing element 
    curr_max = arr[0] 
    for i in range(1, n): 
      
        # If curr_element is maximum, 
        # update maximum and increment count 
        if (arr[i] > curr_max): 
          
            count += 1
            curr_max = arr[i] 
  
    return count 
   
arr = [[[4,0],[4,-5],[7,-5],[7,0]], [[0.4,-2],[0.4,-5],[2.5,-5],[2.5,-2]]] 
n = len(arr) 
print(countBuildings(arr, n)) 
