import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.conf import settings

from .models import User, Pet, Comment, Organization
from .forms import *

ITEMS_PER_PAGE = 5

def show_pets(title, request, pets, profile=None):

    # Get current page of posts
    page_index = request.GET.get("page", 1)
    paginator = Paginator(pets, ITEMS_PER_PAGE)
    page = paginator.page(page_index)
    page_numbers = list(paginator.page_range)

    # Show animals
    context = {
            "pets": page,
            "count": pets.count,
            "title": title,
            "profile":profile,
            "page_numbers": page_numbers
        }
    return render(request, "adopt/list.html", context)



def index(request):
    """
    List the 4 most recent pet posts
    Browse post listings for each organization
    """
    pets = Pet.objects.filter(adopted_by__isnull=True)[:4]

    organizations = Organization.objects.all()

    context = {
        "pets":pets,
        "organizations": organizations
    }
    return render(request,  "adopt/index.html", context)


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        #email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        #user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "adopt/login.html", {
                "message": "Invalid username and/or password."
            })
    elif request.method == "GET":
        return render(request, "adopt/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        organization = request.POST["organization"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        province = request.POST["province"]
        
        # Check if organization is selected, get the organization instance
        if 'organization' in request.POST:
            organization_id = request.POST["organization"]
            if organization_id != '':
                organization = Organization.objects.get(id=organization_id)

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "adopt/register.html", {
                "message": "Passwords must match."
            })
    

        # Attempt to create new user
        try:
            if organization_id == '' :
                user = User.objects.create_user(
                    username=username, 
                    email=email, 
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    address=address,
                    province=province
                    )
            else:
                user = User.objects.create_user(
                    username=username, 
                    email=email, 
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    organization=organization,
                    phone=phone,
                    address=address,
                    province=province
                    )
            user.save()
        except IntegrityError:
            return render(request, "adopt/register.html", {
                "message": "Email address already existed."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    elif request.method == "GET":
        form = UserForm()
        return render(request, "adopt/register.html", {"form": form})


@login_required 
def create(request):

    if request.method == "POST":
        form = PetCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.registered_by = request.user
            instance.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "adopt/pet_form.html", {"form":form, "message":form.errors, "action":"Create"})
    elif request.method == "GET":
        context = {
                "form": PetCreateForm(),
                "action": "Create",
                "title": "Create Pet Profile"
            }
        return render(request, "adopt/pet_form.html", context)


@login_required
def edit(request, pk):

    if request.method == "POST":
        # Instaniate the form according to the action
        
        instance = get_object_or_404(Pet, pk=pk)
        form = PetCreateForm(request.POST, instance=instance)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.registered_by = request.user
            instance.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "adopt/pet_form.html", {"form":form, "message":form.errors, "action":"edit"})
    elif request.method == "GET":
        # GET method
        instance = get_object_or_404(Pet, pk=pk)
        context = {
            "form": PetCreateForm(instance=instance),
            "action": "edit",
            "title": "Edit Pet Profile"
        }
        return render(request, "adopt/pet_form.html", context)


def detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    context = {
            "pet": pet,
            "comments":pet.comments.order_by("-created_time").all()
        }
    return render(request, "adopt/pet_profile.html", context)


def search(request):

    if request.method == "POST":
        # Clear the filterDic session variable 
        if 'filterDict' in request.session:
            del request.session['filterDict']

        form = PetSearchForm(request.POST)
    
        if form.is_valid():
            # Construct the search query            
            keys = form.cleaned_data.keys()
            values = form.cleaned_data.values()
            filterDict = {}
            for key, value in zip(keys, values):
                # Check if value is a empty list
                if value != []:
                    if isinstance(value, list):
                        key = f"{key}__in"
                    filterDict[key] = value

            pets = Pet.objects.filter(**filterDict).order_by("-registered_date")

            # Get current page of posts
            page_index = request.GET.get("page", 1)
            paginator = Paginator(pets, ITEMS_PER_PAGE)
            page = paginator.page(page_index)
            page_numbers = list(paginator.page_range)

            # Store the search parameters in session
            request.session['filterDict'] = filterDict

            # Show animals
            context = {
                    "pets": page,
                    "count": pets.count,
                    "title": "Search Results",
                    "profile": None,
                    "page_numbers": page_numbers
                }
            return render(request, "adopt/list.html", context)
            #return show_pets("Search Results", request, pets, profile=None)
        else:
            # invalid data 
            print(form.errors)
            return render(request, "adopt/search.html", {"form":form, "form_error":form.errors})
    
    elif request.method == "GET":

        # Check the current page number in the URL
        if request.GET.get('page'):

            filterDict = request.session.get('filterDict')
            pets = Pet.objects.filter(**filterDict).order_by("-registered_date")

            # Get current page number from the URL
            page_index = int(request.GET.get('page'))
            paginator = Paginator(pets, ITEMS_PER_PAGE)
            page = paginator.page(page_index)
            page_numbers = list(paginator.page_range)

            # Show animals
            context = {
                    "pets": page,
                    "count": pets.count,
                    "title": "Search Results",
                    "page_numbers": page_numbers
                }
            return render(request, "adopt/list.html", context)

        else:
            # Display an empty form for GET request
            form = PetSearchForm(initial={})    
            return render(request, "adopt/search.html", {"form": form})
        
            


def pets_by_organization (request, pk):

    organization = get_object_or_404(Organization, pk=pk)

    registered_users = User.objects.filter(organization_id=organization.id)

    pets = Pet.objects.filter(
        registered_by__in=registered_users, 
        adopted_by__isnull=True
    )
  
    return show_pets(organization.name, request, pets, profile=None)


@csrf_exempt
@login_required
def like(request):

    if request.method != 'POST':
        return JsonResponse({"error":"POST method required."}, status=400)
    
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User is not authenticated"}, status=400)
    
    current_user = User.objects.get(username=request.user)

    data = json.loads(request.body)
    pet_id = int(data.get("pet_id", ""))

    if pet_id == "":
        return JsonResponse({"error": "Missing Pet Id"}, status=400)
    
    pet = Pet.objects.get(id=pet_id)
    if pet.likes.filter(id=current_user.id).exists():
        # Remove Like
        pet.likes.remove(current_user)
        pet.refresh_from_db()
    else:
        # Add Like
        pet.likes.add(current_user)
        pet.refresh_from_db()

    count = pet.get_total_likes()

    return JsonResponse({
        "message":"Liked pet successfully",
        "count": count
    }, status=400)


@login_required
def comment(request, pk):
    if request.method == "POST":
        content = request.POST["comment"]
        pet = get_object_or_404(Pet, pk=pk)
        comment = Comment(commenter=request.user, content=content, pet=pet)
        comment.save()
        return HttpResponseRedirect(reverse("detail", args=(pet.id,)))
    

@login_required
def favorite(request):

    current_user = User.objects.get(username=request.user) 
    pets = Pet.objects.filter(likes=current_user)

    title = current_user.username + "'s Favorites"
    return show_pets(title, request, pets, profile=current_user)


@login_required
def myAnimals(request):

    current_user = User.objects.get(username=request.user) 
    pets = Pet.objects.filter(registered_by=current_user)

    return show_pets(current_user.username, request, pets, profile=current_user)