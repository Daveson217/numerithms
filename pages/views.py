# Create your views here.
from django.views.generic import TemplateView

# Django
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# App
from .utils import fractional_knapsack, job_sequencing_with_deadline
from .forms import FractionalKnapsackForm, JobSequencingDeadlineForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class FractionalKnapsackView(TemplateView):
    template_name = 'algorithms_analysis/fractional_knapsack.html'
  
class JobSequencingView(TemplateView):
    template_name = 'algorithms_analysis/job_sequencing.html'
   

def fractional_knapsack_handler(request):
    form = FractionalKnapsackForm()
    data = dict()
    solution = tuple()
    
    if request.method=='GET':
        request_data = request.GET           
        profits = request_data.get('profits')
        profits = profits.split(',')
        profits = [int(profit) for profit in profits]
        
        weights = request_data.get('weights')
        weights = weights.split(',')
        weights = [int(weight) for weight in weights]
        
        max_weight = request_data.get('max_weight')
        max_weight = int(max_weight)
        
        solution = fractional_knapsack(profits, weights, max_weight)
        data['items'] = solution[1]
        data['message'] = solution[0]  
    return JsonResponse(data)

def job_sequencing_handler(request):
    form = JobSequencingDeadlineForm()
    data = dict()
    solution = tuple()
    
    if request.method=='GET':
        request_data = request.GET           
        jobs = request_data.get('jobs')
        jobs = jobs.split(',')   
        
        deadlines = request_data.get('deadlines')
        deadlines = deadlines.split(',')
        deadlines = [int(deadline) for deadline in deadlines]
        
        profits = request_data.get('profits')
        profits = profits.split(',')
        profits = [int(profit) for profit in profits]
        
        
        solution = job_sequencing_with_deadline(jobs, deadlines, profits)
        data['job_sequence_msg'] = solution[0]
        data['max_profit'] = solution[1]        

    return JsonResponse(data)
    