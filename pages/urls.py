from django.urls import path

from .views import HomePageView, FractionalKnapsackView, fractional_knapsack_handler, JobSequencingView, job_sequencing_handler

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    
    path('fractional_knapsack/', FractionalKnapsackView.as_view(), name='fractional_knapsack'),    
    path('fractional_knapsack/handler/', fractional_knapsack_handler, name='fractional_knapsack_handler'),
    
    path('job_sequencing/', JobSequencingView.as_view(), name='job_sequencing'),    
    path('job_sequencing/handler/', job_sequencing_handler, name='job_sequencing_handler'),
]
