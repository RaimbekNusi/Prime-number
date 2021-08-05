# Prime numbers
## Description
A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself. However, 4 is composite because it is a product (2 × 2) in which both numbers are smaller than 4. Primes are central in number theory because of the fundamental theorem of arithmetic: every natural number greater than 1 is either a prime itself or can be factorized as a product of primes that is unique up to their order.

The property of being prime is called primality. A simple but slow method of checking the primality of a given number n, called trial division, tests whether n is a multiple of any integer between 2 and square root of n. Faster algorithms include the Miller–Rabin primality test, which is fast but has a small chance of error, and the AKS primality test, which always produces the correct answer in polynomial time but is too slow to be practical. Particularly fast methods are available for numbers of special forms, such as Mersenne numbers. As of December 2018 the largest known prime number is a Mersenne prime with 24,862,048 decimal digits.

There are infinitely many primes, as demonstrated by Euclid around 300 BC. No known simple formula separates prime numbers from composite numbers. However, the distribution of primes within the natural numbers in the large can be statistically modeled. The first result in that direction is the prime number theorem, proven at the end of the 19th century, which says that the probability of a randomly chosen number being prime is inversely proportional to its number of digits, that is, to its logarithm.

Several historical questions regarding prime numbers are still unsolved. These include Goldbach's conjecture, that every even integer greater than 2 can be expressed as the sum of two primes, and the twin prime conjecture, that there are infinitely many pairs of primes having just one even number between them. Such questions spurred the development of various branches of number theory, focusing on analytic or algebraic aspects of numbers. Primes are used in several routines in information technology, such as public-key cryptography, which relies on the difficulty of factoring large numbers into their prime factors. In abstract algebra, objects that behave in a generalized way like prime numbers include prime elements and prime ideals.

## Problem Description
Caching is a technique of much importance in computer science. The technique simply involves recording the result of a complex calculation rather than re-computing that result every time it is needed. It may or may not surprise one to hear that there is no known formula for determinining whether or not a given number N is prime or not. More or less, the only way to know is to try dividing N by all integers between 1 and itself and seeing if any of them yield a remainder. For large N, this is a time-consuming computation, and therefore a good example of something that might be cached for some problems. For this question, the task is to write a program that takes a given set of numbers, determines whether each of them is prime, and caches the result using a dictionary.

## Problem Details
A sample input file, numbers.txt is provided as an example. It contains some positive integers, one per line of the file. It is used to test the program, however the program should work for ANY similarly formatted input file.

## How to use

Here are the steps for how to open, use and utilize the program:

- First, download all of the files listed above;
- Put all the files in one folder;
- Open the file Project_pg.py;
- The program will open a command console in which it will ask you to name a .txt file located in the same folder;
- Finally, the program will output a graph with results of clusterized data.


*The program can use other .txt file that are in the same format as provided files.

# Простые числа

## Описание
Простое число - это натуральное число больше 1, которое не является произведением двух меньших натуральных чисел. Натуральное число больше 1, которое не является простым, называется составным числом. Например, число 5 является простым, потому что единственные способы записать его как продукт, 1 × 5 или 5 × 1, включают само число 5. Однако число 4 составное, потому что это произведение (2 × 2), в котором оба числа меньше 4. Простые числа занимают центральное место в теории чисел в силу фундаментальной арифметической теоремы: каждое натуральное число больше 1 либо само простое, либо могут быть разложены на множители как произведение простых чисел, уникальное в соответствии с их порядком.

Свойство быть простым называется первичностью. Простой, но медленный метод проверки простоты данного числа n, называемый пробным делением, проверяет, является ли n кратным любому целому числу от 2 до квадратного корня из n. Более быстрые алгоритмы включают тест на простоту Миллера – Рабина, который является быстрым, но имеет небольшую вероятность ошибки, и тест на простоту AKS, который всегда дает правильный ответ за полиномиальное время, но слишком медленный, чтобы быть практичным. Особенно быстрые методы доступны для ряда специальных форм, таких как числа Мерсенна. По состоянию на декабрь 2018 года самым большим известным простым числом является простое число Мерсенна с 24 862 048 десятичными знаками.

Простых чисел бесконечно много, как показал Евклид около 300 г. до н.э. Нет известной простой формулы, отделяющей простые числа от составных. Однако распределение простых чисел в натуральных числах в большом можно смоделировать статистически. Первым результатом в этом направлении является теорема о простых числах, доказанная в конце XIX века, которая гласит, что вероятность того, что случайно выбранное число будет простым, обратно пропорциональна его количеству цифр, то есть его логарифму.

Некоторые исторические вопросы, касающиеся простых чисел, до сих пор не решены. К ним относятся гипотеза Гольдбаха о том, что каждое четное целое число больше 2 может быть выражено как сумма двух простых чисел, и гипотеза о двойных простых числах о том, что существует бесконечно много пар простых чисел, между которыми имеется только одно четное число. Такие вопросы стимулировали развитие различных разделов теории чисел, в которых основное внимание уделялось аналитическим или алгебраическим аспектам чисел. Простые числа используются в нескольких процедурах в информационных технологиях, таких как криптография с открытым ключом, которая основана на сложности разложения больших чисел на их простые множители. В абстрактной алгебре объекты, которые ведут себя обобщенно как простые числа, включают простые элементы и простые идеалы.

## Описание задачи

Кэширование - это очень важная техника в информатике. Этот метод просто включает запись результата сложного вычисления, а не повторное вычисление результата каждый раз, когда это необходимо. Кто-то может или не удивится, услышав, что не существует известной формулы для определения того, является ли данное число N простым или нет. Более или менее, единственный способ узнать это - попытаться разделить N на все целые числа между 1 и самим собой и посмотреть, дает ли какое-либо из них остаток. Для больших N это трудоемкое вычисление и, следовательно, хороший пример чего-то, что можно кэшировать для решения некоторых проблем. Для этого вопроса задача состоит в том, чтобы написать программу, которая принимает заданный набор чисел, определяет, является ли каждое из них простым, и кэширует результат с помощью словаря.

## Детали задачи

В качестве примера предоставляется образец входного файла numbers.txt. Он содержит некоторые положительные целые числа, по одному на строку файла. Он используется для тестирования программы, однако программа должна работать с ЛЮБЫМ входным файлом аналогичного формата.

## Как использовать
Шаги по открытию, использованию программы:

- Сначала загрузите все файлы, перечисленные выше;
- Поместите все файлы в одну папку;
- Откройте файл Project_pg.py;
- Программа откроет командную консоль, в которой попросит вас назвать файл .txt, расположенный в той же папке;
- Наконец, программа выведет график с результатами кластеризованных данных.
- Программа может использовать другие файлы .txt в том же формате, что и предоставленные файлы.
