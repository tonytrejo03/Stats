# Tony Trejo
# statistics with list of numbers


from num_func import print_numbers, build_random_number_list, find_min, find_max, find_sum, find_mean, double_numbers


def print_menu():
    print("Here are your choices: ")
    print("1. Find min")
    print("2. Find max")
    print("3. Find sum")
    print("4. Find mean")
    print("5. Double the numbers")
    print("6. Print the numbers")
    print("7. Quit")
    
# main

num_count = int(input("How many numbers do you want: "))
cap = int(input("How large a number should I be able to generate? "))
numbers = build_random_number_list(num_count,cap)

choice = 0
while choice != 7:
    print_menu()
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        min_num = find_min(numbers)
        print("The minimum is %d." % min_num)
    elif choice == 2:
        max_num = find_max(numbers)
        print("The max is %d." % max_num)
    elif choice == 3:
        total = find_sum(numbers)
        print("The total is %d." % total)
    elif choice == 4:
        mean = find_mean(numbers)
        print("The mean is %d." % mean)
    elif choice == 5:
        double_numbers(numbers)
        print_numbers(numbers)
    elif choice == 6:
        print_numbers(numbers)
print("Good bye")
