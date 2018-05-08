from django.contrib import admin
from .models import ApiApplicationer,ApiList
from django.core.mail import EmailMessage  
from django.contrib.auth.hashers import make_password
import random
import string
import rsa 
import os

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def sendEmail(modeladmin, request, queryset):
	sendEmail.short_description = "发送邮件"
	for apper in queryset:
		sa = []
		for i in range(16):
			sa.append(random.choice(seed))

		appID = apper.email[:4]
		appID +=  ''.join(sa)
		sa = []
		for i in range(8):
			sa.append(random.choice(seed))

		appKey = ''.join(sa)
		appKey = make_password(appKey)[20:80]
		(pubkey, privkey) = rsa.newkeys(512)

		fd = open('key.txt', 'w')
		fd.write("AppID: " + appID +'\n')
		fd.write("AppKey: " + appKey+ '\n')
		fd.write("PublicKey: " + str(pubkey))
		fd.close
		ApiList.objects.create(appId=appID,appKey=appKey,publicKey=str(pubkey),privateKey=str(privkey))
		email = EmailMessage("接口申请成功","请注意查收附件。", "alex_noreply@163.com", [apper.email])
		email.content_subtype = "html"
		fd = open('key.txt', 'r')
		email.attach('key.txt', fd.read(), 'text/plain')
		email.send()
		os.remove('key.txt')




@admin.register(ApiApplicationer)
class ApiApplicationerAdmin(admin.ModelAdmin):
	list_display = ('email','name')
	search_fields = ('email','name')
	actions = [sendEmail]
		
# Register your models here.
