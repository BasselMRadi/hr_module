from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductionRange(models.Model):
    _name = 'production.range'
    _description = 'Production Range'

    name = fields.Char(string='Range Name', required=True)
    min_qty = fields.Integer(string='Minimum Quantity', required=True)
    max_qty = fields.Integer(string='Maximum Quantity', required=True)
    rate_per_piece = fields.Float(string='Rate Per Piece', required=True)
    department_id = fields.Many2one('hr.department', string='Department', ondelete='cascade')
    range_size = fields.Float(string='Range Size', compute='_compute_range_size')

    # department_id = fields.Many2one('hr.department', string='Department')
    @api.constrains('min_qty', 'max_qty')
    def _check_min_max_qty(self):
        for record in self:
            if record.min_qty < 0 or record.max_qty < 0:
                raise ValidationError("Quantities cannot be negative.")
            if record.min_qty >= record.max_qty:
                raise ValidationError("Minimum quantity must be less than maximum quantity.")

    @api.depends('min_qty', 'max_qty')
    def _compute_range_size(self):
        for record in self:
            # Example logic for calculating range_size
            if record.min_qty and record.max_qty:
                record.range_size = record.max_qty - record.min_qty
            else:
                record.range_size = 0
