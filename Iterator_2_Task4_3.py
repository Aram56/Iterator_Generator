# 1. Написать итератор аналогичный итератору из задания 1, 
# но обрабатывающий списки с любым уровнем вложенности. 
# Шаблон и тест в коде ниже:

class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.start_first_level = 0
        self.end_first_level = len(self.list)
        self.start_second_level = -1
        return self
    
    def __next__(self):
        self.start_second_level += 1 # Вот здесь прописать бы увеличение последнего индекса item на 1.
        # self.list[-1] += 1 # к сожалению так нельзя и не работает 
        # item[-1] += 1 # к сожалению так нельзя и не работает 
        
        
        self.end_second_level = len(self.list[self.start_first_level])
                
        if self.start_second_level == self.end_second_level: 
            self.start_second_level = 0
            self.start_first_level += 1
            
        if self.start_first_level == self.end_first_level or self.list[self.start_first_level][self.start_second_level] == []:
            raise StopIteration
                
        item = self.list[self.start_first_level][self.start_second_level] 
        
        if bool(item) and type(item) != list:
            # print('можно выводить')
            item = item
        if type(item) == list: 
            # print('есть список')
            while type(item) == list:
                # print('вкопаться')
                item = item[0]
            while type(item) != list: # А здесь обратный процесс убирать послений индекс 
                # print('раскопаться') # и приавлять к ставшему уже дргому последнему индексу "1"
                return item
                
        return item


# def test_3():

#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]

#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):

#         assert flat_iterator_item == check_item

#     assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


# if __name__ == '__main__':
#     test_3()


list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

list_of_list = FlatIterator(list_of_lists_2)

for item in list_of_list:
    print(item)

print('Цикла нет')


    