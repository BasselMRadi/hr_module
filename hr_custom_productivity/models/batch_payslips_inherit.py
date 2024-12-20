from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    @api.model
    def get_productivity_for_month(self, employee_id):
        employee = self.env['hr.employee'].browse(employee_id)
        if not employee.exists():
            return 0  # أو يمكنك إثارة استثناء

        start_date = fields.Date.today().replace(day=1)
        end_date = start_date + relativedelta(months=1, days=-1)

        attendance_records = self.env['hr.attendance'].search([
            ('employee_id', '=', employee_id),
            ('check_in', '>=', start_date),
            ('check_in', '<=', end_date)
        ])
        return sum(record.daily_production for record in attendance_records)
