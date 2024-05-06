{
    "name": "venda_extens",
    "version": "16.0.0",
    "application": True,
    "depends": ["base", "mail", "sale", 'account', 'stock'],
    "data": [
        'security/ir.model.access.csv',
        'views/venda.xml',
        'report/sale_order_report.xml',
        'report/report.xml',

    ],
    "installable": True,
    'license': 'LGPL-3',
}
