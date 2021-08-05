# Prime numbers
## Description
A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself. However, 4 is composite because it is a product (2 × 2) in which both numbers are smaller than 4. Primes are central in number theory because of the fundamental theorem of arithmetic: every natural number greater than 1 is either a prime itself or can be factorized as a product of primes that is unique up to their order.

The property of being prime is called primality. A simple but slow method of checking the primality of a given number n, called trial division, tests whether n is a multiple of any integer between 2 and square root of n. Faster algorithms include the Miller–Rabin primality test, which is fast but has a small chance of error, and the AKS primality test, which always produces the correct answer in polynomial time but is too slow to be practical. Particularly fast methods are available for numbers of special forms, such as Mersenne numbers. As of December 2018 the largest known prime number is a Mersenne prime with 24,862,048 decimal digits.

There are infinitely many primes, as demonstrated by Euclid around 300 BC. No known simple formula separates prime numbers from composite numbers. However, the distribution of primes within the natural numbers in the large can be statistically modelled. The first result in that direction is the prime number theorem, proven at the end of the 19th century, which says that the probability of a randomly chosen number being prime is inversely proportional to its number of digits, that is, to its logarithm.

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

