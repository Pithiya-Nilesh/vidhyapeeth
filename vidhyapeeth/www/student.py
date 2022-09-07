import frappe

# import erpnext.education.utils as utils
import vidhyapeeth.www.my_utils as utils
language1 = ''

no_cache = 1
def get_context(context):
	context.education_settings = frappe.get_single("Education Settings")
	if not context.education_settings.enable_lms:
		frappe.local.flags.redirect_location = "/"
		raise frappe.Redirect


	context.featured_programs = get_featured_programs()



	# program = {}
	# for p in context.featured_programs:
	# 	print("\n\n\n\n pro", p["program"], "\n\n\n\n")
	# 	if p["has_access"]:
	# 		# print("\n\n\n has",p["program"])
	# 		program.append(p["program"])
	# 	else:
	# 		print("\n\n\n","no any enrollment")
	# print("\n\n\n program list",program)

	# # courses = []
	# # get_courses = frappe.get_doc("Course", "પુષ્ટિસિદ્ધાંતજ્ઞાન")
	# # print(" \n\n\n course=> ", get_courses)

	# context.education_settings = frappe.get_single("Education Settings")
	# context.courses = [frappe.get_doc("Course", course.course) for course in program.courses]
	# print("\n\n\n", context.courses, "\n\n\n")

	# # context.education_settings = frappe.get_single("Education Settings")
	# # context.courses = [frappe.get_doc("Course", course.course) for course in program]
	# # print("\n", context.courses)
	# # context.progress = get_course_progress(context.courses, program)

	context.education_settings = frappe.get_single("Education Settings")

	program_list = []
	courses_list = []
	course_pro_list = []
	recommended_program_list = []

	# program = {}
	for p in context.featured_programs:
		# print("\n\n\n\n pro", p["program"], "\n\n\n\n")
		if p["has_access"]:
			# print("\n\n\n has",p["program"])
			program_list.append(p["program"])
		else:
			# recommended_program_list.append(p["program"])
			# print("\n\n\n recommended pro", p["program"] )
			pass

	for a in program_list:
		# print("\n\n\n after loop", a.name, "\n\n\n")
		context.program = get_program(a.name)
		# print("\n\n context pro", context.program)
		courses = [frappe.get_doc("Course", course.course) for course in context.program.courses]
		# print("\n\n context courses", context.courses, "\n\n")
		courses_list.append(courses)
		# print("\n\n courses_list ", context.courses_list, "\n\n")
		context.has_access = utils.allowed_program_access(a.name)
		# print("\n\n\n con has acs",context.has_access)
		context.progress = get_course_progress(courses, context.program)
		# print("\n\n\n con progress", context.progress, "\n\n")
		course_pro_list.append(context.progress)
		# print("\n\n\n course_pro_list", course_pro_list, "\n\n\n")
		context.courses = courses_list
	# print("\n\n courses", context.courses, "\n\n\n")

	# print("\n\n\n program disc", program["program"], "\n\n\n")


	# context.program = get_program(program)
	# print("\n\n context pro", context.program)
	# context.courses = [frappe.get_doc("Course", course.course) for course in context.program.courses]
	# context.has_access = utils.allowed_program_access(program)
	# context.progress = get_course_progress(context.courses, context.program)


def get_program(program_name):
	try:
		# print("\n\n\n get_program", frappe.get_doc("Program", program_name))
		return frappe.get_doc("Program", program_name)
	except frappe.DoesNotExistError:
		frappe.throw(_("Program {0} does not exist.").format(program_name))


def get_course_progress(courses, program):
	progress = {course.name: utils.get_course_progress(course, program) for course in courses}
	return progress or {}




def get_featured_programs():
	# global language1
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

# ------------------------------------------------------ #
# frappe.cache().set_value('abc', 'hello done')
# value = frappe.cache().get_value('abc')
# print("\n\n\n\n", value, "\n\n\n\n")

def get_language():
	global language1
	lang = frappe.db.sql(f"select language from `tabUser` where name = '{frappe.session.user}'")
	for language in lang:
		language1 = list(language)[0]
	return language1


def get_featured_programs1():
	# global language1
	return utils.get_portal_programs1() or []

