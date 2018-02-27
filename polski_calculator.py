string = "1+22*(3+4/2-(1+22))/((22+1)/4)"
string2 = "2-4/(3*(4*2-2+3)/2)+4"
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, }
result = 0
stack_of_numbers = []
stack_of_operations = []


def calc(equation):
    step = 0
    try:
        while step < len(equation):
            # print(equation[step]) #ДЛЯ ОТЛАДКИ
            if equation[step].isdigit() == True:
                stack_of_numbers.append(equation[step])
                if equation[step + 1].isdigit() == True:
                    a = str(stack_of_numbers[-1])
                    b = str(equation[step + 1])
                    c = float(a + b)
                    stack_of_numbers[-1] = c
                    step += 1
            elif equation[step] == "(":

                stack_of_operations.append(equation[step])

            elif equation[step] == ")":
                if stack_of_operations[-1] == "(":
                    stack_of_operations.pop()
                else:
                    a = float(stack_of_numbers.pop(-2))
                    b = float(stack_of_numbers.pop())
                    do_operation(a, b, stack_of_operations[-1])
                    step -= 1
            else:
                if len(stack_of_operations) != 0:
                    if stack_of_operations[-1] == "(":
                        stack_of_operations.append(equation[step])
                    elif priority[stack_of_operations[-1]] > priority[equation[step]]:
                        a = float(stack_of_numbers.pop(-2))
                        b = float(stack_of_numbers.pop())
                        do_operation(a, b, stack_of_operations[-1])
                        step -= 1
                    elif priority[stack_of_operations[-1]] == priority[equation[step]]:
                        a = float(stack_of_numbers.pop(-2))
                        b = float(stack_of_numbers.pop())
                        do_operation(a, b, stack_of_operations[-1])
                        step -= 1
                    elif priority[stack_of_operations[-1]] > priority[equation[step]]:
                        stack_of_operations.append(equation[step])

                    else:
                        stack_of_operations.append(equation[step])

                else:
                    stack_of_operations.append(equation[step])

            # print("Шаг {}. Числа: {}".format(step, stack_of_numbers)) #ДЛЯ ОТЛАДКИ!
            # print('Шаг {}. Операции: {}'.format(step, stack_of_operations)) #ДЛЯ ОТЛАДКИ!
            step += 1
        if len(stack_of_operations) != 0:
            # print('Закончили пробег по строке') #ДЛЯ ОТЛАДКИ
            i = 0
            while i < len(stack_of_operations):
                a = float(stack_of_numbers.pop(-2))
                b = float(stack_of_numbers.pop())
                do_operation(a, b, stack_of_operations[-1])

        if len(stack_of_numbers) == 1:
            result = float(stack_of_numbers[0])
        print("\n ОТВЕТ: {}".format(result))

    except ZeroDivisionError:
        print("У тебя там есть деление на ноль. Не порти калькулятор плз")


def do_operation(a, b, sign):
    if sign == "-":
        stack_of_numbers.append(a - b)
        stack_of_operations.pop()
    elif sign == "+":
        stack_of_numbers.append(a + b)
        stack_of_operations.pop()
    elif sign == "/":
        stack_of_numbers.append(a / b)
        stack_of_operations.pop()
    elif sign == "*":
        stack_of_numbers.append(a * b)
        stack_of_operations.pop()


# eq= input('Введите пример: ')
calc(string)
