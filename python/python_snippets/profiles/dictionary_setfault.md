# Python 字典(Dictionary) setdefault()方法

```python
dict.setdefault(key,default = None)
```
> key-- 查找的键值

> default-- 键不存在时，设置的默认值键值

`setdefault` 如果不存在会在原字典里添加一个 `key:default_value` 并返回 `default_value`。 `get` 找不到 `key` 的时候不会修改原字典，只返回 `default_value`。若要修改字典 `dic.setdefault(key,default_value)` 等同于 `dic[key] = dic.get(key,default_value)`。

# Collections.defaultdict()的使用
Python中通过Key访问字典，当Key不存在时，会引发‘KeyError’异常。为了避免这种情况的发生，可以使用collections类中的`defaultdict()`方法来为字典提供默认值。

* 1. 使用List作为第一个参数，可以很容易地将键-值对序列转化为列表字典
当字典中没有的键第一次出现时，`default_factory`自动为其返回一个空列表，`list.append()`会将值添加进新列表；再次遇到相同的键时，`list.append()`将其它值再添加进该列表。
```python
from collections import defaultdict
s=[('yellow',1),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
my_dict = defaultdict(list)
for key,value in s:
    my_dict[key].append(value)
print(my_dict)
```

* 2. Defaultdict 还可以被用来计数，将default_factory 设置为Int 即可
```python
from collections import defaultdict
s = 'zongdaomingandzongkaixuan'
my_dict = 

```
