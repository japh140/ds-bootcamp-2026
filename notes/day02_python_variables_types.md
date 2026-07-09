# Day 2 — Python Variables, Data Types and Expressions

## 1. Variables

A variable is a name used to store a value.

```python
name = "Japhet"
age = 25
height_m = 1.83
```

The `=` symbol assigns a value to a variable.

```python
patient_count = 120
```

Python reads this as:

> Store the value `120` inside the variable `patient_count`.

### Good variable names

Use clear lowercase names with underscores:

```python
patient_age = 45
mean_glucose = 5.6
sample_is_valid = True
```

Avoid unclear names:

```python
x = 45
thing = 5.6
a = True
```

Variable names:

* cannot contain spaces
* cannot begin with a number
* are case-sensitive
* should describe what the value represents

---

## 2. Strings

A string stores text.

Strings use quotation marks:

```python
patient_name = "Patient A"
sample_id = "SAMPLE_001"
target_role = "Health Data Analyst"
```

Even if a value looks like a number, quotation marks make it a string:

```python
age_text = "25"
```

The value `"25"` is text, not a numerical value.

Check the type:

```python
print(type(age_text))
```

Output:

```text
<class 'str'>
```

---

## 3. Integers

An integer is a whole number.

```python
patient_age = 45
record_count = 500
missing_records = 25
```

Check the type:

```python
print(type(patient_age))
```

Output:

```text
<class 'int'>
```

---

## 4. Floats

A float is a decimal number.

```python
temperature = 37.2
mean_age = 46.7
height_m = 1.83
```

Check the type:

```python
print(type(temperature))
```

Output:

```text
<class 'float'>
```

---

## 5. Booleans

A Boolean represents either:

```python
True
False
```

Examples:

```python
record_is_complete = True
analysis_is_finished = False
```

Booleans are used when checking conditions.

```python
print(type(record_is_complete))
```

Output:

```text
<class 'bool'>
```

The capital letters matter.

Correct:

```python
True
False
```

Incorrect:

```python
true
false
```

---

## 6. None

`None` represents the absence of a value.

```python
follow_up_date = None
```

It means the variable currently has no meaningful value.

`None` is different from:

```python
0
""
False
```

Those are actual values.

Check the type:

```python
print(type(follow_up_date))
```

Output:

```text
<class 'NoneType'>
```

---

## 7. Checking Data Types

Use `type()` to check the type of a value.

```python
patient_id = "P001"
patient_age = 42
temperature = 37.5
record_complete = True
follow_up_date = None

print(type(patient_id))
print(type(patient_age))
print(type(temperature))
print(type(record_complete))
print(type(follow_up_date))
```

---

## 8. Arithmetic Operators

Python can perform mathematical calculations.

```python
a = 12
b = 5
```

### Addition

```python
print(a + b)
```

Output:

```text
17
```

### Subtraction

```python
print(a - b)
```

Output:

```text
7
```

### Multiplication

```python
print(a * b)
```

Output:

```text
60
```

### Division

```python
print(a / b)
```

Output:

```text
2.4
```

### Floor division

```python
print(a // b)
```

Output:

```text
2
```

Floor division removes the decimal part and rounds down.

### Remainder

```python
print(a % b)
```

Output:

```text
2
```

The `%` operator returns the remainder.

### Power

```python
print(a ** b)
```

This means:

```text
12 to the power of 5
```

---

## 9. Operator Precedence

Python follows the normal order of operations:

1. Parentheses
2. Powers
3. Multiplication and division
4. Addition and subtraction

Example:

```python
result_one = 2 + 3 * 4
result_two = (2 + 3) * 4

print(result_one)
print(result_two)
```

Output:

```text
14
20
```

Parentheses change the order of the calculation.

---

## 10. Type Conversion

Type conversion changes a value from one type into another.

### String to integer

```python
age_text = "25"
age_number = int(age_text)

print(age_number + 5)
```

Output:

```text
30
```

### String to float

```python
temperature_text = "37.5"
temperature_number = float(temperature_text)

print(temperature_number + 0.5)
```

Output:

```text
38.0
```

### Integer to string

```python
age = 25
age_text = str(age)

print("Age: " + age_text)
```

Common conversion functions:

```python
int()
float()
str()
bool()
```

Not every string can become a number.

This works:

```python
int("25")
```

This fails:

```python
int("twenty-five")
```

---

## 11. Input

`input()` collects information from the user.

```python
name = input("What is your name? ")
print(name)
```

Important:

`input()` always returns a string.

```python
age = input("What is your age? ")
print(type(age))
```

Even if the user types `25`, Python stores it as `"25"`.

To perform calculations, convert it:

```python
age = int(input("What is your age? "))
print(age + 1)
```

---

## 12. Comparison Operators

Comparisons return either `True` or `False`.

```python
age = 25
```

### Equal to

```python
print(age == 25)
```

### Not equal to

```python
print(age != 25)
```

### Greater than

```python
print(age > 18)
```

### Less than

```python
print(age < 30)
```

### Greater than or equal to

```python
print(age >= 25)
```

### Less than or equal to

```python
print(age <= 25)
```

Comparison operators:

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

Do not confuse assignment with comparison:

```python
age = 25
```

This assigns a value.

```python
age == 25
```

This checks whether the value equals `25`.

---

## 13. Boolean Operators

Boolean operators combine conditions.

### and

Both conditions must be true.

```python
has_python = True
has_sql = False

print(has_python and has_sql)
```

Output:

```text
False
```

### or

At least one condition must be true.

```python
print(has_python or has_sql)
```

Output:

```text
True
```

### not

Reverses a Boolean value.

```python
print(not has_sql)
```

Output:

```text
True
```

Health-data example:

```python
has_patient_id = True
has_measurement = True

record_is_usable = has_patient_id and has_measurement

print(record_is_usable)
```

---

## 14. F-Strings

F-strings allow variables to be inserted into text.

```python
name = "Japhet"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

Calculations can also appear inside braces:

```python
applications_sent = 3
weekly_target = 5

print(f"Applications remaining: {weekly_target - applications_sent}")
```

### Decimal formatting

```python
mean_age = 46.7284

print(f"Mean age: {mean_age:.2f}")
```

Output:

```text
Mean age: 46.73
```

The `.2f` displays the value to two decimal places.

---

## 15. Common Errors

### Mixing strings and integers

Incorrect:

```python
age = 25
print("Age: " + age)
```

Correct using conversion:

```python
print("Age: " + str(age))
```

Better using an f-string:

```python
print(f"Age: {age}")
```

### Invalid variable names

Incorrect:

```python
patient age = 45
```

Correct:

```python
patient_age = 45
```

### Incorrect Boolean spelling

Incorrect:

```python
record_complete = true
```

Correct:

```python
record_complete = True
```

---

## 16. Key Differences to Remember

```text
"25" = string
25 = integer
25.0 = float
True = Boolean
None = no value
```

```text
= assigns a value
== compares two values
```

```text
/ performs normal division
// performs floor division
% returns the remainder
** calculates a power
```

```text
input() always returns a string
```

---

## 17. Day 2 Mastery Questions

I should be able to answer:

1. What is a variable?
2. What is the difference between `"25"` and `25`?
3. What is the difference between an integer and a float?
4. What does a Boolean represent?
5. What does `None` mean?
6. What does `type()` do?
7. What is the difference between `/` and `//`?
8. What does `%` return?
9. Why is type conversion needed?
10. What is the difference between `=` and `==`?
11. What do `and`, `or` and `not` do?
12. Why are f-strings useful?
13. What type does `input()` return?
14. How can a string be converted into an integer?
