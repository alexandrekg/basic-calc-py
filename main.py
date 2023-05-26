
class Calculator:
    def main(self):
        print('What can you do?')
        print('| 7 | 8 | 9 | +')
        print('| 4 | 5 | 6 | -')
        print('| 1 | 2 | 3 | x')
        print('| . | 0 |   | /')

        self.controller()

    def controller(self):
        if getattr(self, 'result', False):
            result_expression = input(f'What do you want to do with the result? {self.result} ')
            self.expression = f'{self.result} {result_expression}'
        else:
            self.expression = input('Write your expression (Ex: n1 + n2/3 + 3):  ')

        validator = self.operators_validator()
        if not any(validator):
            print('Your expression does not have an operator.')
            return False

        n1, operator, n2 = self.expression.split(' ')
        self.calc(int(n1), int(n2), operator)
        print(f'Result of {self.expression} is: {self.result}')

        self.controller()

    def calc(self, n1, n2, operator):
        if operator == '/':
            self.result = int(n1 / n2)
        elif operator == '+':
            self.result = int(n1 + n2)
        elif operator == '-':
            self.result = int(n1 - n2)
        elif operator in ['*', 'x']:
            self.result = int(n1 * n2)

    def operators_validator(self):
        return [True if i in self.expression else False for i in ['+', '-', 'x', '/']]


if __name__ == "__main__":
    Calculator().main()
