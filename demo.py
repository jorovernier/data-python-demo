first_name = 'Joely'
print(first_name)

last_name = "Vernier"
print(last_name)

age = 21 # int
bank_account = 435.34 # float
loves_code = True # boolean

# age = 'twenty one'
# print(age)
print(type(age))

if age >= 21 or first_name == 'Steve':
    print('Your favorite flavor of Smirnoff Ice is green apple.')

if age >= 18:
    print('I am an adult!')
elif age >= 13:
    print('I am a teen.')
else:
    print('I am a child.')

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    print(number)

for idx, val in enumerate(numbers):
    print(numbers[0])

my_cats = ['jake', 'buddy', 'gogi', 'macy']

for cat in my_cats:
    print(cat.capitalize())

print(len(my_cats))


open_file = open('FinalGrades.csv')

for row in open_file:
    print(row)

open_file.seek(0,0)

for row in open_file:
    split = row.split(',')
    for value in split:
        if value.startswith('J'):
            print(value)

open_file.seek(0,0)

total_a = 0
total_b = 0
total_c = 0

for row in open_file:
    item = row.rstrip('\n').split(',')
    for value in item:
        if value == 'A':
            total_a += 1
        elif value == 'B':
            total_b += 1
        elif value == "C":
            total_c += 1

print("A's: ", total_a)
print("B's: ", total_b)
print("C's: ", total_c)

open_file.close()