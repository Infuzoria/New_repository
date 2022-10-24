# Базовые операции в языке программирования - Python

= - Присваивание, операция для сохранения значений в памяти компьютера

**Данные**

> - Числа - 1, 2, 0.5 и так далее. Необходимы для оперделения количественных и арифметических операций.
> - Строки - "СТРОКА" - представление буквенных (языковые) данных
> - Списки [] / Кортежи () - Для создания коллекций (множественное хранение разнообразных типов данных под одним указателем)

**Операции с данными**

> - Все представленные операции ниже можно выполнить с (список/строки/кортежи)
>   - Индексирование - СПИСОК[ЧИСЛО] - получение отдельного значения
>   - Срез - СПИСОК[ЧИСЛО:] СПИСОК[:ЧИСЛО] СПИСОК[ЧИСЛО:ЧИСЛО] - получение группы значений
>   - Подсчет количества элементов - len(СПИСОК)
>   - СТРОКА + СТРОКА - склеивание
>   - СТРОКА * ЧИСЛО - повторение

**Операции сравнения (можно сравнивать любые типы данных)**
```
> < >= <= != ==
and or not
```

**Ветвление**

```
if УСЛОВИЕ:
  тело ветвления - if
elif УСЛОВИЕ:
  тело ветвления - elif
else:
  тело ветвления - else
```

**Циклы**

```
while УСЛОВИЯ:
  тело цикла
```

```
for ПЕРЕМЕННАЯ in СПИСОК/КОРТЕЖ/СТРОКА/range:
  тело цикла
```

**Функции**

```
def ИМЯ_ФУНКЦИИ(АРГУМЕНТ):
  тело функции
```
