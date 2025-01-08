# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Total Quantity Of Lines',
    'version': '1.1',
    'summary': 'Compute sum quantity of sale order lines',
    'sequence': 10,
    'description': "Compute sum quantity of sale order lines",
    'category': 'Sales',
    'author': 'Omar Shaaban',
    'images': [],
    'depends': ['base', 'sale', 'sale_management'],
    'data': ['secuirty/ir.model.access.csv',
             'views/total_of_lines_view.xml'
             ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
