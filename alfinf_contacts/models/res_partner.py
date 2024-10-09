# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    id_rep = fields.Many2one(
        'res.partner',
        string='Representative',
        # domain="[('is_company', '=', False)]"
    )