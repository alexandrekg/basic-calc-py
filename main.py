def main():
    print('What can you do?')
    print('| 7 | 8 | 9 | +')
    print('| 4 | 5 | 6 | -')
    print('| 1 | 2 | 3 | x')
    print('| . | 0 |   | /')

    while True:
        expression = input('Write your expression: ')
        operators_validator = [True if i in expression else False for i in ['+', '-', 'x', '/']]

        if not any(operators_validator):
            print('Your expression does not have an operator.')
            return False

        print(expression)
        option = input('Is this result what you are expecting?  (y/n)')
        if option in ['yes', 'y', 'no', 'n']:
            return False


if __name__ == "__main__":
    main()