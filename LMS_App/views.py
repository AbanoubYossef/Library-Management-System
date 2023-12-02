from django.shortcuts import redirect, render,get_object_or_404
from . models import *
from . forms import *
# Create your views here.
def home(request):
    if request.method == 'POST':
        add_new_cat = CategoryForm(request.POST)
        add_new_book = BookForm(request.POST,request.FILES)
        
        if add_new_book.is_valid():
            add_new_book.save()
            
            
        if add_new_cat.is_valid():
            add_new_cat.save()    
        
    context={
        'categories':Category.objects.all(),
        'books': Book.objects.all(),
        'add_book_form':BookForm(),
        'add_cat_form': CategoryForm(),
        
    }
    return render(request,'index.html',context)


def books(request):
    context={
        'categories':Category.objects.all(),
        'books': Book.objects.all(),
        
    }
    return render(request,'books.html',context)   

def delete(request,id):
    book_deleted = get_object_or_404(Book,id=id)
    if request.method == 'POST':  
        book_deleted.delete()
        return redirect('home')
    return render(request,'delete.html')   

def update(request,id): 
    book_id = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        update_book= BookForm(request.POST,request.FILES,instance=book_id)
        if update_book.is_valid():
            update_book.save()
            return redirect('home')
    else:
        update_book =BookForm(instance=book_id)  
    context={
            'form':update_book,
        }       
    return render(request,'update.html',context)   

