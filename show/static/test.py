import requests
import csv

key = 0
url = "https://api.themoviedb.org/3/tv/{}?api_key=cfbf1e4c6331a7da2ad4b5d8c373490e"


def fill_csv(user_reg_tv_shows, file_name):
    tv_shows = []
    update = False
    with open(file_name, newline='') as csvfile:
    	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    	for row in reader:
    		if row[0] != "name" and int(row[1]) in user_reg_tv_shows:
    			obj = {
    				'name': row[0],
    				'id': row[1],
    				'next_ep' : row[2]
    			}

    			response = requests.get(url.format(obj['id']))
    			if response.status_code == 200:
    				res_data = response.json()['next_episode_to_air'] 
    				if res_data is not None and obj['next_ep'] != res_data['air_date']:
    					update = True
    					obj['next_ep'] = res_data['air_date']

    			tv_shows.append(obj)


    	if update:
    		update_csv(tv_shows, file_name)

    return tv_shows

def update_csv(tv_shows, file_name):
	with open(file_name, mode='w') as test_csv:
		employee_writer = csv.writer(test_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		employee_writer.writerow(['name', 'id', 'next_ep'])
		for item in tv_shows:
			employee_writer.writerow([item['name'],item['id'],item['next_ep']])

user_reg = [456,1434]
print(fill_csv(user_reg, 'tv_show.csv'))