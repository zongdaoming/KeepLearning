# Reverse Dictionary Lookup by Brute Force

class Solution(object):
    def __init__(self):
        super(Solution, self).__init__()
        my_dict = {
            "color":"red",
            "width": 17,
            "height":19,
        }

        value_to_find = "red"
        # color:red
        for key, value in my_dict.items():
            if value  == value_to_find:
                print(f'{key}:{value}')

# Reverse Dictionary Lookup Using a Generator Expression
class Solution2:
    def __init__(self):
        super(Solution2, self).__init__()
        my_dict = {
            "color":"red",
            "width": 17,
            "height":19,
        }
        value_to_find = 'red'
        key = next(key for key,value in my_dict.items() if value==value_to_find)
        print(f'{key}:{value_to_find}')

# Naturally, the difference between a list comprehension and a generator expression 
# is that there’s no list created. 
# In other words, we save memory and possibly time.
# If we call next more times than there are matches, we get a StopIteration error. 
# As a workaround, we can use a for-each loop directly:

# Reverse Dictionary Lookup Using an Inverse Dictionary 

class Solution3:
    def __init__(self):
        super(Solution3, self).__init__()
        my_dict = {
            "color":"red",
            "width": 17,
            "height":19,
        }
        value_to_find = "magenta"
        my_reverse_dict = {value:key for key, value in my_dict.items()}
        key = my_reverse_dict[value_to_find]
        print(key)

# Unfortunately, this solution won’t work for every circumstance because not all values are hashable (e.g. lists), 
# but it gets the job done. 
# Likewise, it only saves the last key for any duplicate values. As a result, other possible keys are lost.


class Solution4:
    def __init__(self):
        super(Solution4, self).__init__()
    my_dict = {"color": "red", "width": 17, "height": 19, "columns": 17, "rows":19}
    value_to_find = "red"
    my_inverted_dict = dict()
    for key,value in my_dict.items():
        my_inverted_dict.setdefault(value, list()).append(key)
        # c.setdefault(2,[]).append("daoming")
        # {1: 'zong', 2: ['daoming']}
    # keys = my_inverted_dict[value_to_find]
    for key, value in my_inverted_dict.items():
        print(f"key is {key}, value is {value}")
    
solution = Solution4()