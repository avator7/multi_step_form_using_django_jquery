from rest_framework import routers
from django.urls import path, include
from management.views import *

urls = [
    # health check
    # models handle with web View urls
    path('mangement/health/', getadminhealth),
    path('mangement/multistepform/', multi_step_form),
    path('mangement/saveform/', save_form),

]