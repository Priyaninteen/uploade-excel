from django.shortcuts import render
from django.http import JsonResponse
from .models import UploadeFile
import pandas as pd
import json, os
from Mysql.settings import BASE_DIR

def insert(request):
    if request.method == 'POST':
        data=request.FILES["excel_file"]
        path=str(BASE_DIR)+"/uploade_file"
        if os.path.exists(path):
            if os.path.exists(path+"/"+str(data)):
                return JsonResponse({"status":False,"msg":"File already uploaded"})
        
        b=UploadeFile(
            file_path=data
        )
        b.save()

        return JsonResponse({"status":True,"msg":"file uploaded"})

    else:
       return JsonResponse({"status":False,"msg":"Method not allow"}) 


def excel_file(request):
    if request.method == "GET":

         a=UploadeFile.objects.all().values('file_path')

         json_data={}

         for i in a:
            excel_data_df = pd.read_excel(str(BASE_DIR)+"/uploade_file/"+i['file_path']) 

            json_d=excel_data_df.assign(**excel_data_df.select_dtypes(['datetime']).astype(str).to_dict('list')).to_json(orient='records')

            json_data[i['file_path']]=json.loads(json_d)

            return JsonResponse({"status":True,"data":json_data})

    else:
        return JsonResponse({"status":False,"msg":"Method not allow"})
