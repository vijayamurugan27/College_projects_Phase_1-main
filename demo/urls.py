"""tempaltedemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from demo import views
from demo.views import TrainerCreateView, TrainerUpdateView, TrainingUpdateView
app_name = "demo"

urlpatterns = [
    path('home', views.home, name = 'home'),
    # path('', views.home, name = 'home'),
    path('blog', views.blog, name = 'blog'),
    path('about', views.about, name = 'about'),
    path('portfolio', views.portfolio, name = 'portfolio'),
    path('contact', views.contact, name = 'contact'),
    path('blogsingle/<id>', views.blogsingle, name = 'blogsingle'),
    path('training', views.training, name = 'training'),
    path('trainingdetails/<id>', views.trainingdetails, name = 'trainingdetails'),
    path('TrainerCreateView', TrainerCreateView.as_view(), name = 'TrainerCreateView'),
    path('<pk>/trainer', TrainerUpdateView.as_view(), name = 'trainer'),
    path('<pk>/training', TrainingUpdateView.as_view(), name = 'training')
]


# home, about, blog, portfolio, contact, blogsingle