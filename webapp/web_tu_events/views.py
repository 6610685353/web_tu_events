from .models import Announcement, Found, Lost, Club
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .forms import FoundForm, LostForm, ClubAnnouncementForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# def login(request):
#     return render(request, "login.html")


def all_events(request):
    all_announcement = Announcement.objects.all()
    return render(
        request, "events/all_events.html", {"all_announcement": all_announcement}
    )


def event_detail(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    return render(request, "events/event_detail.html", {"announcement": announcement})


def category_events(request, category):
    announcement = Announcement.objects.filter(categories=category)

    return render(
        request,
        "events/category_events.html",
        {"announcement": announcement, "category": category},
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                messages.error(request, "Invalid username.")
                return redirect("login")  # Redirect back to login page

            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, "Invalid password.")
                return redirect("login")  # Redirect back to login page

            login(request, user)

            if user.is_superuser:

                messages.success(
                    request, "Welcome, Admin! Redirecting to the admin panel."
                )
                return redirect(reverse("admin:index"))
            elif username.isnumeric():

                messages.success(request, "Welcome, Student!")
                return render(request, "home.html")
            else:

                messages.success(request, "Welcome, Club Account!")
                return render(request, "home.html")
        else:
            messages.error(request, "Both fields are required.")
            return redirect("login")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# โพสของที่เจอ
def create_found_item(request):
    if request.method == "POST":
        form = FoundForm(request.POST, request.FILES)
        if form.is_valid():
            found_item = form.save(commit=False)
            found_item.student = request.user.student 
            found_item.save()
            return redirect('found_items_list')
    else:
        form = FoundForm()

    return render(request, "found/create_found_item.html", {"form": form})


# หน้ารวมของที่เจอ
def found_items_list(request):
    found_items = Found.objects.all().order_by("-id")  # เรียงตาม id ล่าสุด
    return render(request, "found/found_items_list.html", {"found_items": found_items})


# โพสของหาย
def create_lost_item(request):
    from django.shortcuts import render, redirect
from .forms import LostForm
from .models import Lost

def create_lost_item(request):
    if request.method == "POST":
        form = LostForm(request.POST, request.FILES)
        if form.is_valid():
            lost_item = form.save(commit=False)
            lost_item.student = request.user.student 
            lost_item.save()
            return redirect('lost_items_list')
    else:
        form = LostForm()

    return render(request, "lost/create_lost_item.html", {"form": form})



# หน้ารวมของหาย
def lost_items_list(request):
    lost_items = Lost.objects.filter().order_by("-id")
    return render(request, "lost/lost_items_list.html", {"lost_items": lost_items})


# สมาชิกชุมนุมโพสประกาศกิจกรรม
@login_required
def club_create_announcement(request):
    if not request.user.username.startswith("tu_"):
        return redirect("home")  # ถ้าไม่ใช่accountชุมนุมจะกลับไปหน้าhome

    if request.method == "POST":
        form = ClubAnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.categories = "clubs"
            announcement.save()
            return redirect("club_announcement_list")
    else:
        form = ClubAnnouncementForm()

    return render(request, "club/club_create_announcement.html", {"form": form})


# รวมโพสจากทุกclub
def all_club_announcement_list(request):
    all_club_announcements = Announcement.objects.filter(categories="clubs").order_by(
        "-date"
    )
    clubs_info = Club.objects.filter().order_by("-id")
    return render(
        request,
        "clubs/clubs_announcement_list.html",
        {"announcements": all_club_announcements, "clubs": clubs_info},
    )


def lost_detail(request, lost_id):
    lost = get_object_or_404(Lost, id=lost_id)
    return render(request, "lost/lost_item_detail.html", {"lost": lost})



def found_detail(request, found_id):
    found = get_object_or_404(Found, id=found_id)
    return render(request, "found/found_item_detail.html", {"found": found})


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("login")

def lost_edit(request, lost_id):
    lost = get_object_or_404(Lost, id=lost_id)

    return render(request, "lost/edit_lost_item.html", {"lost": lost})

def found_edit(request, found_id):
    found = get_object_or_404(Found, id=found_id)
    return render(request, "found/edit_found_item.html", {"found": found})

def tu_clubs_list(request):
    clubs = Club.objects.filter(origin="tu")
    return render(request, "clubs/tu_clubs.html", {"clubs": clubs})

def club_detail(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    return render(request, "clubs/club_detail.html", {"club": club})
