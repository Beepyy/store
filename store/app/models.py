from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    money=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user}"



class Basket(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE,related_name="basket")
    #goods=models.ManyToManyField(Goods,unique=False)



class Bought(models.Model):

    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="bought",null=True,unique=False)
#      good_name=models.CharField(max_length=30,default='None',null=True,blank=True)
#      num_of_good=models.IntegerField(default=0)
#      good_price=models.IntegerField(default=0)
#      good_full_price=models.IntegerField(default=0)
    


class Catalogs(models.Model):
    catalog_name=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.catalog_name}"



class Goods(models.Model):
    name_of_good=models.CharField(max_length=20,verbose_name="Товар")
    price=models.IntegerField(default=0)
    amount=models.IntegerField(default=0)
    catalog=models.ForeignKey(Catalogs,on_delete=models.CASCADE,related_name='good',null=True)

    def __str__(self):
        return f"{self.name_of_good}"

    class Meta:
        verbose_name="Good"

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])



class Product(models.Model):
   good=models.ForeignKey(Goods,on_delete=models.CASCADE,related_name="product",null=True)
   num_of_good=models.IntegerField(default=0)
   basket=models.ForeignKey(Basket,on_delete=models.CASCADE,related_name="product",null=True)
   profile=models.ForeignKey(Bought,on_delete=models.CASCADE,related_name="product",null=True)
   good_full_price=models.IntegerField(default=0)
   date_time=models.DateTimeField(auto_now_add=True)

   LOAN_STATUS = (
        ('S','InStock'),
        ('O', 'OnBuying'),
        ('T', 'TimeIsOut'),
        ('B', 'Bought'),
        ('C','Canceled')
    )
   status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='S', help_text='Purchasing status')
   


class Goods_descr(models.Model):
    #To OneToOneField related_name='good_descr'
    good=models.ForeignKey(Goods,on_delete=models.CASCADE,related_name='good_descr',null=True)
    descr=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.descr}"