# -*- coding: utf-8 -*-
from django.db import models
from localflavor.br.forms import STATE_CHOICES as BR_STATES


class Contact(models.Model):

    name = models.CharField(
        u'Nome',
        max_length=200
    )

    email = models.EmailField(
        u'Nome'
    )

    phone = models.CharField(
        u'Telefone',
        max_length=20
    )

    estado = models.CharField(
        u'Estado',
        max_length=2,
        choices=BR_STATES
    )

    cidade = models.CharField(
        u'Cidade',
        max_length=100
    )

    message = models.TextField(
        u'Mensagem'
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Contato'
        verbose_name_plural = u'Contatos'
