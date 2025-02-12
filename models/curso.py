# -*- coding: utf-8 -*-
from odoo import fields, models

class Curso(models.Model):
    _name = 'curso.curso'
    _description = "Curso"
    _rec_name = "titulo"

    titulo = fields.Char(string='Título', required=True)
    descripcion = fields.Char(string='Descripción')
    responsable = fields.Many2one(
        comodel_name='hr.employee',
        string='Responsable del curso',
        required=True
    )
    tipo_curso = fields.Selection(
        [
            ('certificaciones', 'Certificaciones'),
            ('prevencion', 'Prevención'),
            ('reciclaje', 'Reciclaje'),
            ('crecimiento_personal', 'Crecimiento personal')
        ],
        string="Tipo de curso",
        default='prevencion',
        required=True,
        help="Elige el tipo de curso deseado."
    )

    _sql_constraints = [
        ('titulo_uniq', 'unique (titulo)', "¡Nombre de curso ya existente!"),
    ]
