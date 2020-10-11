

# Create your views here.
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404

from django.urls import reverse

from django.contrib.auth import login,logout,authenticate


def index(request):
	if request.user.is_authenticated:
		return render(request,"show/dashboard.html")

	else:
		return render(request,"show/home.html")




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
