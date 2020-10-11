import csv 

with open('csv.csv', mode='w') as test_csv:
	items = [
		{
		'name':'asdf',
		'id':'123',
		'next_ep':'asdfasdf'
		},
		{
		'name':'asdf',
		'id':'123',
		'next_ep':'asdfasdf'
		},
	]
	employee_writer = csv.writer(test_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	employee_writer.writerow(['name', 'id', 'next_ep'])
	for item in items:
		employee_writer.writerow([item['name'],item['id'],item['next_ep']])