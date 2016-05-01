#!/usr/bin/env python

import os

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

import json
import sys

from pinpayments import PinPayments
from pinpayments.exceptions import PinPaymentsException

api_secret = os.environ.get('PIN_API_SECRET')

pin = PinPayments(api_secret = api_secret, test = True)

try:
    customers = pin.getCustomers()
    for customer in customers.get('response'):
        print("{}: {}".format(customer['token'],customer['email']))
        print("Card: {} ({})".format(customer['card']['display_number'], customer['card']['token']))
except PinPaymentsException as e:
    print(e.msg)
