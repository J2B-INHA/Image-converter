import json

content = {
    'name': 'nero',
    'age': 2,
    'color': 'black',
    'like_food': ['banana', 'apple', 'chewrrr'],
    'is_cat': True,
    'is_dog': False,
    'friends': {
    	'poki': 'cat',
        'bowow': 'dog',
        'yatong': 'cat',
    }
}

with open('test.json', 'w') as f:
    json.dump(content, f, indent=2)

with open('test.json', 'r') as f:
    content = json.load(f)

print(content)
print(content['name'])
