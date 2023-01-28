def remove_duplicates(medicine_string, k):
    
    subparts = [medicine_string[i:i+k] for i in range(0, len(medicine_string), k)]
    
    modified_subparts = []
  
    for subpart in subparts:
        modified_subpart = ""
        
        for char in subpart:
            if char not in modified_subpart:
                modified_subpart += char
      
        modified_subparts.append(modified_subpart)
    
    return modified_subparts


medicine_string = "AABCAAADA"
k = 3
print(remove_duplicates(medicine_string,k)) 

