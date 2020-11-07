from math import sqrt

print("Hello World",123)
print(sqrt(4), f"є рівним {sqrt(4)}")

arr = [1,2,3]
try:
    print(arr[3])
except Exception as e:
    print(e)
finally:
    print("Приклад обробки виключень")

with open("F:/textfile.txt", "r") as f:
    for line in f:
        print(line)

sum_lambda = lambda a, b:f"Сума двох чисел {a+b}"
print("Це просто функція:", sum_lambda)
print("Це її виклик:", sum_lambda(1,2))
