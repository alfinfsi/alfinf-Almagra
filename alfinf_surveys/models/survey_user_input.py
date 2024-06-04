
from odoo import fields, models

class SurveyUserInput(models.Model):
    _inherit = "survey.user_input"


    def _mark_done(self):

        if self.survey_id.foruser:

            # Contruir diccionrio
            data = {}

            for line in self.user_input_line_ids:
                if line.question_id.field_id:

                    if line.answer_type == 'text_box':
                        value = line.value_text_box
                    elif line.answer_type == 'char_box':
                        value = line.value_char_box
                    elif line.answer_type == 'numerical_box':
                        value = line.value_numerical_box
                    elif line.answer_type == 'date':
                        value = line.value_date
                    elif line.answer_type == 'datetime':
                        value = line.value_datetime
                    elif line.answer_type == 'suggestion':
                        value = line.suggested_answer_id.id

                    data[line.question_id.field_id.name] = value


            # Modify survey name

            self.partner_id.write(data)


        super(SurveyUserInput, self)._mark_done()


