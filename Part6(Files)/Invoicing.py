import datetime
from os import SEEK_SET
from typing import TextIO


def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    year, number = invoice_number.split('-')
    return int(year), int(number)


def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """


def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float) -> None:
    """Create a new invoice number, and write it to a file on disk.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    """


# Test code:
current_year = get_year()
test_data = [
    ('2019-0005', (2019, 5), f'{current_year}-0001'),
    (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
    (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
    (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
]

for test_string, result, next_number in test_data:
    parts = parse_invoice_number(test_string)
    if parts == result:
        print(f'{test_string} parsed successfully')
    else:
        print(f'{test_string} failed to parse. Expected {result} got {parts}')

    new_number = next_invoice_number(test_string)
    if next_number == new_number:
        print(f'New number {new_number} generated correctly for {test_string}')
    else:
        print(f'New number {new_number} is not correct for {test_string}')

    print('-' * 80)

