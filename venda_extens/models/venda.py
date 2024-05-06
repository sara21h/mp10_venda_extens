from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError



class Venda(models.Model):
    _inherit = 'sale.order'

    num_articles = fields.Integer(string="Nombre d'articles", compute='_compute_num_articles', store=True)

    order_count = fields.Integer(compute='_compute_order_count', string='Nombre de comandes pel mateix comercial i mateix estat')
    total_amount = fields.Float(compute='_compute_total_amount', string='Suma total dels imports de les comandes pel mateix comercial i mateix estat')
    correu_preferencial = fields.Char(string='Adreça de correu preferencial')


    @api.depends('user_id', 'state')
    def _compute_order_count(self):
        for record in self:
            same_salesman_state_orders = self.search([('user_id', '=', record.user_id.id), ('state', '=', record.state)])
            record.order_count = len(same_salesman_state_orders)

    @api.depends('user_id', 'state', 'amount_total')
    def _compute_total_amount(self):
        for record in self:
            same_salesman_state_orders = self.search([('user_id', '=', record.user_id.id), ('state', '=', record.state)])
            record.total_amount = sum(order.amount_total for order in same_salesman_state_orders)
            

    @api.depends('order_line')
    def _compute_num_articles(self):
        for order in self:
            order.num_articles = len(order.order_line)


    @api.constrains('correu_preferencial')
    def _check_correu_preferencial(self):
        for order in self:
            if '@' not in order.correu_preferencial:
                raise ValidationError("Introdueix un correu vàlid.")