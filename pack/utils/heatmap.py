
import plotly.graph_objects as go

def Heatmap(publisher_count, ta, ta_count, ta_url, Ins_count, source_15, cai_15, publisher, Institutions):

    # Create the heatmap
    fig = go.Figure(data = go.Heatmap(
                    z=publisher_count,
                    hovertemplate='Z: %{z}',
                    text=publisher, 
                    texttemplate="%{text}",
                    textfont={"size":10},
                    colorbar={"title":"Frequency"},
                    colorscale = 'Viridis'))
    
    fig2 = go.Figure(data = go.Heatmap(
                    z=Ins_count,
                    hovertemplate='Z: %{z}',
                    text=Institutions, 
                    texttemplate="%{text}",
                    textfont={"size":10},
                    colorbar={"title":"Frequency"},
                    colorscale = 'Blackbody'))
    
    # Define hover information with URLs
    hover_text = [[f'<a href="{name}" target="_blank" style="color:#FFFFFF">{url}</a>' for name, url in zip(ta,row)] for row,ta in zip(ta,ta_url)]
    
    fig3 = go.Figure(data = go.Heatmap(
                    z=ta_count,
                    text=hover_text, 
                    hovertemplate='Z: %{z}',        
                    customdata = ta_url,
                    texttemplate="%{text}",
                    textfont={"size":12},
                    colorbar={"title":"Frequency"},
                    colorscale = 'Bluered'))

    # Update figure layouts
    fig.update_layout(
        height = 410,
        width = 1350,
        xaxis1=dict(showticklabels=False, showline=False),
        yaxis1=dict(showticklabels=False, showline=False),
        xaxis2=dict(showticklabels=False, showline=False),
        yaxis2=dict(showticklabels=False, showline=False),
        title = "Top Journals"
    )
    
    fig2.update_layout(
        height = 410,
        width = 1350,
        xaxis1=dict(showticklabels=False, showline=False),
        yaxis1=dict(showticklabels=False, showline=False),
        xaxis2=dict(showticklabels=False, showline=False),
        yaxis2=dict(showticklabels=False, showline=False),
        title = "Top Institutions"
    )
    
    fig3.update_layout(
        height = 410,
        width = 1350,
        xaxis1=dict(showticklabels=False, showline=False),
        yaxis1=dict(showticklabels=False, showline=False),
        xaxis2=dict(showticklabels=False, showline=False),
        yaxis2=dict(showticklabels=False, showline=False),
        title = "Top Authors"
    )
    
    # Show the plots
    fig.show()
    fig2.show()
    fig3.show()
