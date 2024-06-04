
from odoo import fields, models

class SurveyQuestion(models.Model):
    _inherit = "survey.question"

    field_id = fields.Many2one('ir.model.fields', string='Field', domain="[('model_id.model', '=', 'res.partner')]")
