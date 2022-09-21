from django.shortcuts import render,redirect
from .models import Page,Post,Song
from .forms import PageForm,PostForm,SongForm
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
#for Singup
def index(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_password1 = request.POST['pass1']
        user_password2 = request.POST['pass2']
        if user_password1==user_password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username allready exist')
                return redirect('/')
            elif User.objects.filter(email=user_email).exists():
                messages.info(request,'email allready exist')
                return redirect('/')
            else:
                new_user = User.objects.create_user(username=user_name,email=user_email,password=user_password1)
                new_user.save()
                return redirect('/login')
        else:
            messages.info(request,'passord does not match')
            return redirect('/')
    else:
        return render(request,'index.html')


#for Login
def login(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_passord = request.POST['pass1']
        user = auth.authenticate(username=user_name,password=user_passord)
        if user is not None:
            auth.login(request,user)
            return redirect('/page')
        else:
            messages.info(request,'detail is not match')
            return redirect('/login')
    else:
        return render(request,'login.html')

#for logout
def logout(request):
    auth.logout(request)
    return redirect('/login')
    


#for user can create page
def page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            page_name = form.cleaned_data['page_name']
            page_cat = form.cleaned_data['page_cat']
            page_publish_date = form.cleaned_data['page_publish_date']

            page_detail = Page(user=user,page_name=page_name,page_cat=page_cat,page_publish_date=page_publish_date)
            page_detail.save()
            return redirect('/pagedetail')
    else:
        form = PageForm()
        return render(request,'pageform.html',{'page_form':form})


#for user can create post
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            post_title = form.cleaned_data['post_title']
            post_cat = form.cleaned_data['post_cat']
            post_publish_date = form.cleaned_data['post_publish_date']

            user_post = Post(user=user,post_title=post_title,post_cat=post_cat,post_publish_date=post_publish_date)
            user_post.save()
            return redirect('/pagedetail')
    else:
        form = PostForm()
        return render(request,'postform.html',{'form_detail':form})


#for user can create song
def song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            song_name = form.cleaned_data['song_name']
            song_duration = form.cleaned_data['song_duration']

            user_song = Song(user=user,song_name=song_name,song_duration=song_duration)
            user_song.save()
            return redirect('/pagedetail')
    else:
        form = SongForm()
        return render(request,'songform.html',{'form_detail':form})
   




def show_user_data(request):
    data1 = User.objects.all()
    data2 = User.objects.filter(email='urmil@gmail.com')
    data3 = User.objects.filter(page__page_cat='programing')
    data4 = User.objects.filter(post__post_publish_date='2022-08-30')
    data5 = User.objects.filter(song__song_duration='10')

    context = {'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5}
    return render(request,'user.html',context)


def show_page_data(request):
    data1 = Page.objects.all()
    data2 = Page.objects.filter(page_cat = 'programing')
    data3 = Page.objects.filter(user__email = 'urmil@gmail.com')
    context = {'data1':data1,'data2':data2,'data3':data3}
    return render(request,'page.html',context)


def show_post_data(request):
    data1 = Post.objects.all()
    data2 = Post.objects.filter(post_publish_date='2022-08-30')
    data3 = Post.objects.filter(user__username = 'urmil')
    context = {'data1':data1,'data2':data2,'data3':data3}

    return render(request,'post.html',context)

def show_song_data(request):
    data1 = Song.objects.all()
    data2 = Song.objects.filter(song_duration = 10)
    data3 = Song.objects.filter(user__username = 'urmil')
    context = {'data1':data1,'data2':data2,'data3':data3}

    return render(request,'song.html',context)