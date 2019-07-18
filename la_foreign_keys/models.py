from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

##################### FOREIGN KEYS #####################
# One car can have 1 user. But 1 user can have many cars (ForeignKey = ManyToOneField)
class Car(models.Model):
    # If I have the user object I can get the car
    # If I have the car object I can get the user
    # by default the ForeignKey of user have related_name='car_set'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="upd_car_user")

    def __str__(self):
        return self.name

################### RELATED NAME ####################
# If I have more than 1 ForeignKey(User) use related_name
# Car.objects.filter(updated_by__username='chrispsk')
# OR
# eu = User.objects.first()
# eu.upd_car_user.all()
############### import Car ##########################
# Car.objects.all()
# obj = Car.objects.first()
# obj.user # <User: chrispsk>
# obj.user.username # 'chrispsk'
# obj.user.password
# obj.user.email
# obj.user.__class__ # <class 'django.contrib.auth.models.User'>
# obj.user.__class__.objects.all() # <QuerySet [<User: chrispsk>, <User: sam>]>
# alt = obj.user.__class__.objects.last() # <User: sam>

################# import User ######################
# User.objects.all() #<QuerySet [<User: chrispsk>, <User: sam>]>
# eu = User.objects.first()
# eu.car_set.all() # Get all cars of chrispsk
# eu.car_set.first() # Get first car of chrispsk

############### CHANGE CAR FORM SAM TO CHRISPSK ###############
# car_obj = Car.objects.last()
# car_obj.user # <User: sam>
# el = car_obj.user.__class__
# el # <class 'django.contrib.auth.models.User'> OR
# el = get_user_model() # <class 'django.contrib.auth.models.User'>

# car_obj.user # <User: sam>

# chrispsk = el.objects.all().first() # <User: chrispsk>
# sam = el.objects.all().last() # <User: sam>
# car_obj # <Car: Car 3>
# car_obj.user # <User: sam>
# car_obj.user = chrispsk
# car_obj.save()

# Get all cars of chrispsk !!!!!!!!!!!!!!!!!
# Car.objects.filter(user__username='chrispsk')
# Car.objects.filter(user__username__icontains="chri")

##################### ManyToManyField #####################

class Bike(models.Model):
    drivers = models.ManyToManyField(User)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

# Bike.objects.all() #<QuerySet [<Bike: bike 1>, <Bike: bike 2>, <Bike: bike 3>]>
# bike1 = Bike.objects.all().first() # <Bike: bike 1>
# bike1.drivers
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<lo
# cals>.ManyRelatedManager object at 0x0000000003DCD940>

# return Users of bike1
# bike1.drivers.all() # <QuerySet [<User: chrispsk>, <User: sam>]>

# get chrispsk user
# user_qs = bike1.drivers.all()
# chrispsk = user_qs.first()

# get all bikes of chrispsk user
# chrispsk.bike_set.all() # <QuerySet [<Bike: bike 1>, <Bike: bike 2>]>
# OR
# Bike.objects.filter(drivers=chris) # <QuerySet [<Bike: bike 1>, <Bike: bike 2>]>

# with duplicates
# list_users = bike1.drivers.all()
# Bike.objects.filter(drivers__in=list_users) # <QuerySet [<Bike: bike 1>, <Bike: bike 2>, <Bike: bike 1>, <Bike: bike 3>]>

# no duplicates
# list_users = bike1.drivers.all()
# Bike.objects.filter(drivers__in=list_users).distinct()

####################### ONETOONEFIELD (unique=True)##############
# __set don't apply. Can do it without using it.
# VERY LIMITED
# 1 user can have be associated to only 1 bike
# 1 bike can be associated to only 1 user

# Can use it for
# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     city
#     image
