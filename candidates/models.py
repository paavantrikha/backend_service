from django.db import models
import uuid
'''For the following to work, run following commands on terminal:-
    # pip install phonenumbers
    # pip install django-phonenumber-field
'''
from phonenumber_field.modelfields import PhoneNumberField

class CandidateModel(models.Model):
    candidate_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    dob = models.DateField()
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    phone_no = PhoneNumberField() # pip install phonenumbers
    location = models.CharField(max_length=50, blank=False, null=False)
    professional_experience = models.IntegerField()
    is_active = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = 'Candidates'

# get list post create put update del destroy
