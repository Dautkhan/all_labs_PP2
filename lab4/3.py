{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a Python program to subtract five days from current date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "February/10/2025\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "\n",
    "x = datetime.datetime.now() - datetime.timedelta(days = 5)\n",
    "\n",
    "print(x.strftime('%B/%d/%Y'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a Python program to print yesterday, today, tomorrow."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "February/14/2025\n",
      "February/15/2025\n",
      "February/16/2025\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "\n",
    "yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)\n",
    "today = datetime.datetime.now()\n",
    "tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)\n",
    "\n",
    "\n",
    "print(yesterday.strftime('%B/%d/%Y'))\n",
    "print(today.strftime('%B/%d/%Y'))\n",
    "print(tomorrow.strftime('%B/%d/%Y'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a Python program to drop microseconds from datetime."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2025-02-15 13:49:03\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "\n",
    "x = datetime.datetime.now().replace(microsecond=0)\n",
    "\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a Python program to calculate two date difference in seconds."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "87000\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "\n",
    "date1 = datetime.datetime(2018, 6, 1, 12, 0, 0)\n",
    "date2 = datetime.datetime(2018, 6, 2, 12, 10, 0)\n",
    "diff = date2 - date1\n",
    "\n",
    "print(diff.days * 24 * 3600 + diff.seconds)"
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