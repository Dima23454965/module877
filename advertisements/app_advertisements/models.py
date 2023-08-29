from django.db import models

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

    def __str__(self):
        return f" Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'


    # продавец (имя, контакты, отзывы)

    #фото объявления

    #рейтинг

    #в продаже/не в продаже - актуальность

    

    