import json
#此时student是一个dict格式内容，不是json

student={
    "name":"liudan",
    "age":18,
    "mobile":"123461235"
}
print(type(student))

stu_json = json.dumps(student)
print(type(stu_json))
print("json对象：{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print("字典对象：{0}".format(stu_dict))
