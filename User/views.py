import email
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from django.contrib.auth import login, logout, authenticate

from .models import User
from News.models import Like, News, Comment, LikeComment


class SignUp(View):
	def get(self, request):
		return render(request, 'signup.html')

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		emails = request.POST.get('email')
		if username and password:
			if username != User.username:
				user = User.objects.create(
					username=username,
					password=password,
					email=emails,
				)
				user.set_password(password)
				user.save()
				send_mail(
                'iPro Service',
                'Assalomu Aleykum',
                settings.EMAIL_HOST_USER,
                [user.email, ]
            	)
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
				return redirect('home')
		return render(request, 'SignUp.html')


class SignIn(View):
	def get(self, request):
		return render(request, 'SignIn.html')

	def post(self, request):
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			send_mail(
                'iPro Service',
                'Assalomu Aleykum',
                settings.EMAIL_HOST_USER,
                [user.email, ]
            )
			return redirect('home')
		return render(request, 'SignIn.html')


class LogOut(View):
	def get(self, request):
		logout(request)
		return redirect('home')


class LikeNews(View):
	def post(self, request, slug):
		news = News.objects.get(slug=slug)
		if Like.objects.filter(news=news):
			like = Like.objects.filter(news=news).first()
			if request.user in like.user.all():
				like.user.remove(request.user)
				return redirect('home')
			like.user.add(request.user)
			return redirect('home')
		like = Like.objects.create(
				news=news
			)
		like.user.add(request.user)
		return redirect('home')


class LikeCommentList(View):
	def post(self, request, id):
		comment = Comment.objects.get(id=id)
		if LikeComment.objects.filter(comment=comment):
			like = LikeComment.objects.filter(comment=comment).first()
			if request.user in like.user.all():
				like.user.remove(request.user)
				return redirect('home')
			like.user.add(request.user)
			return redirect('home')
		like = LikeComment.objects.create(
				comment=comment
			)
		like.user.add(request.user)
		return redirect('home')
