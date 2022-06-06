
from turtle import title
from django.db.models.signals import pre_save , pre_delete , pre_init , post_init
from django.dispatch import receiver
from django.utils.text import slugify
from requests import request
from .models import blogmodel, contactModel
from colorama import Fore
import colorama
colorama.init(autoreset=True)
def pre_save_slugify(sender , instance , *args, **kwargs):
    if not instance.slug:
        # print(Fore.LIGHTRED_EX + 'FUCK YOU')
        # print(instance.title)
        slug = slugify(instance.title)
        instance.slug = slug
    else:
        if instance.title:
            slug = slugify(instance.title)
            instance.slug = slug


pre_save.connect(pre_save_slugify ,sender=blogmodel)


def pre_delete_print(sender, instance, *args, **kwargs):
    if instance.title:
        print(instance.title)
        # 30 days trash bin then full delete
        i = input('are you sure? ')
        if i == 'yes':
            print(Fore.CYAN +'OK')
        else:
            print(Fore.RED + 'OK BABY')
            exit()
    else:
        print(Fore.RED + 'Not found')
        exit()

pre_delete.connect(pre_delete_print , sender=blogmodel)

# هر دفعه که به دیتابیس کويری زده میشه این تابع فعال میشه
def pre_init_signal(sender , *args, **kwargs):
    # print(f"{Fore.LIGHTCYAN_EX} kwargs: {kwargs} \n ")
    for key, value in kwargs.items():
        print (f"{Fore.GREEN} KEY:\n{key},\n  {Fore.GREEN}VALUE:\n{value}")

# pre_init.connect(pre_init_signal , sender=blogmodel)


def post_init_signal(sender , instance , *args, **kwargs):
    print("-"*100 ,"\n" ,instance.id)
# post_init.connect(post_init_signal , sender=blogmodel)


def pre_save_slugifye(sender , instance , *args, **kwargs):
    if not instance.slug:
        # print(Fore.LIGHTRED_EX + 'FUCK YOU')
        # print(instance.title)
        slug = slugify(instance.name)
        instance.slug = slug
    else:
        if instance.name:
            slug = slugify(instance.name)
            instance.slug = slug


pre_save.connect(pre_save_slugifye ,sender=contactModel)
