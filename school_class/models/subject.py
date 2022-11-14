# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Subject(models.Model):
    _name = 'subject'
    _description = 'School Subject'

    name = fields.Char('Subject Name')
    description = fields.Text('Subject description')
    active = fields.Boolean('Active', default=True)
