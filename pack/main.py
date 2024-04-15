
import requests
import pandas as pd
import numpy as np
from collections import Counter
from pack.utils.siblings import SibInfo
from pack.utils.heatmap import Heatmap

def work_search(query, field_id):
    endpoint_url = 'https://api.openalex.org/works'
    
    qp1 = f'?page=1&per-page=200&filter=primary_topic.field.id%3A'
    
    field_parameters = [f'fields%2F{i}' for i in SibInfo(field_id).sfield_id] + [f'fields%2F{field_id}']
    
    seperator = "|"

    #qp3 = f',default.search%3A{query}'
    qp3 = f",title_and_abstract.search%3A{query}"
    
    # sorting by citation count in descending order (by default sort by relevance score)
    qp4 = f'&sort=cited_by_count%3Adesc'

    url = endpoint_url + qp1 + seperator.join(field_parameters) + qp3 + qp4

    req = requests.get(url)
    res = req.json()
    
    work_titles = [result["display_name"] for result in res["results"][:10]]
    work_count = [result["cited_by_count"] for result in res["results"][:10]]
    work_url = [result["id"] for result in res["results"][:10]]
    summary = zip(work_titles, work_url, work_count)
    
    # Work Summary
    for i,j,k in summary:
        
        if i == work_titles[0]:
            print(f'# of Papers = {res["meta"]["count"]}\n\n{"Work Titles":110s}{"URL":40s}{"Citations":10s}\n{i:110s}{j:40s}{k:10d}')
        
        else:
            print(f'{i:110s}{j:40s}{k:10d}')
                
    
    # Authorships
    authorship = [result['authorships'] for result in res['results']]
    authors = [authorship[i][j]['author']['display_name'] for i in range(len(authorship)) for j in range(len(authorship[i]))]
    author_ids = [authorship[i][j]['author']['id'] for i in range(len(authorship)) for j in range(len(authorship[i]))]
    
    df_data = pd.DataFrame({"IDs":author_ids}, index = authors)

    # Remove duplicate index values
    df_data = df_data[~df_data.index.duplicated(keep='first')]

    # Authors ranked by works count
    author_count = dict(Counter(authors))
    top_authors = list(author_count.keys())
    ta_counts = list(author_count.values())

    df = pd.DataFrame({'Works':ta_counts}, index = top_authors)
    df = df.sort_values(by = 'Works', ascending = False)[:15]

    # Map URLs form raw author data to sorted DataFrame with top 10 authors
    df['URL'] = df_data.loc[df.index, 'IDs'] 
    
    ta = np.array(df.index).reshape((3,5))
    ta_count = np.array(df['Works']).reshape((3,5))
    ta_url = np.array(df['URL']).reshape((3,5))
    
    # First-named author institutions and counts
    cai = []
    cai_info = [authorship[i][0]['institutions'][:1] for i in range(len(authorship))]
    for i in range(len(cai_info)):
        if len(cai_info[i]) != 0:
            temp = cai.append(cai_info[i][0]['display_name'])
        else:
            continue # bypass instances of empty institutional display names
    num_cai = dict(Counter(cai))
    cai_9 = dict(sorted(num_cai.items(), key = lambda item: item[1], reverse = True)[:15])
    Institutions = np.array(list(cai_9.keys())).reshape((3,5))
    Ins_count = np.array(list(cai_9.values())).reshape((3,5))
    
    # Publication sources and counts
    source_count = dict(Counter([res['results'][i]['primary_location']['source']['display_name'] for i in range(len(res['results']))]))
    source_9 = dict(sorted(source_count.items(), key = lambda item: item[1], reverse = True)[:15]) # sort dictionary by keys in descending order and return top 10
    
    publisher = np.array(list(source_9.keys())).reshape((3,5))
    publisher_count = np.array(list(source_9.values())).reshape((3,5))
    
    
   # return Heatmap(publisher_count, Ins_count, source_9, cai_9, publisher, Institutions), print(df)
    return  Heatmap(publisher_count, ta, ta_count, ta_url, Ins_count, source_9, cai_9, publisher, Institutions)
