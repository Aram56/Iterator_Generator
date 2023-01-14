# 1. Доработать класс FlatIterator в коде ниже. Должен получиться итератор, 
# который принимает список списков и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        
        self.list = list_of_list
        
        
    def __iter__(self):
        self.start_first_level = 0
        self.end_first_level = len(self.list)
        self.start_second_level = -1
        
        return self

    def __next__(self):
        self.start_second_level += 1
        self.end_second_level = len(self.list[self.start_first_level])
        
        if self.start_second_level == self.end_second_level: 
            self.start_second_level = 0
            self.start_first_level += 1
            
                       
        if self.start_first_level == self.end_first_level:
            raise StopIteration
        
        return self.list[self.start_first_level][self.start_second_level]
    
        
        
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()




    