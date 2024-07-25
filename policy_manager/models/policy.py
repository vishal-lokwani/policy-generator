from odoo import models, fields, api
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)


class PolicyManager(models.Model):
    _name = 'policy.manager'
    _description = 'Policy Manager'

    company_name = fields.Char('Company Name', required=True)
    company_website = fields.Char('Company Website')    
    address = fields.Text('Address')
    city = fields.Char('City')
    state = fields.Char('State')
    country = fields.Char('Country')
    zip_code = fields.Char(string='ZIP Code', size = 9, required=True)
    contact_details = fields.Char('Contact Details')
    policy_text = fields.Text('Policy Text')
    email = fields.Char(string='Email', required=True)


    @api.constrains('zip_code')
    def _check_zip_code(self):
        for record in self:
            if not record.zip_code.isdigit() or len(record.zip_code) != 9:
                raise ValidationError("The ZIP Code must be exactly 9 digits long.")
            
    def action_view_policy(self):            
        return {
            'type': 'ir.actions.act_url',
            'url': '/policy/view/%s' % self.id,
            'target': 'new',
        }
    
    

