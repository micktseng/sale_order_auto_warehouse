from odoo import models, fields

class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
