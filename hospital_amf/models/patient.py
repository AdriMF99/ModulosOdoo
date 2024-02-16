from odoo import models, fields

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    symptoms = fields.Text(string='Symptoms')
    portadapat = fields.Image(string="Patient Photo", max_width=130, max_height=130)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')