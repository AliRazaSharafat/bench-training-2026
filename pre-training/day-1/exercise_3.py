def generate_table(number):
    for counter in range(1,11):
        print(f"      {number} * {counter} = {number * counter}")

while True:
    number = int(input("Enter a number to print its table: "))
    if 1 <= number <= 12:
        generate_table(number)
        break
    else:
        print("Please enter a number between 1 and 12. Try again.")

print("""

    Generating table for number 1-12
    
""")

for i in range(1,13):
    print("Table for number ", i, ":")
    generate_table(i)
