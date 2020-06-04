# importing the requests library 
import requests 
from dotenv import load_dotenv
import os

"""
GoogleApi class is used to implement google search api. 
# defining a params dict for the parameters to be sent to the API 
# sending get request and saving the response as response object 
# extracting data in json format 
"""
class GoogleApi:
    def __init__(self):
        load_dotenv()
        # api-endpoint 
        self.API_KEY= os.getenv('API_KEY')
        self.SEARCH_ENGINE_ID= os.getenv('SEARCH_ENGINE_ID')
        self.URL = "https://www.googleapis.com/customsearch/v1"  


    #Used to call search api for the given keyword taken as argument and return first 5 links 
    def callApi(self,keyword):    
        try:
            PARAMS = {'key':self.API_KEY,'cx':self.SEARCH_ENGINE_ID,'q':keyword}  
            r = requests.get(url = self.URL, params = PARAMS) 
            data = r.json() 
        except:
            return "Network Issue"   
        
        ans=[]
        for i in data['items']:
            ans.append(i["link"])

        return '\n'.join(ans[:5])    
