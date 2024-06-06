# Copyright 2024 Pablo Martín López - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class SurveyQuestion(models.Model):
    _inherit = "survey.question"

    field_id = fields.Many2one('ir.model.fields', string='Field', domain="[('model_id.model', '=', 'res.partner')]")
