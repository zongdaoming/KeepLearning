# Python 字典(Dictionary) setdefault()方法

```python
dict.setdefault(key,default = None)
```
> key-- 查找的键值

> default-- 键不存在时，设置的默认值键值

`setdefault` 如果不存在会在原字典里添加一个 `key:default_value` 并返回 `default_value`。 `get` 找不到 `key` 的时候不会修改原字典，只返回 `default_value`。若要修改字典 `dic.setdefault(key,default_value)` 等同于 `dic[key] = dic.get(key,default_value)`。




