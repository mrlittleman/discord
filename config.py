from odoo import models, fields
class config(models.Model):
    _name='car.inventory'
    _description='Car Inventory'
    carModel=fields.Char('Model', Required=True)
    carQuantity=fields.Integer('Quantity', Required=True)
    carStatus=fields.Char('Status', Required=True)
    carPrice=fields.Float('Price', Required=True)

