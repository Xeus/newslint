import math
from colorama import Fore, Style

def report(result, opts):
    opts = opts if opts != None else {}
    log_heading('Newslint')
    if (result.is_clean()):
        log_success()
    if (result.has_fail_points()):
        log_fail_charts(result.fail_points)
    print
    if (result.has_messages()):
        log_messages('error', 'red', opts['verbose'], result.errors)
        log_messages('warning', 'yellow', opts['verbose'], result.warnings)
        log_messages('notice', 'grey', opts['verbose'], result.notices)
    print


def log_heading(heading):
    print
    print(Fore.CYAN + 'Joblint')

def log_success():
    print(Fore.GREEN + 'No issues found with the job spec!')

def log_fail_charts(points):
    data_set = [
        {'label': 'Culture', 'value': points['culture']},
        {'label': 'Realism', 'value': points['realism']},
        {'label': 'Recruiter', 'value': points['recruiter']},
        {'label': 'Tech', 'value': points['tech']}
    ]
    max_label_length = max_val(len(datum['label']) for datum in data_set)

    max_value = max_val(datum['value'] for datum in data_set)

    for datum in data_set:
        log_fail_chart(datum['label'], max_label_length, datum['value'], max_value)

def log_fail_chart(label, max_label_length, value, max_value):
    full_label = label + ' Issues';
    bar = ''
    for i in range(int(math.ceil(value))):
        bar += '%'
    num = '(' + str(int(value)) + ')'
    print(Style.NORMAL + Fore.WHITE + full_label + ' ' * (max_label_length - len(full_label) + 15) + Fore.WHITE + Style.DIM + '|' + Style.NORMAL + Fore.YELLOW + bar + ' ' * (10 - len(bar)) + Fore.WHITE + Style.DIM + num)

def max_val(arr):
    return max(arr)

def log_messages(type_cat, color, verbose, messages):
    for msg in messages:
        log_message(type_cat, color, verbose, msg)

def log_message(type_cat, color, verbose, message):
    if color == 'yellow':
        current_color = Fore.YELLOW + Style.NORMAL
    elif color == 'red':
        current_color = Fore.RED + Style.NORMAL
    elif color == 'grey':
        current_color = Fore.WHITE + Style.DIM
    print(current_color + '* ' + message['message'] + Fore.WHITE + Style.DIM + ' (' + type_cat + ')')
    if (verbose):
        print(Fore.WHITE + Style.DIM + message['detail'])
