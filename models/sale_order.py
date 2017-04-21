from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('carrier_id')
    def _onchange_carrier(self):
        if self.carrier_id.warehouse_id:
            self.warehouse_id = self.carrier_id.warehouse_id
        else:
            self.warehouse_id = self.default_get(['warehouse_id'])['warehouse_id']