from odoo import models, fields

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    bono = fields.Float(string='Bono')