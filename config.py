from typing_extensions import Required
from odoo import models, fields
class config(models.Model):
    _name='Car Inventory'
    _description='Car Inventory'
    carModel=fields.Char('Model', Required=True)
    carQuantity=fields.Integer('Quantity', Required=True)
    carStatus=fields.Char('Status', Required=True)
    carPrice=fields.Float('Price', Required=True)


    # confname=fields.Char('ConfName' , Required=True)
    # indexed=fields.Boolean('Indexed ?', Required=True)
    # startdate=fields.Date('Start Date', Required=True)
    # enddate=fields.Date('End Date', Required=True)    
    # fee=fields.Float('Registration Fee', Required=True)
    