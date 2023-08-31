from threading import Thread
from multiprocessing import Process, Manager
from typing import Union

from functions import get_count_lucky, create_ticket_groups, timing_decorator


@timing_decorator
def main(task: Union[Thread, Process], ticket_groups):

    tasks = []
    results = Manager().list()
    for group in ticket_groups:
        tasks.append(task(target=get_count_lucky, args=[group, results]))

    for t in tasks:
        t.start()

    for t in tasks:
        t.join()

    lucky_tickets = sum(results)
    return dict(
        lucky_tickets=lucky_tickets,
        lucky_ticket_percentage=round((lucky_tickets / ticket_quantity) * 100, 3),
    )


if __name__ == '__main__':
    ticket_quantity = 1_000_000
    ticket_groups = create_ticket_groups(ticket_quantity, ticket_length=6, split=4)

    answer1 = main(Thread, ticket_groups)
    answer2 = main(Process, ticket_groups)

    # [Execution time <Thread>] - 0.93s
    # [Execution time <Process>] - 2.05s