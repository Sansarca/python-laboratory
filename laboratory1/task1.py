"""
З тризначного числа x відняли його останню цифру.
Коли результат розділили на 10, а до отриманого зліва приписали останню цифру числа x, то вийшло число 237. Знайти число x.
"""

print("Данилевич Олександр Олександрович\n Лабораторна робота №1\n Варіант 8\n Знаходження початкового числа")
print("В умові число 237.")
x=237
print("Початкове число:")
print ((x-int(x/100)*100)*10+int(x/100))

