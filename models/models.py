# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PortofolioSkills(models.Model):
	_name = 'portofolio.skills'

	name = fields.Char(string='Nama', required=True)
	score = fields.Integer(string='Score', required=True)
	skills_id = fields.Many2one(comodel_name="hr.employee", string="Nama")


class PortofolioWorks(models.Model):
	_name = 'portofolio.works'

	name = fields.Char(string='Nama', required=True)
	image = fields.Binary(string='Gambar')
	link = fields.Char(string='Link', required=True)
	description = fields.Text(string='Description')
	works_id = fields.Many2one(comodel_name="hr.employee", string='Nama')


class PortofolioExperience(models.Model):
	_name = 'portofolio.experience'

	name = fields.Char(string='Nama', required=True)
	start = fields.Date(string='Year Start')
	end = fields.Date(string='Year End')
	year = fields.Char(string='Year', compute='get_year')
	description = fields.Text(string='Description')
	experiences_id = fields.Many2one(comodel_name="hr.employee", string='Nama')

	def get_year(self):
		for x in self:
			x.year = str(x.start.year) + ' / ' + str(x.end.year)


class PortofolioSocial(models.Model):
	_name = 'portofolio.social'

	name = fields.Char(string='Nama', required=True)
	link = fields.Char(string='Link', required=True)
	social_id = fields.Many2one(comodel_name="hr.employee", string='Nama')


class Employees(models.Model):
	_name = 'hr.employee'
	_inherit = 'hr.employee'

	profile = fields.Text(string='Profile')

	skills_ids = fields.One2many(
		'portofolio.skills',
		'skills_id',
		string='Skills',
	)

	works_ids = fields.One2many(
		'portofolio.works',
		'works_id',
		string='Works',
	)

	experience_ids = fields.One2many(
		'portofolio.experience',
		'experiences_id',
		string='Experience',
	)

	social_ids = fields.One2many(
		'portofolio.social',
		'social_id',
		string='Social Media',
	)