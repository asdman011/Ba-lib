from datetime import timedelta
from django.shortcuts import render, redirect
from .forms import FolderForm, ProfileForm, BookForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Book, ReadingProgress, Folder
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.http import Http404

def user_profile(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, id=user_id)
    
    # Check if the current user is viewing their own profile
    is_owner = user == request.user
    return render(request, 'user_profile.html', {'user': user, 'is_owner': is_owner})

@login_required
def dashboard(request):
    reading_progress, _ = ReadingProgress.objects.get_or_create(user=request.user)
    folders = Folder.objects.filter(user=request.user).prefetch_related('books')  # Load folders and related books
    
    return render(request, 'dashboard.html', {
        'reading_progress': reading_progress,
        'folders': folders
    })
    
@login_required
def book_list(request):
    books = Book.objects.filter(folder__user=request.user)
    return render(request, 'book_list.html', {'books': books})

@login_required
def folder_list(request):
    folders = Folder.objects.filter(user=request.user)
    return render(request, 'folder_list.html', {'folders': folders})

@login_required
def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            messages.success(request, 'Folder created successfully!')
            return redirect('my_folders')
    else:
        form = FolderForm()
    return render(request, 'create_folder.html', {'form': form})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    pages_left = book.total_pages - book.current_page
    return render(request, 'book_detail.html', {'book': book, 'pages_left': pages_left})


@login_required
def folder_detail(request, folder_id):
    try:
        # First, get the folder. Check if it's either public or belongs to the user
        folder = Folder.objects.get(id=folder_id)
        
        if not folder.is_public and folder.user != request.user:
            raise PermissionDenied("You do not have permission to view this folder.")
        
        # Load books related to the folder
        books = folder.books.all()
        return render(request, 'folder_detail.html', {'folder': folder, 'books': books})
    
    except Folder.DoesNotExist:
        raise Http404("No Folder matches the given query.")

@login_required
def my_folders(request):
    folders = Folder.objects.filter(user=request.user)
    return render(request, 'my_folders.html', {'folders': folders})

def public_folders(request):
    folders = Folder.objects.filter(is_public=True)
    return render(request, 'public_folders.html', {'folders': folders})

def public_profiles(request):
    User = get_user_model()
    users_with_public_folders = User.objects.filter(folder__is_public=True).distinct()
    return render(request, 'public_profiles.html', {'users': users_with_public_folders})

@login_required
def add_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        book = form.save()
        return redirect('dashboard')  # Assuming a dashboard view
    return render(request, 'add_book.html', {'form': form})


from django.core.exceptions import PermissionDenied

@login_required
@require_http_methods(["POST"])
def update_reading_progress(request, book_id):
    # Get the book and ensure it exists
    book = get_object_or_404(Book, id=book_id)
    
    # Check if the logged-in user is the owner of the folder that contains the book
    if book.folder.user != request.user:
        raise PermissionDenied("You do not have permission to update this book's progress.")
    
    # Proceed with updating the reading progress only if the user is the owner
    pages_read = int(request.POST.get('pages_read', 0))
    book.current_page += pages_read
    if book.current_page >= book.total_pages:
        book.current_page = book.total_pages
        book.is_read = True
    book.save()

    # Update the streak for the folder
    folder = book.folder
    today = timezone.now().date()
    if folder.last_read_date == today - timedelta(days=1):
        folder.streak_count += 1
    elif folder.last_read_date != today:
        folder.streak_count = 1
    folder.last_read_date = today
    folder.save()

    # Update the general reading streak for the user
    progress, _ = ReadingProgress.objects.get_or_create(user=request.user)
    progress.update_general_streak()

    return redirect('dashboard')


@login_required
def get_reading_progress(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        progress = ReadingProgress.objects.get(user=request.user, book=book)
        return JsonResponse({
            'current_page': progress.current_page,
            'streak_count': progress.streak_count,
            'last_read_date': progress.last_read_date,
        })
    except ReadingProgress.DoesNotExist:
        return JsonResponse({'error': 'Progress not found'}, status=404)

def profile(request):
    if not request.user.is_authenticated:
        return render(request, 'not_logged_in.html')
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form})

def index(request):
    return render(request, 'index.html')  # This serves React's index.html

def not_logged_in(request):
    return render(request, 'not_logged_in.html')