# Copyright 2024 Pablo Martín López - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class SignOcaRequestSigner(models.Model):
    # Herencia del modelo sign.oca.request.signer
    _inherit = 'sign.oca.request.signer'

    #* El diccionario de partner contiene los valores por defecto de los campos, para hacer referecia
    #* a ellos tienes que cambiar el valor por defecto en el campo

    def get_info(self, access_token=False):
        self.ensure_one()
        self._set_action_log("view", access_token=access_token)
        return {
            "role_id": self.role_id.id if not self.signed_on else False,
            "name": self.request_id.template_id.name,
            "items": self.request_id.signatory_data,
            "to_sign": self.request_id.to_sign,
            "partner": {
                "id": self.partner_id.id,
                "name": self.partner_id.name,
                "email": self.partner_id.email,
                "phone": self.partner_id.phone,
                "mobile": self.partner_id.mobile,
                "calle": self.partner_id.street,
                "numero": self.partner_id.street2,
                "provincia": self.partner_id.state_id.name,
                "pais": self.partner_id.country_id.name,
                "ciudad": self.partner_id.city,
                "cif": self.partner_id.vat,
                "company_name": self.partner_id.company_name,
                "fecha": self.create_date.strftime("%d de %B del %Y"),
            },
        }
