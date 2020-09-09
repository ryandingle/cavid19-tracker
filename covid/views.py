from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.core import serializers
from .models import Covid
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone 

import requests
import pandas as pd

@method_decorator(csrf_exempt, name='dispatch')
class V1(View):

    template_name = 'covid/index.html'
    
    def get(self, request):
        # check existing data if laps an hour
        check = Covid.objects.all()[:1]
        
        last_updated = check[0].updated_date
        new_date = timezone.now()
        diff = new_date - last_updated
        hours = diff.total_seconds() / 3600

        # check if updated time is greater than 1 hour then update the database table data
        if hours > 1:
            # covid ppublic api
            covid_api_endpoint = 'https://coronavirus-19-api.herokuapp.com/countries'

            # get dataset from api endpoint via restful api get request method and convert to json format
            get_dataset = requests.get(covid_api_endpoint)
            dataset = get_dataset.json()
            
            # Truncate the table
            Covid.truncate()

            # Loop each data to insert into the database
            # In case that the data needs to used by other team it can be get to the database or directly to the api endpoint
            for data in dataset:
                Covid(country=data['country'], cases=data['cases'], todayCases=data['todayCases'], deaths=data['deaths'], todayDeaths=data['todayDeaths'], recovered=data['recovered'], active=data['active'], critical=data['critical'], casesPerOneMillion=data['casesPerOneMillion'], deathsPerOneMillion=data['deathsPerOneMillion'], totalTests=data['totalTests'], testsPerOneMillion=data['testsPerOneMillion']).save()

        
        data_response = {
            'dataset': Covid.objects.all(), 
            'records': Covid.objects.count 
        }

        return render(request, self.template_name, data_response)
        # return JsonResponse({'data': dataset, 'records': len(dataset)}, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class V2(View):
    # too be able to use the data to load for some reporting tool like power bi, qliksense, qlikview etc..
    def get(self, request):
        # convert queryset into pandas dataframe
        queryset = Covid.objects.values('country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered', 'active', 'critical', 'casesPerOneMillion', 'deathsPerOneMillion', 'totalTests', 'testsPerOneMillion','updated_date')
        df = pd.DataFrame(list(queryset))

        # convert response into file download attachment
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=covid-world-data.csv'

        # convert dataframe into csv
        df.to_csv(path_or_buf=response,sep=';',index=False)

        return response