from django.contrib import admin
from django.db import models
from django.utils.html import format_html

class Advertisement(models.Model):
    #название товара
    #CharField -короткое текстовое поле
    # 'заголовок' - verbose_name - человекочитаемое название
    title = models.CharField('заголовок', max_length=128)

    #описание товара
    #длинное текстовое поле
    description = models.TextField('описание')

    # цена
    #числовое поле с фиксированной точкой
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    
    #уместен ли торг
    #булевое поле(логическое)
    auction = models.BooleanField('торг', help_text='отметьте если хотите торговаться')

    #дата публикации
    
    created_at = models.DateTimeField(auto_now_add=True)

    #дата изменения обновления + что изменилось
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_date = self.created_at.strftime("%H:%M:%S")
        
            return format_html('<span style="color:green; font-weight:bold;"> сегодня в {} </span>', created_date)

        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")



    @admin.display(description='дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_date = self.updated_at.strftime("%H:%M:%S")
        
            return format_html('<span style="color:blue; font-weight:bold;"> сегодня в {} </span>', updated_date)

        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")



    def __str__(self):
        return f" Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'


    # продавец (имя, контакты, отзывы)

    #фото объявления

    #рейтинг

    #в продаже/не в продаже - актуальность

    

    