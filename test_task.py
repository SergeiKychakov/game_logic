# Плюсы нового алгоритма:
# Новый алгоритм использует побитовую операцию & - это быстрее операции деления по модулю.
# Проверка младшего бита делает алгоритм более эффективным и оптимизированным.

# Минусы нового алгоритма:
# Новый алгоритм менее понятен.

# 1
# Определение чётности числа.
def is_even(value):
    if value & 1 == 0:  # Проверка младшего бита
        return True
    else:
        return False

# 2
# Реализация с использованием массива более эффективна по временной сложности операций добавления и извлечения элементов, 
# а также более экономична по памяти. 
# Реализация с использованием списка более проста и интуитивно понятна, но менее эффективна по времени и памяти. 

class CircularBufferList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def put(self, value):
        if len(self.buffer) == self.capacity:
            del self.buffer[0]
        self.buffer.append(value)

    def get(self):
        if len(self.buffer) == 0:
            return None
        return self.buffer.pop(0)


class CircularBufferArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def put(self, value):
        if self.size == self.capacity:
            return
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def get(self):
        if self.size == 0:
            return None
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

# 3
Я считаю, что данная функция соответствует заданным критериям - она эффективна по времени выполнения благодаря своей временной сложности 
O(n log n) в среднем случае, а также проста в реализации и понимании. Быстрая сортировка часто используется в реальных проектах благодаря своей высокой производительности и эффективности.

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

