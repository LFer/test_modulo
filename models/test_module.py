from openerp import models, fields, _, api, exceptions
import ipdb as pdb
import datetime
from datetime import timedelta,date
import math
from qrcode import *
import tempfile
import base64

class test_module(models.Model):
    _name='test.module'


    #Campos que voy a meter en el qr
    alumno = fields.Many2one(comodel_name='res.partner', string='Alumno')
    nacimiento = fields.Date(string='Fecha de Nacimiento')
    comentarios = fields.Char(string='Comentarios')

    cfdi_cbb =  fields.Binary('CFD-I CBB')
    img =  fields.Binary("img")

    """
    @api.one
    def _get_same_image(self):
        #pdb.set_trace()
        if self.cfdi_cbb:
            self.img = self.cfdi_cbb
    """
    """
    @api.one
    @api.model
    def get_qr(self):
        #pdb.set_trace()
        if self.alumno:
            qr_string = ""
            nombre = 'Nombre: ' + self.alumno.name
            nacimiento = 'Fecha de Nacimiento: ' + self.nacimiento
            direccion = 'Direccion: ' + self.alumno.street
            telefono = 'telefono:' + self.alumno.phone
            comentarios = 'Comentarios:' + self.comentarios

            qr_string = nombre + '\n' + nacimiento + '\n' + direccion + '\n' + telefono + '\n'+ comentarios
            qr = QRCode(version=1, error_correction=ERROR_CORRECT_L,box_size=4)
            qr.add_data(qr_string)
            qr.make() 
            im = qr.make_image()
            fname=tempfile.NamedTemporaryFile(suffix='.png',delete=False)
            im.save(fname.name)
            f = open(fname.name, "r")
            data = f.read()
            f.close()
            self.write({'cfdi_cbb':base64.encodestring(data)})             
        else:
            pass
    """

    @api.multi
    def test(self):
        #pdb.set_trace()
        if self.id:
            print "|||||||||||||||||||||||||||||||||||||||||||Hola|||||||||||||||||||||||||||||||||||||||1"
        else:
            return

