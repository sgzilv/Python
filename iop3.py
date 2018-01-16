import pickle
import json

d = dict(name = 'Bob', age = 20, score = 88)
'''
print(pickle.dumps(d))


f = open('d:/iod/dump.txt', 'wb')
pickle.dump(d, f)
f.close()

with open('d:/iod/dump.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)

print(json.dumps(d))

with open('d:/iod/jdump.txt', 'w') as f:
    json.dump(d, f)


with open('d:/iod/jdump.txt', 'r') as f:
    print(json.load(f))
    
json_str = '{"name": "bob", "age": 18, "score": 90}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

        
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Jim', 22, 100)
print(json.dumps(s, default = student2dict))
print(json.dumps(s, default = lambda obj: obj.__dict__))
'''

#练习
#对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
