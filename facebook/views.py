from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Page
from facebook.models import Comment

# Create your views here.
count = 0
def play1(request):
    return render(request, 'play.html')

def play2(request):
    choidogeun = '최도근'
    age = 20
    global count
    count = count + 1

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    if count == 7:
        lottery = '당첨!'
    else:
        lottery = '꽝...'


    diary = ['오늘은 날씨가 맑았다. 4월 3일', '미세먼지가 너무 심하다. (4월 2일)', '비가 온다. 4월 1일에 작성']
    return render(request, 'play2.html', { 'name':choidogeun, 'diary':diary, 'cnt':count, 'age':status , 'lottery':lottery })

def fail(request):
    return render(request, 'fail.html')

def help(request):
    return render(request, 'help.html')

def warn(request):
    return render(request, 'warn.html')


def my_profile(request):
    return render(request, 'profile.html')

def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', { 'articles': articles })

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':  # new comment
        Comment.objects.create(
            article=article,
            author=request.POST['nickname'],
            text=request.POST['reply'],
            password=request.POST['password']
        )

        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'feed': article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail/')   #비밀번호 오류페이지로 이동

    return render(request, 'edit_feed.html', {'feed': article})

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/') # 첫페이지로 이동하기
        else:
            return redirect('/fail/')   #비밀번호 오류페이지로 이동

    return render(request, 'remove_feed.html', {'feed': article})

def pages(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages})

def new_feed(request):
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            text = request.POST['content']
            text = text + ' - 추신 : 감사합니다.'

            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=text,
                password=request.POST['password']
            )
        return redirect(f'/feed/{ new_article.pk }')
    return render(request, 'new_feed.html')

def new_page(request):
    if request.method == 'POST':    #폼이 전송되었을때만 아래 코드를 시행
        new_Page = Page.objects.create(
            master=request.POST['master'],
            name=request.POST['name'],
            text=request.POST['text'],
            category=request.POST['category']
        )

        return redirect('/pages/')

    return render(request, 'new_page.html')

def remove_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.delete()
        return redirect('/pages/')

    return render(request, 'remove_page.html', {'page': page})


def edit_page(request, pk):
    page = Page.objects.get(pk=pk)

    if request.method == 'POST':
        page.master = request.POST['master']
        page.name = request.POST['name']
        page.text = request.POST['text']
        page.category = request.POST['category']
        page.save()
        return redirect('/pages/')

    return render(request, 'edit_page.html', {'page': page})