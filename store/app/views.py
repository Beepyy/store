from django.http.response import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#@login_required
def profile(req):
    num_visits=req.session.get('num_visits',0)
    req.session['num_visits'] = num_visits+1
    if req.user.is_authenticated:
        pf,cr=Profile.objects.get_or_create(user=req.user)
        return render(req,"profile.html",{
        "profile":pf
    })
    return render(req,"profile.html")

# Товары в корзине
def basket(req):
    pf=Profile.objects.get(user=req.user)
    Basket.objects.get_or_create(profile=pf)
    bs=pf.basket.product.all()
    bought=pf.bought.get()
    return render(req,"basket.html",{
        "bs":bs,
        "bought":bought

    })

# Добавление в корзину и удаление из корзины
def basket_change(req,g_id):
    pf=Profile.objects.get(user=req.user)
    Basket.objects.get_or_create(profile=pf)
    bs=pf.basket
    good=Goods.objects.get(pk=g_id)
    g_amount=good.amount
    amount=req.POST

    if amount.get('add_amount'):
        amount=int(amount["add_amount"])
        if g_amount<amount:
            return render(req,"descr.html",{
                "good":good,
                "mes":"Выбрано товара больше,чем есть на складе"})
        pr,cr=bs.product.update_or_create(good=good,basket=bs)       
        if cr:
            pr.num_of_good=amount
            pr.save()
            good.amount-=amount
            good.save()
        elif not cr:
            pr.num_of_good+=amount
            pr.save()
            good.amount-=amount
            good.save()
    elif amount.get("del"):
        pr,cr=bs.product.update_or_create(good=good,basket=bs)
        good.amount+=pr.num_of_good
        good.save()
        pr.delete()
        return HttpResponseRedirect(reverse("basket"))
    return HttpResponseRedirect(reverse("goods_descr",args=[g_id]))


# Покупка
def bought(req):
    pf=Profile.objects.get(user=req.user)
    Basket.objects.get_or_create(profile=pf)
    products=pf.basket.product.all()
    lst=[]
    for product in products:
        good_name=product.good.name_of_good
        good_price=product.good.price
        num_of_good=product.num_of_good
        good_full_price=num_of_good*good_price
        lst.append((good_name,num_of_good,good_price,good_full_price))
    full_price=sum([i[3] for i in lst])

    if full_price>pf.money:
        return render(req,"bought.html",{
            "mes":"Недостаточно денег для покупки товаров"
        })
    elif full_price<=pf.money:
        for i in products:
            print(22222222222222222)
            b,cr=Bought.objects.update_or_create(profile=pf)
            b.product.create(good=i.good,num_of_good=i.num_of_good,good_full_price=good_full_price)
            
            #pr,cr=pf.product.update_or_create(profile=pf,good=i.good,num_of_good=i.num_of_good,full_price=full_price) 
            #pr.save()
        pf.money-=full_price
        pf.save()
        pf.basket.delete()
        return render(req,"bought.html",{
             "mes":"Товары успешно куплены,теперь они хранятся в истории"
         })


        # for i in lst:
        #     Bought(good_name=i[0],num_of_good=i[1],good_price=i[2],good_full_price=i[3],profile=pf,).save()
        # pf.money-=full_price
        # pf.save()
        # pf.basket.delete()
        # return render(req,"bought.html",{
        #     "mes":"Товары успешно куплены,теперь они хранятся в истории"
        # })
     
        
    
# Поиск товара
def search(req):
    if req.method=="POST":
        text=req.POST.get("srch",'').title()
        goods=Goods.objects.filter(name_of_good__contains=text)
        return render(req,"search.html",{
         "goods":goods
        })
    elif req.method=="GET":
        pass


# Товары по категории
def goods(req,c_str):
    catalogs=Catalogs.objects.get(catalog_name=c_str)
    goods=catalogs.good.all()
    return render(req,"goods.html",{
    "catalogs":catalogs,
    "goods":goods,
    })


# Информация о товаре
def goods_descr(req,g_id):
    if req.method=="POST":
        good=req.POST.get("text",'')
        if good:
            good=Goods.objects.get(name_of_good=good)
            return render(req,"descr.html",{
            "good":good
        })
        return render(req,"descr.html",{
            "good":None
        })
    try:
        """ =) """
        good = get_object_or_404(Goods, pk=g_id) 
    except:
        good=None
    return render(req,"descr.html",{
        "good":good
    })


# Дотсупные каталоги    
def catalogs(req):
    catalogs=Catalogs.objects.all()
    return render(req,"catalogs.html",{
        "catalogs":catalogs
    })

