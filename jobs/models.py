from django.db import models
import uuid
from candidates.models import CandidateModel

class JobModel(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    role = models.CharField(max_length=50, blank=False, null=False)
    location = models.CharField(max_length=50, blank=False, null=False)
    minimim_salary = models.IntegerField(default=0)
    maximum_salary = models.IntegerField(default=0)
    target_date_to_finish_hiring = models.DateField(null=True, blank=True)
    job_description = models.TextField() # Text field for long texts
    is_active = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = 'Jobs'


class JobApplicationModel(models.Model):
    '''
    Importing Foreign key from above Job Table.
    Need to specify what to do when the referenced object is deleted. 
    For example, you can set it to models.CASCADE, 
    which will delete all related objects when the referenced object is deleted.
    '''
    job_id = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    candidate_id = models.ForeignKey(CandidateModel, on_delete=models.CASCADE) # Importing Foreign key from different app "candidates"
    is_active = models.BooleanField(default=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Job Application"
        verbose_name_plural = 'Job Applications'
