# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fn1 = 1
fn1 = 1

n = int(input("введите число:  "))

print(fn1, fn2, end=' ')

for i in range(2, n):
    fn, fn2 = fn2, fn1 + fn2
    print(fn2, end=' ')