create_test_data:
	make create_test_hospitals
	make create_test_doctors
	make create_test_nurses
	make create_test_patients
	make create_test_eps

create_test_hospitals:
	python manage.py create_test_hospitals

create_test_doctors:
	python manage.py create_test_doctors

create_test_nurses:
	python manage.py create_test_nurses

create_test_patients:
	python manage.py create_test_patients

create_test_eps:
	python manage.py create_test_eps



