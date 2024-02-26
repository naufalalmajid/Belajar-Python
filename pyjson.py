# in python we have built-in package called json, which it is can be used to work with JSON data
import json

# convert from JSON to python
x = '{ "name":"John", "age":30, "city":"New York"}'
xpy = json.loads(x)

print(type(xpy), xpy)

# convert from python to JSON
y = {"name": "almajid", "age": 21, "city": ("Singapore")}
yjs = json.dumps(y)

print(type(yjs), yjs)

# format convert result, we can using indent parameter, separators, and order the result by using sort_keys parameter
z = json.dumps(y, indent=4, sort_keys=True)
