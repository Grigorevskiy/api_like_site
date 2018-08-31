from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    class Meta:
        ordering = ("-created_at",)

    title = models.CharField(max_length=255, blank=False)
    short_description = models.TextField(blank=False)
    body = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class NewsPhoto(models.Model):
    news = models.ForeignKey(News, related_name='news_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_photo')


class Category(models.Model):
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    name = models.CharField(max_length=255, verbose_name='Назва Категорії')
    description = models.TextField(verbose_name='Опис Категорії')
    category_logo = models.ImageField(upload_to='category_logo', null=True, verbose_name='Катринка Категорії')

    def __str__(self):
        return self.name


class Journey(models.Model):
    class Meta:
        verbose_name = "Пригода"
        verbose_name_plural = "Пригоди"
        ordering = ('-updated_at',)

    sku = models.CharField(max_length=255, verbose_name='Номер')
    title = models.CharField(max_length=255, verbose_name='Назва пригоди')
    description = models.TextField(verbose_name='Опис пригоди')
    durations_days = models.IntegerField(verbose_name='Тривалість днів')
    durations_night = models.IntegerField(verbose_name='Тривалість ночей')
    price = models.IntegerField(verbose_name='Ціна')
    sale_price = models.IntegerField(verbose_name='Ціна зі скидкою', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='Journeys', on_delete=models.CASCADE, verbose_name='Категорія')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата останнього оновлення')

    def __str__(self):
        return self.title


class JourneyPhoto(models.Model):
    journey = models.ForeignKey(Journey, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='journeys_photos')


class Comment(models.Model):
    class Meta:
        ordering = ('-created_at',)

    journey = models.ForeignKey(Journey, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Відгук')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class ClientCompany(models.Model):
    class Meta:
        verbose_name = "Клієнт-Компанія"
        verbose_name_plural = "Клієнт-Компанії"

    title = models.CharField(max_length=255, verbose_name='Назва компанії', blank=True)
    logo = models.ImageField(upload_to='companies_logo', verbose_name='Лого')
    site = models.CharField(max_length=255, verbose_name='Сайт', blank=True)

    def __str__(self):
        return self.title


# class Feedback(models.Model):
#     class Meta:
#         verbose_name = "Відгук"
#         verbose_name_plural = "Відгуки"
#
#     name = models.CharField(max_length=255, verbose_name='Імя', blank=True)
#     body_text = models.TextField(verbose_name='Відгук')
#     created_at = models.DateField(auto_now_add=True)
#     is_published = models.BooleanField(default=False, verbose_name='Опубліковано?')
#
#     def __str__(self):
#         return self.name


class Document(models.Model):
    class Meta:
        verbose_name = "Документ"
        ordering = ('title',)

    title = models.CharField(max_length=255, verbose_name="Назва документу", blank=False)
    document = models.FileField(upload_to='documentation')

    def __str__(self):
        return self.title


class Faq(models.Model):
    class Meta:
        verbose_name = "Типове запитання"
        verbose_name_plural = "Типові запитання"

    question = models.TextField(blank=False, verbose_name="Типове Запитання")
    answer = models.TextField(blank=False, verbose_name="Відповідь")

    def __str__(self):
        return self.question


class Order(models.Model):
    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    ORDER_STATUS_CHOICES = (
        (0, 'Нове'),
        (1, 'Оплачене'),
    )

    user = models.ForeignKey(User, verbose_name='Покупець', on_delete=False)
    journey = models.ForeignKey(Journey, related_name='in_orders', on_delete=False)
    email_address = models.CharField(max_length=255, verbose_name='Email адрес', blank=False)
    contact_phone = models.CharField(max_length=255, verbose_name='Номер телефону', blank=False)
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0])
    total = models.IntegerField(verbose_name='Загальна ціна', null=True)
    persons = models.IntegerField(verbose_name='Люди', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contacted = models.BooleanField(verbose_name="Зконтактовано", default=False)

    def __str__(self):
        return "Order # " + str(self.pk)


class OrderAnonymous(models.Model):
    class Meta:
        verbose_name = "Анонімне замовлення"
        verbose_name_plural = "Анонімні замовлення"

    name = models.CharField(max_length=255, blank=False, verbose_name='ПІБ')
    description = models.TextField(blank=False, verbose_name='Опис')
    person = models.IntegerField(blank=True, verbose_name='Кількість осіб')
    duration = models.IntegerField(blank=False, verbose_name='Тривалість')
    email = models.CharField(max_length=255, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=255, blank=False, verbose_name='Телефон')
    contacted = models.BooleanField(verbose_name="Зконтактовано", default=False)

    def __str__(self):
        return "Order # " + str(self.name)
