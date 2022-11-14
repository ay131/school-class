# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Subject'

    name = fields.Char('Class Name', copy=False, readonly=True, default=lambda x: _('New'))
    subject_id = fields.Many2one('subject', string='Subject')
    country_id_teacher = fields.Many2one('res.country', related='teacher_id.country_id',stor=True)
    student_id = fields.Many2one('res.partner', string='Student', domain=[('is_student', '=', True)])
    teacher_id = fields.Many2one('res.partner', string='Teacher',
                                 domain=[('is_teacher', '=', True)])

    active = fields.Boolean('Active', default=True)
    # ,('country_id','=','country_id_student')
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            subject = self.env['subject'].browse(vals.get('subject_id')).name
            vals['name'] = _('%s-%s-%s', subject, fields.Date.today().year, fields.Date.today().month)
        res = super(SchoolClass, self).create(vals)
        return res
    @api.onchange('teacher_id')
    def _onchange_data(self):
        print(self.teacher_id.country_id)