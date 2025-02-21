{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a Python program to convert degree to radian."
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
      "0.2617993877991494\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "degree = int(input(\"Input degree: \"))\n",
    "rad = math.radians(degree)\n",
    "print(\"Output radian:\", rad)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a Python program to calculate the area of a trapezoid."
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
      "Expected Output: 27.5\n"
     ]
    }
   ],
   "source": [
    "h = int(input(\"Height: \"))\n",
    "base1 = int(input(\"Base, first value: \"))\n",
    "base2 = int(input(\"Base, second value: \"))\n",
    "area = (base1 + base2) / 2 * h\n",
    "print(\"Expected Output:\", area)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a Python program to calculate the area of regular polygon."
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
      "Expected Output: 625.0000000000001\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "n = int(input(\"Input number of sides: \"))\n",
    "s = int(input(\"Input the length of a side: \"))\n",
    "P = n * s\n",
    "a = s / (2 * math.tan(math.pi / n))\n",
    "area = P * a / 2\n",
    "print(\"The area of the polygon is:\", area)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a Python program to calculate the area of a parallelogram."
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
      "The area of the polygon is: 30\n"
     ]
    }
   ],
   "source": [
    "b = int(input(\"Length of base: \"))\n",
    "h = int(input(\"Height of parallelogram: \"))\n",
    "area = b * h\n",
    "print(\"Expected Output:\", area)"
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