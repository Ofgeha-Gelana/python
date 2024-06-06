{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a0dfd5f1-df26-4082-bd84-993369254c88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter city name: mumbai\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mumbai is in india\n"
     ]
    }
   ],
   "source": [
    "# 1 answer\n",
    "\n",
    "# a answer\n",
    "\n",
    "india = [\"mumbai\", \"banglore\", \"chennai\", \"delhi\"]\n",
    "pakistan = [\"lahore\",\"karachi\",\"islamabad\"]\n",
    "bangladesh = [\"dhaka\", \"khulna\", \"rangpur\"]\n",
    "city_name = input(\"Enter city name:\")\n",
    "if city_name in india:\n",
    "    print(f\"{city_name} is in india\")\n",
    "elif city_name in pakistan:\n",
    "    print(f\"{city_name} is in pakistan\")\n",
    "elif city_name in bangladesh:\n",
    "    print(f\"{city_name} is in bangladesh\")\n",
    "else:\n",
    "    print(\"NONE\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "047729ba-2542-497f-8d3c-8a1ccc1f43cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter city one: dhaka\n",
      "Enter city two: khulna\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Both countries are in bangladesh\n"
     ]
    }
   ],
   "source": [
    "# b answer\n",
    "city_one = input(\"Enter city one:\")\n",
    "city_two = input(\"Enter city two:\")\n",
    "if (city_one in india) and (city_two in india):\n",
    "    print(\"Both countries are in India\")\n",
    "elif (city_one in pakistan) and (city_two in pakistan):\n",
    "    print(\"Both countries are in pakistan\")\n",
    "elif (city_one in bangladesh) and (city_two in bangladesh):\n",
    "    print(\"Both countries are in bangladesh\")\n",
    "else:\n",
    "    print(\"They don't belong to same country\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cae86b79-2fd9-43e5-ba31-8ff524f9891f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter fasting sugar level 111\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It is high\n"
     ]
    }
   ],
   "source": [
    "# 2 ANSWER\n",
    "\n",
    "fasting_sugar_level = int(input(\"enter fasting sugar level\"))\n",
    "if fasting_sugar_level >=80 and fasting_sugar_level <=100:\n",
    "    print(\"It is normal\")\n",
    "elif fasting_sugar_level < 80:\n",
    "    print(\"It is low\")\n",
    "else:\n",
    "    print(\"It is high\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
