"""Class object for getting information on work fields."""

import requests


class FieldInfo:
    """
    A class to represent OpenAlex fields.

    ...

    Attributes
    ----------
    fields: str
        List of OpenAlex fields
    field_id: str
        List of OpenAlex ids for each field
    field_url: str
        List of OpenAlex URLs for each field
    info: str
        Printed table of all fields, their corresponding
        ids, and URLs

    """

    def __init__(self):
        """
        Construct all attributes for the FieldInfo object.

        Parameters
        ----------
        self: An instance of FieldInfo
        """
        req = requests.get("https://api.openalex.org/fields?page=1&per-page=200")
        res = req.json()

        self.fields = [result["display_name"] for result in res["results"]]
        self.field_url = [result["id"] for result in res["results"]]
        self.field_id = [
            result["id"][-2:] for result in res["results"]
        ]  # Get numerical ids of fields as strings
        self.info = zip(self.fields, self.field_id, self.field_url)

    def field_info(self):
        """
        Print statements to generate a table of fields information.

        Parameters
        ----------
        self: An instance of FieldInfo

        Returns
        -------
        field_info: A structured tabular printing of fields, their
        corresponding ids, and URLs
        """
        field_info = ""

        for i, j, k in self.info:

            if i == self.fields[0]:
                line = f'{"Fields":50s}{"ID":10s}{"URL":50s}\n{i:50s}{j:10s}{k:50s}\n'

            elif i != self.fields[-1]:
                line = f"{i:50s}{j:10s}{k:50s}\n"

            else:
                line = f"{i:50s}{j:10s}{k:50s}\n\nNumber of fields = {len(self.fields)}"

            field_info += line

        return print(field_info)
