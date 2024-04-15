import requests

class FieldInfo:

    def __init__(self):
        req = requests.get('https://api.openalex.org/fields?page=1&per-page=200')
        res = req.json()

        self.fields = [result['display_name'] for result in res['results']]
        self.field_url = [result["id"] for result in res['results']]
        self.fields_id = [result["id"][-2:] for result in res['results']] # Get numerical ids of fields as strings
        self.finfo = zip(self.fields, self.fields_id, self.field_url)
    
    
    def field_info(self):  
    # Adding print statements based on conditions to generate a table of fields information
        field_info = ""
        
        for i,j,k in self.finfo:
            
            if i == self.fields[0]:
                line = f'{"Fields":50s}{"ID":10s}{"URL":50s}\n{i:50s}{j:10s}{k:50s}\n'
        
            elif i != self.fields[-1]:
                line = f'{i:50s}{j:10s}{k:50s}\n'
        
            else:
                line = f'{i:50s}{j:10s}{k:50s}\n\nNumber of fields = {len(self.fields)}'
                
            field_info += line
            
        return field_info 
