"""Function for converting JSON data into descriptive heatmaps."""

import plotly.graph_objects as go


def Heatmap(publisher, publisher_count, institutions, ins_count, ta, ta_count, ta_url):
    """
    Process JSON data into heatmaps summarizing the data.

        Parameters:
            publisher: An array of shape (3,5) of the top 15
            journals/publishers by works from the users work search query
            publisher_count: An array of shape (3,5) of the works count
            of the top 15 journals/publishers
            institutions: An array of shape (3,5) of the top 15
            institutions by work count from the users work search query
            ins_count: An array of shape (3,5) of the work counts of the
            top 15 institutions
            ta: An array of shape (3,5) of the top 15 authors by work
            count from the users work search query
            ta_count: An array of shape (3,5) of the work counts of the
            top 15 authors
            ta_url: An array of shape (3,5) of the OpenAlex URLS of the
            top 15 authors

        Returns:
            3 Plotly heat maps that showcasing publishers, intitutions,
            and authors
    """
    # Create the heatmap depicting top 15 publisher/sources
    fig = go.Figure(
        data=go.Heatmap(
            z=publisher_count,
            hovertemplate="Z: %{z}",
            text=publisher,
            texttemplate="%{text}",
            textfont={"size": 10},
            colorbar={"title": "Frequency"},
            colorscale="Viridis",
        )
    )

    # Create the heatmap depicting top 15 affiliated Institutions
    fig2 = go.Figure(
        data=go.Heatmap(
            z=ins_count,
            hovertemplate="Z: %{z}",
            text=institutions,
            texttemplate="%{text}",
            textfont={"size": 10},
            colorbar={"title": "Frequency"},
            colorscale="Blackbody",
        )
    )

    # Define hover information with URLs embedded and clickable,
    # taking the user to the OpenAlex author page
    hover_text = [
        [
            f'<a href="{name}" target="_blank" style="color:#FFFFFF">{url}</a>'
            for name, url in zip(ta, row)
        ]
        for row, ta in zip(ta, ta_url)
    ]

    # Create the heatmap depicting top 15 cited authors
    fig3 = go.Figure(
        data=go.Heatmap(
            z=ta_count,
            text=hover_text,
            hovertemplate="Z: %{z}",
            customdata=ta_url,
            texttemplate="%{text}",
            textfont={"size": 12},
            colorbar={"title": "Frequency"},
            colorscale="Bluered",
        )
    )

    # Update figure layouts
    fig.update_layout(
        height=410,
        width=1350,
        xaxis1=dict(showticklabels=False, showline=False),
        yaxis1=dict(showticklabels=False, showline=False),
        xaxis2=dict(showticklabels=False, showline=False),
        yaxis2=dict(showticklabels=False, showline=False),
        title="Top Journals",
    )

    fig2.update_layout(
        height=410,
        width=1350,
        xaxis1=dict(showticklabels=False, showline=False),
        yaxis1=dict(showticklabels=False, showline=False),
        xaxis2=dict(showticklabels=False, showline=False),
        yaxis2=dict(showticklabels=False, showline=False),
        title="Top Institutions",
    )

    fig3.update_layout(
        height=410,
        width=1350,
        xaxis1=dict(showticklabels=False, showline=False),
        yaxis1=dict(showticklabels=False, showline=False),
        xaxis2=dict(showticklabels=False, showline=False),
        yaxis2=dict(showticklabels=False, showline=False),
        title="Top Authors",
    )

    # Show the plots
    fig.show()
    fig2.show()
    fig3.show()
