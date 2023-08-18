

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for i in problems:
        operand1, symbol, operand2 = i.split()

        if symbol not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isnumeric() or not operand2.isnumeric():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(operand1), len(operand2))

        first_line = first_line + operand1.rjust(max_length + 2) + "    "
        second_line = second_line + symbol + " " + operand2.rjust(max_length) + "    "
        dash_line = dash_line + "-" * (max_length + 2) + "    "

        if show_answers:
            if symbol == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answer_line = answer_line + answer.rjust(max_length + 2) + "    "

    arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dash_line.rstrip()
    if show_answers:
        arranged_problems = arranged_problems + "\n" + answer_line.rstrip()

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))