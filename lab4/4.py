{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a generator that generates the squares of numbers up to some number N."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "4\n",
      "9\n",
      "16\n",
      "25\n",
      "36\n",
      "49\n",
      "64\n"
     ]
    }
   ],
   "source": [
    "def square_to(N):\n",
    "    cnt = 1\n",
    "    while cnt <= N:\n",
    "        yield cnt**2\n",
    "        cnt += 1\n",
    "\n",
    "N = int(input(\"Enter number: \"))\n",
    "square_num = square_to(N)\n",
    "for num in square_num:\n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20\n"
     ]
    }
   ],
   "source": [
    "def only_even(N):\n",
    "    cnt = 0\n",
    "    while cnt <= N:\n",
    "        if cnt % 2 == 0:\n",
    "            yield cnt\n",
    "        cnt += 1\n",
    "\n",
    "N = int(input(\"Enter number: \"))\n",
    "even_num = only_even(N)\n",
    "print(*even_num, sep = ', ')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0, 12, 24, 36, 48, 60, 72, 84, 96\n"
     ]
    }
   ],
   "source": [
    "def divisible_by_3_and_4(N):\n",
    "    cnt = 0\n",
    "    while cnt <= N:\n",
    "        if cnt % 3 == 0 and cnt % 4 == 0:\n",
    "            yield cnt\n",
    "        cnt += 1\n",
    "\n",
    "N = int(input(\"Enter number: \"))\n",
    "nums = divisible_by_3_and_4(N)\n",
    "print(*nums, sep = ', ')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a \"for\" loop and print each of the yielded values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n",
      "36\n",
      "49\n",
      "64\n"
     ]
    }
   ],
   "source": [
    "def squares(A, B):\n",
    "    for cnt in range(A, B+1):\n",
    "        yield cnt**2\n",
    "\n",
    "A = int(input(\"Enter number A: \"))\n",
    "B = int(input(\"Enter number B: \"))\n",
    "square_num = squares(A, B)\n",
    "for num in square_num:\n",
    "    print(num)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Implement a generator that returns all numbers from (n) down to 0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "def countdown(N):\n",
    "    cnt = N\n",
    "    while cnt >= 0:\n",
    "        yield cnt\n",
    "        cnt -= 1\n",
    "\n",
    "N = int(input(\"Enter number:\"))\n",
    "nums = countdown(N)\n",
    "for num in nums:\n",
    "    print(num)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}