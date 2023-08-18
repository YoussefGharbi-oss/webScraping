def check_items_not_in_string(item_list, input_string):
    for item in item_list:
        
        if item in input_string : 
            return False
        
        return True 
  
            

# Example list and string


result = check_items_not_in_string(my_list, my_string)
print("Any item not in string:", result)