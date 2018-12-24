from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    ticket1_count = models.PositiveIntegerField(default=0)
    ticket2_count = models.PositiveIntegerField(default=0)
    ticket3_count = models.PositiveIntegerField(default=0)
    ticket4_count = models.PositiveIntegerField(default=0)
    ticket5_count = models.PositiveIntegerField(default=0)
    ticket6_count = models.PositiveIntegerField(default=0)
    level         = models.PositiveIntegerField(default=1)
    game_won = models.PositiveIntegerField(default=0)
    game_played = models.PositiveIntegerField(default=0)
    profile_pic = models.FileField(default=None,upload_to='Profile Pictures',blank=True,null=True)
    coins_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    def __str__(self):
        return self.first_name


class Transaction(models.Model):
    request_date = models.DateTimeField()
    amount = models.PositiveIntegerField(default=0)
    status = models.PositiveIntegerField(choices=((1, 'Approved'), (2, 'pending')))
    approved_date = models.DateTimeField()
    Account_Name = models.CharField(max_length=50)
    IBAN_number = models.CharField(max_length=24)
    t_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
