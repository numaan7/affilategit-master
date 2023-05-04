from django.shortcuts import render
from .models import Product, Blog, CustomerQuery, Service
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()    
    blogs = Blog.objects.all()[:4]

    return render(request, 'index.html', context={'products': products, 'allblogs':blogs, 'service':Service.objects.first()})


def products(request):
    products = Product.objects.all()    
    print(products)
    return render(request, 'products.html', context={'products': products})


def about(request):
    return render(request, 'about.html', context={'products': products})


def services(request):
    return render(request, 'services.html', {'services':Service.objects.all()})

def client(request):
    return render(request, 'client.html', context={'products': products})


def contact(request):
    return render(request, 'contact.html')

def blogbyurl(request, posturl):
    blog = Blog.objects.get(blog_url=posturl)
    return render(request, 'blog.html', context={'blog':blog})

def servicebyurl(request, serviceurl):
    service = Service.objects.get(service_url=serviceurl)
    return render(request, 'service.html', context={'service':service})

def blogs(request):
    blog = Blog.objects.all()
    return render(request, 'blogs.html', context={'allblogs':blog})

def write(request):
    blog = Blog.objects.all()
    return render(request, 'write.html', context={'allblogs':blog})

def submitform(request):
    try:
        if request.method == 'POST':

            email = request.POST['email']
            name = request.POST['name']
            message = request.POST['message']
            phone = request.POST['phone']
            if len(email)==0 or len(name)==0 or len(message)==0 or len(phone)!=10:

                return HttpResponse({'failed'})
            custQuery = CustomerQuery.objects.create(name=name, email=email, phone=phone,message=message)
            return HttpResponse({'success'})
    except Exception as e:
        print(str(e))
        return HttpResponse({'failed'})
    
def sitemap(request):
    return render(request, 'sitemap.xml', content_type='application/xml')

def robot(request):
    return render(request, 'robots.txt', content_type='text/html')