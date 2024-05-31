# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).



class Survey(models.Model):
    _inherit = "survey.survey"

    forUser = fields.Boolean('Para usuario', default=False)
