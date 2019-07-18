from django.db import models
from datetime import timedelta, datetime, date
from django.utils.encoding import smart_text
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.utils.timesince import timesince

def validate_author_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("Not a valid email!!!!!")

def validate_chris(value):
    if "chris" in value:
        return value
    else:
        raise ValidationError("Chris not in value!!!!!")


PUBLISH_CHOICES = (
    ('draft', "Draft"),
    ('publish', "Publish"),
    ('private', "Private"),
)

class PostQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class PostManager(models.Manager):
    #wrap queryset
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    #OVERRIDE the all() call
    def all(self, *args, **kwargs):
        #get only active posts
        #qs = super(PostManager, self).all(*args, **kwargs).active() #filter(active=True)
        qs = super(PostManager, self).all(*args, **kwargs).filter(active=True)

        #print(qs)
        return qs

class Post(models.Model):
    #ID
    #id = models.AutoField(primary_key=True)
    id = models.BigAutoField(primary_key=True)
    #BOOLEAN
    active = models.BooleanField(default=True)
    #CHARFIELD
    #title = models.CharField(max_length=120, default='New Title')
    # title = models.CharField(max_length=120, unique=True, null=True, verbose_name="Post Title") # can be empty
    #OVERRIDING ERROR MESSAGES
    title = models.CharField(
        max_length=120,
        unique=True,
        null=True,
        verbose_name="Post Title",
        error_messages={
            "unique": "This title is not unique!!!" #apare in modelforms
        },
        help_text='Must be a unique title') #apare in modelforms
    #TEXTFIELD
    content = models.TextField(null=True, blank=True) # blank for model forms
    #CHOICES
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    # IN BUILT VALIDATION
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    # Custom Validation
    #author_email = models.CharField(max_length=220, validators=[validate_author_email, validate_chris], null=True, blank=True)
    author_email = models.EmailField(max_length=220, validators=[validate_chris], null=True, blank=True)
    # OVERRIDING SAVE METHOD UTILITIES SLUG
    slug = models.SlugField(null=True, blank=True) #editable=False
    # TIMESTAMP and DATETIMEFIELD
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostManager() # integrate PostManager
    objects = PostManager() # can call like Post.other.all(), Post.other.create('latitle')

    ### OVERRIDING SAVE (Don't do it. Use better pre save, post save)
    def save(self, *args, **kwargs): #title1, title2, key1=None, key2=None etc.
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        print("I am saving!!!!!")
        # self.title = 'Universal title'
        super(Post, self).save(*args, **kwargs)

    def __str__(self): # python 3
        #return self.title
        return smart_text(self.title) #for chineese, etc..can be used in other places

    @property # can be treated like any property: title, active
    def age(self):
        if self.publish == 'publish':
            now = datetime.now()
            publish_time = datetime.combine(
                                self.publish_date,
                                datetime.now().min.time()
                        )
            try:
                difference = now - publish_time
            except:
                return "Unknown"
            if difference <= timedelta(minutes=1):
                return 'just now'
            return '{time} ago'.format(time= timesince(publish_time).split(', ')[0])
        return "Not published"


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
### SIGNALS ######
#BEFORE SAVE
def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    # ex. create new model
    print("BEFORE SAVE!!!!!!!!")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)
pre_save.connect(blog_post_model_pre_save_receiver, sender=Post)

#AFTER SAVE
def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("AFTER SAVE!!!!!!!")
    print(created) #boolean
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()
post_save.connect(blog_post_model_post_save_receiver, sender=Post)
