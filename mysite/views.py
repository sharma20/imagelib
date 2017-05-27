from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ImageUploadForm, RegisterForm, LoginForm
from .models import UserImage, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
                if user.password == form.cleaned_data['password']:
                    request.session['email'] = form.cleaned_data['email']
                    return redirect('/imagelib/view/')
                else:
                    return HttpResponse('user authentication failed')
            except User.DoesNotExist as e:
                return HttpResponse('user does not exist')
        else:
            print form.errors
    elif request.method == 'GET':
        return render(request, 'mysite/login.html')


def user_view(request):
    message = request.session.pop('message', None)
    user = User.objects.get(email=request.session['email'])
    image_list = user.userimage_set.all().order_by('-pub_date')
    paginator = Paginator(image_list, 10)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    return render(request, 'mysite/index.html', {'message': message, 'images': images})


def upload_file(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            userImage = UserImage()
            user = User.objects.get(email=request.session['email'])
            userImage.user_id = user.user_id
            userImage.image = form.cleaned_data['image']
            userImage.caption = form.cleaned_data['caption']
            userImage.save()
            request.session['message'] = "Image successfully uploaded!!"
        else:
            request.session['message'] = "Could not upload file!!"
        return redirect('/imagelib/view/')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = User()
            user.name = form.cleaned_data['name']
            user.password = form.cleaned_data['password']
            user.email = form.cleaned_data['email']
            user.save()
            request.session['message'] = "User Registered successfully"
            return redirect('/imagelib/register/')
        else:
            request.session['message'] = "Please try again"
            return redirect('/imagelib/register/')
    return render(request, 'mysite/register.html')


def logout(request):
    try:
        del request.session['name']
    except:
        pass
    return HttpResponse("You are logged out")
