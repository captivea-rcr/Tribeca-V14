# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'CAP Purchase',
    'version': '1.0',
    'category': 'Website',
    'summary': 'This is used for add new state in the purchase order and Also used for update portal '
               'domains now visible all the orders they have not in draft and cancel state.',
    'description': """
This is used for add new state in the purchase order and Also used for update portal domains now visible 
all the orders they have not in draft and cancel state.
======================================
This is used for add new state in the purchase order.
This module is also updates the portal controller to view a all the order they not have in draft and cancel.
    """,
    'depends': ['purchase'],
    'data': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
