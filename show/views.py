

# Create your views here.
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404

from django.urls import reverse
from .models import Profile
import requests
import csv
import os
from django.contrib.auth import login,logout,authenticate

url = "https://api.themoviedb.org/3/tv/{}?api_key=cfbf1e4c6331a7da2ad4b5d8c373490e"
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'static/anime.csv')


def fill_csv(user_reg_tv_shows, file_name):
    tv_shows = []
    update = False
    with open(file_name, newline='') as csvfile:
    	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    	for row in reader:
    		if row[0] != "name" and row[1] in user_reg_tv_shows:
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


def index(request):
    if request.user.is_authenticated:
        obj = Profile.objects.get(user=request.user.id)
        # print(obj.ep_list)
        if obj.ep_list is not None:
            tv_show = fill_csv(obj.ep_list, file_path)
            print(tv_show)
        context = {
            'tv_shows':tv_show
        }
        return render(request,"show/dashboard.html", context=context)
    else:
        return render(request,"show/home.html")


def get_details_of_tv_shows(ep_list):
    tv_show = []



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        global user
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "show/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "show/login.html")





def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))






def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email=request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "show/register.html", {
                "message": "Passwords must match."
            })

      
        # try:
        #     user = User.objects.create_user(username, email, password)
        #     user.save()
        # except IntegrityError as e:
        #     print(e)
        #     return render(request, "mail/register.html", {
        #         "message": "Email address already taken."
        #     })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "show/register.html")
