# life = {
#     'kid': {
#         'food': ['milk', 'fruit_pure'], 'work': ['eat', 'sleep']
#     },
#     'adult': {
#         'food' : ['meat', 'corn'], 'work': ['eat', 'sleep', 'sex']
#     }
# }
#
# for key, value in life.items():
#     print(key, ':')
#     for key2, value2 in life[key].items():
#         print(key2, ':', end=' ')
#         for i in value2:
#             print(i, end='  ')
#         print('--', end=' ')
#     print()


s = "1_2,40_5,5_32"
a = [sum(map(int, element.split('_'))) for element in s .split(',')]
print(a)

# s = ['1', '2']
# a = sum(map(int, s))
# print(a)