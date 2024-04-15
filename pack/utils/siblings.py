
import requests

class SibInfo:
    
    def __init__(self,id):
        
        fields = (requests.get('https://api.openalex.org/fields?page=1&per-page=200')).json()
        allowed_ids = list(map(int, [result["id"][-2:] for result in fields['results']]))
        
        if not isinstance(id, int):
            raise ValueError("ID must be an integer")
            
        if id not in allowed_ids:
            raise ValueError("The ID does not exist.")
    
        req = requests.get(f'https://api.openalex.org/fields/{id}?page=1&per-page=200')
        res = req.json()

        self.fields = [result['display_name'] for result in res['siblings']]
        self.field_url = [result["id"] for result in res['siblings']]
        self.field_id = [result["id"][-2:] for result in res['siblings']] # Get numerical ids of fields as strings
        self.info = zip(self.fields, self.field_id, self.field_url)

    def sib_info(self):  
    # Adding print statements based on conditions to generate a table of fields information
        sib_info = ""
        
        for i,j,k in self.info:
            
            if i == self.fields[0]:
                line = f'{"Fields":50s}{"ID":10s}{"URL":50s}\n{i:50s}{j:10s}{k:50s}\n'
        
            elif i != self.fields[-1]:
                line = f'{i:50s}{j:10s}{k:50s}\n'
        
            else:
                line = f'{i:50s}{j:10s}{k:50s}\n\nNumber of Sibling fields = {len(self.fields)}'
                
            sib_info += line
                
        return sib_info
    
