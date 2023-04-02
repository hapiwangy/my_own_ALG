import copy
class my_alg:
    def __init__(self, data):
        if isinstance(data, (tuple, list)):
            self.data = list(data)
        else:
            self.data = data
    def binary_search(self, target: int):
        if not isinstance(self.data, list):
            print("當前資料格式錯誤(請以list當作輸入)")
            return 
        array = sorted(self.data)
        left, right = 0, len(array)
        while True:
            current = (left + right) // 2
            if current > len(array) - 1 or left > right:
                print(f"There is no {target} in {array}!")
                return 
            if array[current] > target:
                right = current - 1
            elif array[current] < target:
                left = current + 1
            elif array[current] == target:
                print(f"{target} at index {current} in list {array}")
                return array, current, target
    def selection_sort(self):
        SortArray = []
        OriginArray = copy.copy(self.data)
        for _ in range(len(OriginArray)):
            value, index = self.find_min_value_and_index(OriginArray)
            SortArray.append(value)
            OriginArray.pop(index)
        print(f"{self.data} 排序後的結果為: {SortArray}")
    def find_min_value_and_index(self, what):    
        value, index = what[0], 0
        for x in range(1, len(what)):
            if what[x] < value:
                value, index = what[x], x
        return value, index 
if __name__ == '__main__':
    test_obj = my_alg([10,3,5,2,7,6])
    # test_obj.binary_search(10)
    test_obj.selection_sort()