from django.shortcuts import render
from faker import Faker
from .models import People
from decouple import config
import requests
fake = Faker('ko_KR')

# Create your views here.
def index(request):
    return render(request, 'previous/index.html')

def find(request):
    name = request.POST.get('name')
    if not People.objects.filter(name=name).exists():
        job = fake.job()
        people = People(name = name, job = job)
        people.save()
    people = People.objects.filter(name=name)[0]
    
    # 직업 결과에 따라, giphy 요청
    job = people.job
    api_key = config('GIPHY_API_KEY')
    
    # 1. url 설정
    url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=ko'
    
    # 2. 요청 보내기
    response = requests.get(url).json()
    
    # 3. 응답 결과에서 이미지 url 뽑기
    try:
        image_url = response.get('data')[0].get('images').get('original').get('url')
    except:
        image_url = None
    
    context = {
        'people' : people,
        'image_url' : image_url,
    }
    
    return render(request, 'previous/find.html', context)
