# 4.* (необязательное задание) Написать генератор аналогичный генератору из задания 2, 
# но обрабатывающий списки с любым уровнем вложенности. Шаблон и тест в коде ниже:
import types


def flat_generator(list_of_list):
    
    for item_first in list_of_list:
        for item_second in item_first:
            if type(item_second) != list:
                yield item_second
            if type(item_second) == list:
                for item_thirth in item_second:
                    if type(item_thirth) != list:
                        yield item_thirth
                    else:
                        while type(item_thirth) == list:
                            item_thirth = item_thirth[0] 
                            if type(item_thirth) != list:
                                yield item_thirth
            
            while type(item_thirth) == list:
                item_thirth = item_thirth[0] 
                if type(item_thirth) != list:
                    yield item_thirth
           
            
            
def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()



    