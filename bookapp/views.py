from django.shortcuts import render, redirect
from .models import Book
from .models import Cart
import os


# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        bookobj = Book()
        bookobj.book_name = request.POST.get('book_name')
        bookobj.book_author = request.POST.get('book_author')
        bookobj.book_category = request.POST.get('book_category')
        bookobj.book_copies = request.POST.get('book_copies')
        bookobj.book_description = request.POST.get('book_description')
        bookobj.book_pages = request.POST.get('book_pages')
        bookobj.book_price = request.POST.get('book_price')
        bookobj.book_publisher = request.POST.get('book_publisher')
        bookobj.book_image = request.FILES.get('book_image')
        bookobj.save()
        return redirect('/view')
    else:
        return render(request, 'add.html')
    
def view(request):
    books = Book.objects.all()
    return render(request, 'view.html', {'books':books})

def update(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.book_name = request.POST.get('book_name')
        book.book_author = request.POST.get('book_author')
        book.book_category = request.POST.get('book_category')
        book.book_copies = request.POST.get('book_copies')
        book.book_description = request.POST.get('book_description')
        book.book_pages = request.POST.get('book_pages')
        book.book_price = request.POST.get('book_price')
        book.book_publisher = request.POST.get('book_publisher')
        
        # Check if a new image was uploaded; 
        if request.FILES.get('book_image'):

            old_image_path = book.book_image.path
            if old_image_path and os.path.exists(old_image_path):
                os.remove(old_image_path)

            book.book_image = request.FILES['book_image']
        else:
            # Keep the existing image if no new image is uploaded
            book.book_image = book.book_image 

        book.save()
        return redirect('/view')
    else:
        return render(request, 'update.html', {'book':book})
    
def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books':books})

def book(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book.html', {'book':book})

def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/view')

def add_to_cart(request, id):
    cart_obj = Cart()
    cart_obj.book = Book.objects.get(id=id)
    cart_obj.save()
    return redirect('/books')

def view_cart(request):
    items = Cart.objects.all()
    total_amount = sum(item.book.book_price for item in items)  # Calculate total amount
    return render(request, 'cart.html',{'items':items, 'total_amount':total_amount})

def delete_cart(request, id):
    cart = Cart.objects.get(cart_id=id)
    cart.delete()
    return redirect('/cart')

