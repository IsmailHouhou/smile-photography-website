from django.db import models

# Create your models here.

class Product(models.Model):
    PRODUCT_CATEGORIES = (
        ('Image', 'Image'),
        ('Lightning', 'Lightning'),
        ('Support', 'Support'),
        ('Sound', 'Sound'),
    )
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=PRODUCT_CATEGORIES)
    summary = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    price_day_1 = models.IntegerField()
    price_day_3 = models.IntegerField()
    price_day_10 = models.IntegerField()
    student_promotion = models.IntegerField()

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.product.name


class Video(models.Model):
    VIDEO_CATEGORIES = (
        ('Documentary', 'Documentary'),
        ('Advertisement', 'Advertisement'),
        ('Event', 'Event'),
        ('Reporting', 'Reporting'),
    )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=VIDEO_CATEGORIES)
    client = models.CharField(max_length=200, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def shortDescription(self):
        return self.description[:20]+'...'
    
class Showreel(models.Model):
    thumbnail = models.ImageField()
    video = models.FileField()

    def __str__(self):
        return 'Showreel'
    

class Message(models.Model):
    client_name = models.CharField(max_length=200, null=True, blank=True)
    client_city = models.CharField(max_length=200, null=True, blank=True)
    client_email = models.EmailField(null=True, blank=True)
    client_prefix = models.CharField(max_length=5, null=True, blank=True)
    client_phone = models.IntegerField(null=True, blank=True)

    read = models.CharField(max_length=10, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date_sent = models.DateField(auto_now_add=True, auto_now=False, null=True)
    date_time_sent = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

    def __str__(self):
        return self.client_name + ': ' + str(self.date_sent)
    
    def shortMessage(self):
        return self.message[:20]
    
    def phoneNumber(self):
        return self.client_prefix + str(self.client_phone)
    

class Reservation(models.Model):
    STATUS = (
        ('personal', 'personal'),
        ('business', 'business'),
        ('student', 'student'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    client_name = models.CharField(max_length=200, null=True, blank=True)
    client_email = models.EmailField(null=True, blank=True)
    client_address = models.CharField(max_length=200, null=True, blank=True)
    client_business = models.CharField(max_length=200, null=True, blank=True)
    client_prefix = models.CharField(max_length=5, null=True, blank=True)
    client_phone = models.IntegerField(null=True, blank=True)
    client_status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True)

    read = models.CharField(max_length=10, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    order_date_time = models.DateTimeField(auto_now_add=True, auto_now=False, null=True) # FIX FORMAT TYPE OF DATE
    # order_hour = models.TimeField(auto_now_add=True, auto_now=False, null=True)

    def __str__(self):
        return self.client_name + ' -> ' + self.product.name

    def phoneNumber(self):
        return self.client_prefix + str(self.client_phone)

    def duration(self):
        diff_date = self.end_date - self.start_date
        diff_date_stripped = str(diff_date).split(',', 1)[0]
        return diff_date_stripped

    def total_price(self):
        diff_date = self.end_date - self.start_date
        duration = int(str(diff_date).split(' ', 1)[0])
        promo = self.product.student_promotion*0.01
        day1 = self.product.price_day_1 * duration
        day1_student = day1 - day1*promo
        day3 = self.product.price_day_3 * duration
        day3_student = day3 - day3*promo
        day10 = self.product.price_day_10 * duration
        day10_student = day10 - day10*promo
        if(self.client_status == 'student'):
            if((duration >= 1) and (duration < 3)):
                return "{:0,.2f}".format(float(day1_student))
            elif((duration >= 3) and (duration < 10)):
                return "{:0,.2f}".format(float(day3_student))
            elif(duration >= 10):
                return "{:0,.2f}".format(float(day10_student))
        else:
            if((duration >= 1) and (duration < 3)):
                return "{:0,.2f}".format(float(day1))
            elif((duration >= 3) and (duration < 10)):
                return "{:0,.2f}".format(float(day3))
            elif(duration >= 10):
                return "{:0,.2f}".format(float(day10))

        