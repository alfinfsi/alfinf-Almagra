/** @odoo-module **/
console.log("text.esm.js");
import core from "web.core";
import textSignOca from "@sign_oca/elements/text.esm";

const originalGenerate = textSignOca.generate;

textSignOca.generate = function (parent, item, signatureItem) {

    var input = originalGenerate.call(this, parent, item, signatureItem);

    if (item.default_value != '') {
        input.value = parent.info.partner[item.default_value] || "";
        input.setAttribute("readonly", "readonly");
        item.value = parent.info.partner[item.default_value] || "";
    }
    return input;
}
