# class List:
#     def __init__(self, input_list):
#         self.input_list = input_list
#         self.output_list = []
#
#     def pull_data(self):
#         while len(self.input_list) > 0:
#             if type(self.input_list[0]) is int:
#                 self.output_list.append(self.input_list.pop(0))
#             else:
#                 self.pull_data()
#         return print(self.output_list)
#
#
# l = [1, 2, 3, 4, [9, [5, 6, []]]]
# my_list = List(l)
# my_list.pull_data()


def pull_data(array):
    result = []
    while len(array) > 0:
        if type(array[0]) is int:
            result.append(array.pop(0))
        else:
            result.extend(pull_data(array[0]))
            array.pop(0)
    return result


l = [1, 2, 3, 4, [9, [5, 6, []]]]

print(pull_data(l))