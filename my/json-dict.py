#coding=utf-8

"""
定义和使用字典 (即json)

"""
import json


def main():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71

    # 可以增加,修改
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))

    # 清空
    scores.clear()
    print(scores)


    #json (更上面区别?无,就是dict) # # # # # # # # # # # # #
    json_str = '{"name": "骆昊", "age": 38, "title": "叫兽"}'
    result = json.loads(json_str)
    print(result)
    print(type(result))
    print(result['name'])
    print(result['age'])

    # json 变为字符串
    teacher_dict = {'name': '白元芳', 'age': 25, 'title': '讲师'}
    json_str = json.dumps(teacher_dict)
    print(json_str)
    print(type(json_str))

    # 把list变为string
    fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
    json_str = json.dumps(fruits_list)
    print(json_str)
    print(type(json_str))

if __name__ == '__main__':
    main()
