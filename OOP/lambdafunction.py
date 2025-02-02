# Lambda function=A small anonymous function for a one time use (throw away function)
#     They take any number of arguments, but have only 1 expression
#     Helps keep the namespace clean and is useful with higher-order functions
#     'sort()', 'map()', 'filter()', 'reduce()'
#     lambda parameters: expression


double = lambda x:x*2
addition = lambda x,y: x+y
verify_age = lambda age:True if age >= 18 else False
min = lambda x,y:x if x < y else y
max = lambda x,y:x if x > y else y
fullName = lambda first,last: first + " " + last

print(double(12))
print(addition(1,2))
print(verify_age(15))
print(min(15,30))
print(max(15,30))
print(fullName("prajwol", "subedi"))