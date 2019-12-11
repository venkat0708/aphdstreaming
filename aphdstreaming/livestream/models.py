from django.db import models
from aphdstreaming.core.models import BaseEntity
from django.core.validators import RegexValidator

import random
import string
# Create your models here.

def stream_directory_path(event, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'stream_{0}/{1}'.format(event.Stream_Key, filename)

def images_stream_directory_path(image, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'stream_{0}/{1}'.format(image.event.Stream_Key, filename)

def randomString(len = 12):
    """Generate a random string of letters, digits and special characters """

    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(20))

class Event(BaseEntity):
    """ Event is a single live stream that can
        can be carried out"""
    STATUS_CHOICES=(
        ('CREATED', 'created'),
        ('CONFIRMED', 'Confirmed'),
        ('INPROGRESS', 'Inprogress'),
        ('COMPLETED', 'Completed')
    )

    Bride = models.CharField(
		max_length=80,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='name should contain only alphabets',
				code='invalid_name'
			),
		]
	)
    Groom = models.CharField(
		max_length=80,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='name should contain only alphabets',
				code='invalid_name'
			),
		]
	)
    Message = models.CharField(
		max_length=80,
		validators=[
			RegexValidator(
            	regex='^[a-zA-Z\s]*$',
             	message='message should contain only alphabets',
				code='invalid_name'
			),
		]
	)
    time = models.DateTimeField(
        verbose_name='Event Time',
        )
    status = models.CharField(
        max_length =15,
        choices = STATUS_CHOICES,
        default = 'CREATED',
    )
    Bride_Img = models.ImageField(
        upload_to=stream_directory_path,
        blank=True,
        null=True,
        )
    Groom_Img = models.ImageField(
        upload_to=stream_directory_path,
        blank=True,
        null=True,
        )
    Poster_Img = models.ImageField(
        upload_to=stream_directory_path,
        blank=True,
        null=True,
        )
    Studio = models.CharField(
		max_length=80,
	)
    Stream_Key = models.CharField(
		max_length=80,
        editable = False,
	)
    start_date_time = models.DateTimeField(
        verbose_name='Start Date Time',
        )

    end_date_time = models.DateTimeField(
        verbose_name='End Date Time',
        )
    studio_person = models.CharField(
		max_length=80,
        blank =True,
        null = True,
	)
    studio_phone = models.CharField(
		max_length=13,
        blank = True,
        null = True,
		validators=[
        RegexValidator(
            regex='^[0-9]{10}$',
            message='Phone number should contain only 10 numbers',
			code='invalid Phone number'
			),
    	]
	)
    studio_email = models.EmailField(
        max_length = 254,
        blank = True,
        null = True
    )



    def save(self, *args, **kwargs):
        if not self.Stream_Key:
            self.Stream_Key = randomString()
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        bride = self.Bride.replace(" ", "")
        groom = self.Groom.replace(" ", "")
        msg = self.Message.replace(" ", "")
        return bride+msg+groom


class Image(BaseEntity):
    """Images for Carousel of an event """
    event = models.ForeignKey(
        Event,
        related_name='images',
        on_delete=models.CASCADE
    )

    photo = models.ImageField(
        upload_to=images_stream_directory_path,
        blank=True,
        null=True,
        )
