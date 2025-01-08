from odoo import api, fields, models



class TotalLines(models.Model):
    _inherit = 'sale.order'
    _description = "Total Quantity"

    total_lines_qty = fields.Float(string="Total Quantity", compute="_compute_total_qty",store=True)

    @api.depends('order_line.product_uom_qty')
    def _compute_total_qty(self):
        for rec in self:
            rec.total_lines_qty = sum(rec.order_line.mapped('product_uom_qty'))
