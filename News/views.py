from django.shortcuts import render, redirect
from django.views import View

from User.models import User
from .models import *


class Haqida(View):
	def get(self, request):
		# haqida = Haqida.objects.all()
		return render(request, 'about.html')


class CreateNews(View):
	def get(self, request):
		return render(request, 'create.html')

	def post(self, request):
		photo_list = request.FILES.getlist('photo', [])
		title=request.POST.get('title')
		content=request.POST.get('content')
		# photo = request.FILES.get('photo')
		if title and content:
			news = News.objects.create(
				title=title,
				content=content,
				user=request.user,
				video=request.POST.get('video'),
			)
			for x in photo_list:
				p = Photo.objects.create(
					photo=x
					)
				news.photo.add(p)
			return redirect('home')
		return render(request, 'create.html')


class OpenNews(View):
	def get(self, request, slug):
		news = News.objects.get(slug=slug)
		news.viewed_list = news.viewed_list+0
		news.sum_of_vieved_list()
		return render(request, 'reservation.html', {'news':news})

	def post(self, request, slug):
		news = News.objects.get(slug=slug)
		comment = request.POST.get('comment')
		if comment:
			Comment.objects.create(
				comment=comment,
				news=news,
				user=request.user
				)
			return redirect('home')
		return render(request, 'course-details.html', {'news':news})


class EditNews(View):
	def get(self, request, id):
		news = News.objects.get(id=id)
		return render(request, 'create.html', {'form':news})

	def post(self, request, id):
		news = News.objects.get(id=id)
		title=request.POST.get('title')
		content=request.POST.get('content')
		photo = request.FILES.get('photo')
		if title.exsists():
			News.objects.create(
				title=title,
				content=content,
				photo=photo
			)
			return redirect('home')
		return render(request, 'create.html', {'form':news})


class DeleteNews(View):
	def get(self, request, id):
		news = News.objects.get(id=id)
		news.delete()
		return redirect('home')
