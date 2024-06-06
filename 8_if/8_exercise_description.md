{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5b45b46e-60c8-435b-ab06-8ba254645ca7",
   "metadata": {},
   "source": [
    "1. Using following list of cities per country,\r\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "6af951a8-a946-4850-aece-a71076f77344",
   "metadata": {},
   "source": [
    "india = [\"mumbai\", \"banglore\", \"chennai\", \"delhi\"]\n",
    "pakistan = [\"lahore\",\"karachi\",\"islamabad\"]\n",
    "bangladesh = [\"dhaka\", \"khulna\", \"rangpur\"]\n",
    "\n",
    "i. Write a program that asks user to enter a city name and it should tell which country the city belongs to\n",
    "ii. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print \"Both cities are in India\" but if I enter mumbai and dhaka it should print \"They don't belong to same country\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63011725-7519-4a3f-b59b-db4a39600007",
   "metadata": {},
   "source": [
    "2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.\n",
    " - Ask user to enter his fasting sugar level\n",
    " - If it is below 80 to 100 range then print that sugar is low\n",
    " - If it is above 100 then print that it is high otherwise print that it is normal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8b22e249-ffe2-49a0-8dd6-92aeb4b50f4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter city name: dhaka\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dhaka is in bangladesh\n"
     ]
    },
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
    "    print(\"NONE\")\n",
    "\n",
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
   "execution_count": 8,
   "id": "610b3f13-97b7-4c96-93ba-176b653dc00c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter fasting sugar level 102\n"
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
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2044280e-e819-45d1-9d71-e27a44bbc4d2",
   "metadata": {},
   "outputs": [],
   "source": []
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
