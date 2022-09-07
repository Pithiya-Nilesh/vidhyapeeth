# # from __future__ import unicode_literals

# # import frappe

# # def get_context(context):
# # 	# do your magic here
# from __future__ import unicode_literals

# import frappe

# def get_context(context):
# 	# do your magic here
# 	# data = frappe.get_doc("Exam Center", email)
# 	data = frappe.db.sql(f"""select select_exam_centre from `tabStudent Exam Centre` where email = '{frappe.session.user}' """)
# 	# print("\n\n", data, "\n\n")
# 	# context.data = data

# @frappe.whitelist()
# def get_selected_exam_centre():
# 	exam_centre = frappe.db.sql(f"""select select_exam_centre from `tabStudent Exam Centre` where email = '{frappe.session.user}' """)
# 	return exam_centre

# @frappe.whitelist()
# def check_user_selected(selected_exam_centre):
# 	exam_centre = frappe.db.get_value('Student Exam Centre', {'email': frappe.session.user}, 'select_exam_centre')
# 	if exam_centre is None:
# 		# return 'if'
# 		id = frappe.db.sql(f""" select max(name) from `Student Exam Centre` """)
# 		for i in id:
# 			name = int(list(i)[0]) + 1
# 		frappe.db.sql(f""" insert into `Student Exam Centre` (name, select_exam_centre, email) values ('{name}' ,'{selected_exam_centre}', '{frappe.session.user}') """)
# 		return 'your exam centre is selected'
# 	else:
# 		# return 'else'
# 		frappe.db.sql(f""" update `tabStudent Exam Centre` set select_exam_centre = '{selected_exam_centre}' where email = '{frappe.session.user}' """)
# 		return 'your exam centre updated'

# # exam_centre = frappe.db.sql(f""" select select_exam_centre from `tabExam Center` where email = '{frappe.session.user}' """)
# 	# print("\n\n sdf", exam_centre, "\n\n")
# 	# print("\n\n sec", selected_exam_centre, "\n\n")
# 	# if exam_centre == '':
# 	# 	print("\n\n if", exam_centre, "\n\n")
# 	# 	frappe.db.sql(
# 	# 		f""" update `tabExam Center` set select_exam_centre = '{selected_exam_centre}' where email = '{frappe.session.user}' """)
# 	# else:
# 	# 	print("\n\n else", exam_centre, "\n\n")
# 	# 	frappe.db.sql(
# 	# 		f""" insert into `tabExam Center` (name,select_exam_centre, email) values ('abc','{selected_exam_centre}', '{frappe.session.user}') """)
# 	#



# from __future__ import unicode_literals

# import frappe

# def get_context(context):
# 	# do your magic here
from __future__ import unicode_literals

import frappe

def get_context(context):
	# do your magic here
	# data = frappe.get_doc("Exam Center", email)
	data = frappe.db.sql(f"""select select_exam_centre from `tabStudent Exam Centre` where email = '{frappe.session.user}' """)
	# print("\n\n", data, "\n\n")
	# context.data = data

@frappe.whitelist()
def get_selected_exam_centre():
	exam_centre = frappe.db.sql(f"""select select_exam_centre from `tabStudent Exam Centre` where email = '{frappe.session.user}' """)
	return exam_centre

@frappe.whitelist()
def check_user_selected(selected_exam_centre):
	# exam_centre = frappe.db.get_value('Student Exam Centre', {'email': frappe.session.user}, 'select_exam_centre')
	# if exam_centre is None:
	# 	# return 'if'
	# 	id = frappe.db.sql(f""" select max(name) from `Student Exam Centre` """)
	# 	for i in id:
	# 		name = int(list(i)[0]) + 1
	# 	frappe.db.sql(f""" insert into `Student Exam Centre` (select_exam_centre, email) values ('{selected_exam_centre}', '{frappe.session.user}') """)
	# 	return 'your exam centre is selected'
	# else:
	# 	# return 'else'
	# 	frappe.db.sql(f""" update `tabStudent Exam Centre` set select_exam_centre = '{selected_exam_centre}' where email = '{frappe.session.user}' """)
	# 	return 'your exam centre updated'



		# return 'if'
	frappe.db.sql(f""" delete from `tabStudent Exam Centre` where email = '{frappe.session.user}' """)
	return 'ok'
		











# exam_centre = frappe.db.sql(f""" select select_exam_centre from `tabExam Center` where email = '{frappe.session.user}' """)
	# print("\n\n sdf", exam_centre, "\n\n")
	# print("\n\n sec", selected_exam_centre, "\n\n")
	# if exam_centre == '':
	# 	print("\n\n if", exam_centre, "\n\n")
	# 	frappe.db.sql(
	# 		f""" update `tabExam Center` set select_exam_centre = '{selected_exam_centre}' where email = '{frappe.session.user}' """)
	# else:
	# 	print("\n\n else", exam_centre, "\n\n")
	# 	frappe.db.sql(
	# 		f""" insert into `tabExam Center` (name,select_exam_centre, email) values ('abc','{selected_exam_centre}', '{frappe.session.user}') """)
	#