# Copyright 2024 Pablo Martín - Alfinf
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Alfinf Almagra contratos",
    "summary": "Alfinf Almagra contratos",
    "version": "16.0.1.0.0",
    "development_status": "Beta",
    "license": "AGPL-3",
    "author": "Alfinf",
    "website": "https://github.com/alfinfsi/",
    "category": "Connector",
    "assets": {
        "web.assets_backend": [
            "alfinf_contract/static/src/elements/text.esm.js",
        ],
        "web.assets_frontend": [
            "alfinf_contract/static/src/elements/text.esm.js",
        ],
    },
    "depends": [
        "sign_oca",
    ],
    "data": [
        "views/sign_oca_field_view.xml",
    ],
    "installable": True,
}
