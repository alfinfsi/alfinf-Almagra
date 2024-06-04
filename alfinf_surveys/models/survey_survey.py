# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import string
from odoo import fields, models

class SurveySurvey(models.Model):
    _inherit = "survey.survey"

    foruser = fields.Boolean(string="For User", default=False)


