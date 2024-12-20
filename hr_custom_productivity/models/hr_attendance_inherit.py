from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    daily_production = fields.Integer(string="Daily Production", default=0)
    production_range_id = fields.Many2one('production.range', string="Production Range")
    daily_wage = fields.Float(string="Daily Wage", compute="_compute_daily_wage", store=True)

    @api.constrains('daily_production', 'production_range_id')
    def _check_production_within_range(self):
        for record in self:
            if record.production_range_id:
                if not (
                        record.production_range_id.min_qty <= record.daily_production <= record.production_range_id.max_qty):
                    raise ValidationError(
                        f"Daily production {record.daily_production} is out of range "
                        f"[{record.production_range_id.min_qty} - {record.production_range_id.max_qty}]."
                    )

    # Check if daily production is a positive integer
    @api.constrains('daily_production')
    def _check_daily_production(self):
        for record in self:
            if record.daily_production < 0:
                raise ValidationError("The daily production cannot be negative.")
