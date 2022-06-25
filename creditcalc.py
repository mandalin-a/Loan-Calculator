import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=float)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)
args = parser.parse_args()
args2 = sys.argv
negative_check = [args.principal, args.periods, args.interest, args.payment]
all_arguments = [args.type, args.principal, args.periods, args.interest, args.payment]

def calculate_periods():
    i = args.interest / (12 * 100)
    p_number = math.ceil(math.log((args.payment / (args.payment - (i * args.principal))), (1 + i)))
    overpayment = (p_number * args.payment) - args.principal
    if p_number < 12:
        result = f'It will take {p_number} month to repay this loan!\nOverpayment = {int(overpayment)}'
    elif p_number % 12 == 0:
        result = f'It will take {p_number // 12} years to repay this loan!\nOverpayment = {int(overpayment)}'
    else:
        result = f'It will take {p_number // 12} years and {p_number % 12} months to repay this loan!\nOverpayment = {int(overpayment)}'
    return print(result)


def calculate_annuity():
    i = args.interest / (12 * 100)
    annuity = math.ceil(args.principal * ((i * (math.pow((1 + i), args.periods))) / (math.pow((1 + i), args.periods) - 1)))
    overpayment = (args.periods * annuity) - args.principal
    result = f'Your annuity payment = {annuity}!\nOverpayment = {int(overpayment)}'
    return print(result)


def calculate_loan():
    i = args.interest / (12 * 100)
    loan = args.payment / ((i * (math.pow((1 + i), args.periods))) / (math.pow((1 + i), args.periods) - 1))
    overpayment = (args.periods * args.payment) - loan
    result = f'Your loan principal = {math.floor(loan)}!\nOverpayment = {math.ceil(overpayment)}'
    return print(result)


def calculate_differentiated():
    i = (args.interest / 100) / 12
    counter = args.periods
    current_month = 1
    total_payment = 0
    while counter > 0:
        counter -= 1
        payment = math.ceil((args.principal / args.periods) + i * (args.principal - (args.principal * (current_month - 1)) / args.periods))
        total_payment += payment
        print(f'Month {current_month}: payment is {payment}')
        current_month += 1
    overpayment = total_payment - args.principal
    print(f'Overpayment = {math.ceil(overpayment)}')


if len(args2) < 4:
    print("Incorrect parameters")
elif any(a is not None and a < 0 for a in negative_check):
    print("Incorrect parameters")
elif sum(a is not None for a in all_arguments) < 4:
    print("Incorrect parameters")
else:
    if args.type == "annuity":
        if args.payment is None:
            calculate_annuity()
        elif args.principal is None:
            calculate_loan()
        elif args.periods is None:
            calculate_periods()
    elif args.type == "diff":
        calculate_differentiated()
    else:
        print("Incorrect parameters")
