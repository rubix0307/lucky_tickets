import time
from typing import List

import numpy as np


def is_lucky(number: List[int]) -> bool:
    if not len(number) % 2:
        part = int(len(number) / 2)

        return sum(number[:part]) == sum(number[part:])
    else:
        return False

def get_count_lucky(tickets, results):
    check = []

    for ticket in tickets:
        answer = is_lucky(ticket)
        if answer:
            check.append(answer)

    count_lucky = sum(check)
    results.append(count_lucky)
    return count_lucky

def split_tickets(number, ticket_length):
    answer = [int(digit) for digit in str(number).zfill(ticket_length)]
    return answer

def create_ticket_groups(max_ticket_quantity, ticket_length, split=1):

    start_ticket = 0
    end_ticket = (10 ** (ticket_length - int(ticket_length/10))) - 1

    tickets = [split_tickets(number, ticket_length) for number in range(start_ticket, end_ticket + 1)[:max_ticket_quantity]]

    ticket_groups = []
    len_slice = int(len(tickets) / split)
    for n, part in enumerate(range(split), start=1):

        start = len_slice * part if part else 0
        stop = len_slice * (part + 1)

        if n == split:
            tickets_slice = tickets[start:]
        else:
            tickets_slice = tickets[start:stop]

        ticket_groups.append(tickets_slice)

    return ticket_groups

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)
        print(f'[Execution time <{args[0].__name__}>] - {execution_time}s')
        return result
    return wrapper