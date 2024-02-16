from odoo import models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    medical_registration_number = fields.Char(string='Medical Registration Number', required=True)
    portadadoc = fields.Image(string="Docto Photo", max_width=130, max_height=130)
    patients = fields.Many2many('hospital.patient', string='Patients')