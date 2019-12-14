from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)    # istedigimiz isimde gosterilsin istiyorsak parantez bitmeden ,verbose_name="Yazar" diyebiliriz ve admin sayfasinda degismis oldugunu goruruz. bunu diger basliklar icinde yapabiliriz.
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)            # eklenen makale icin otomatik tarih eklesin
    def __str__(self):       # baslik ve diger yazilarin admin kanalinda gorunsun istiyorsak bu fonksiyonu yapmaliyiz
        return self.title
