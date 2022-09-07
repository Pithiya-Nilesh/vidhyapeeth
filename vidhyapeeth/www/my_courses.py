import frappe

# import erpnext.education.utils as utils
import vidhyapeeth.www.my_utils as utils

no_cache = 1
language1 = ''

def get_context(context):
	context.education_settings = frappe.get_single("Education Settings")
	if not context.education_settings.enable_lms:
		frappe.local.flags.redirect_location = "/"
		raise frappe.Redirect
	context.featured_programs = get_featured_programs()

def get_featured_programs():

	language = get_language()
	if language == 'hi':
		language = 'हिन्दी'
	elif language == 'gu':
		language = 'ગુજરાતી'
	elif language == 'en':
		language = 'English'
	if frappe.session.user == 'Administrator':
		return utils.get_portal_programs1() or []
	else:
		return utils.get_portal_programs(language) or []
def get_language():
	global language1
	lang = frappe.db.sql(f"select language from `tabUser` where name = '{frappe.session.user}'")
	for language in lang:
		language1 = list(language)[0]
	return language1
