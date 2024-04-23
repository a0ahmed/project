"""A module for summarizing works information for a search request."""

import requests
import pandas as pd
import numpy as np
from collections import Counter
from pack.utils.fields import FieldInfo
from pack.utils.siblings import SibInfo
from pack.utils.heatmap import Heatmap


def work_search(query, field_id):
    """
    Return a visual summary of the search query.

        Parameters
        ----------
        query: str
            key words and phrases
        field_id: int
            An OpenAlex field id

        Returns
        -------
        Heatmap(): Heat maps of the top 15 journals, institutions, and
                   authors by work counts of the work_search query
    """
    if str(field_id) in FieldInfo().field_id:
        endpoint_url = "https://api.openalex.org/works"

        # Filter by field
        qp1 = "?page=1&per-page=200&filter=primary_topic.field.id%3A"

        # Join all related fields and the selected field to the filter URL
        field_parameters = [f"fields%2F{i}" for i in SibInfo(field_id).field_id] + [
            f"fields%2F{field_id}"
        ]

        seperator = "|"

        # Filter search by title and abstract
        qp3 = f",title_and_abstract.search%3A{query}"

        # Sort by citation count in descending order
        qp4 = "&sort=cited_by_count%3Adesc"

        # Concatenate all URL components
        url = endpoint_url + qp1 + seperator.join(field_parameters) + qp3 + qp4

        req = requests.get(url)
        res = req.json()

        work_titles = [result["display_name"] for result in res["results"][:10]]
        work_count = [result["cited_by_count"] for result in res["results"][:10]]
        work_url = [result["id"] for result in res["results"][:10]]
        summary = zip(work_titles, work_url, work_count)

        # Work summary printed upon function call
        for i, j, k in summary:

            if i == work_titles[0]:
                print(f'# of Papers = {res["meta"]["count"]}')
                print(
                    f'\n{"Work Titles":110s}{"URL":40s}{"Citations":10s}\n{i:110s}{j:40s}{k:10d}'
                )

            else:
                print(f"{i:110s}{j:40s}{k:10d}")

        if res["meta"]["count"] >= 15:
            # List comprehension to get authors and the OpenAlex author URLs
            authorship = [result["authorships"] for result in res["results"]]
            authors = [
                authorship[i][j]["author"]["display_name"]
                for i in range(len(authorship))
                for j in range(len(authorship[i]))
            ]
            author_ids = [
                authorship[i][j]["author"]["id"]
                for i in range(len(authorship))
                for j in range(len(authorship[i]))
            ]

            df_data = pd.DataFrame({"IDs": author_ids}, index=authors)

            # Remove duplicate index values, returning all unique author names
            df_data = df_data[~df_data.index.duplicated(keep="first")]

            # Rank authors by works count
            author_count = dict(Counter(authors))
            top_authors = list(author_count.keys())
            ta_counts = list(author_count.values())

            # Create a DataFrame of authors and works count for the top 15
            # authors with the highest works count
            df = pd.DataFrame({"Works": ta_counts}, index=top_authors)
            df = df.sort_values(by="Works", ascending=False)[:15]

            # Map URLs from raw author data to sorted DataFrame with top 15
            # authors
            df["URL"] = df_data.loc[df.index, "IDs"]

            # Convert top author names, works counts, and URLs to numpy arrays
            # of size (3,5)
            ta = np.array(df.index).reshape((3, 5))
            ta_count = np.array(df["Works"]).reshape((3, 5))
            ta_url = np.array(df["URL"]).reshape((3, 5))

            # First-named author institutions and counts
            cai_info = []
            for i in range(len(authorship)):
                if len(authorship[i]) != 0:
                    cai_info.append(authorship[i][0]["institutions"][:1])
                else:
                    continue  # bypass instances of empty authorship

            # Initialize and store
            cai = []
            for i in range(len(cai_info)):
                if len(cai_info[i]) != 0:
                    cai.append(cai_info[i][0]["display_name"])
                else:
                    # bypass instances of empty institutional display names
                    continue

            num_cai = dict(Counter(cai))
            cai_15 = dict(
                sorted(num_cai.items(), key=lambda item: item[1], reverse=True)[:15]
            )
            institutions = np.array(list(cai_15.keys())).reshape((3, 5))
            ins_count = np.array(list(cai_15.values())).reshape((3, 5))

            # Publication sources (journals) and counts
            source_count = []
            for i in range(len(res["results"])):

                if res["results"][i]["primary_location"]["source"] is None:
                    continue
                else:
                    source_count.append(
                        res["results"][i]["primary_location"]["source"]["display_name"]
                    )

            source_count = dict(Counter(source_count))
            source_15 = dict(
                sorted(source_count.items(), key=lambda item: item[1], reverse=True)[
                    :15
                ]
            )  # sort dictionary by keys in descending order and return top 15

            publisher = np.array(list(source_15.keys())).reshape((3, 5))
            publisher_count = np.array(list(source_15.values())).reshape((3, 5))

            return Heatmap(
                publisher,
                publisher_count,
                institutions,
                ins_count,
                ta,
                ta_count,
                ta_url,
            )

        else:
            return "Insufficient Works"

    else:
        return "Invalid ID"
