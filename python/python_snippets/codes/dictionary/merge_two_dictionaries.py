# Merge Two Dictionaries with Brute Force
class Solution:
    def __init__(self):
        super(Solution, self).__init__()
        yusuke_power = {"Yusuke Urameshi": "Spirit Gun"}
        hiei_power = {"Hiei": "Jagan Eye"}
        for key, value in hiei_power.items():
            yusuke_power[key] = value
        for key,value in hiei_power.items():
            print(f"key is  {key} value is {value}")

# Merge Two Dictionaries with a Dictionary Comprehension
class Solution2:
    def __init__(self):
        super(Solution2, self).__init__()
        yusuke_power = {"Yusuke Urameshi": "Spirit Gun"}
        hiei_power = {"Hiei": "Jagan Eye"}
        # powers = {key:value for key, value in d.items()}
        # 两层小循环
        powers = {key:value for d in (yusuke_power, hiei_power) for key, value in d.items()}
        for key,value in powers.items():
            print(f"key is {key}, value is {value}")

# Merge Two Dictionaries with Copy and Update
class Solution3:
    def __init__(self):
        super(Solution3, self).__init__()
        yusuke_power = {"Yusuke Urameshi": "Spirit Gun"}
        hiei_power = {"Hiei": "Jagan Eye"}
        powers = yusuke_power.copy()
        powers.update(hiei_power)
        for key,value in powers.items():
            print(f"key is {key}, value is {value}")

# Merge Two Dictionaries with Dictionary Unpacking
class Solution4:
    def __init__(self):
        super(Solution4, self).__init__()
        test_1  = {1:"zong",2:"dao",3:"ming"}
        test_2  = {4:"zong",5:"kai",6:"xuan"}
        powers  = {**test_1,**test_2}
        for key,value in powers.items():
                    print(f"key is {key}, value is {value}")

        
    
