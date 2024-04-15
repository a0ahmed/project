
import plotly.graph_objects as go

def Heatmap(publisher_count, ta, ta_count, ta_url, Ins_count, source_9, cai_9, publisher, Institutions):

    # Convert dictionary to a 2D array (matrix)
    matrix1 = publisher_count
    matrix2 = Ins_count
    matrix3 = ta_count

    # Create the heatmap
    fig = go.Figure(data = go.Heatmap(
                    z=matrix1,
                    hovertemplate='Z: %{z}',
                    text=publisher, 
                    texttemplate="%{text}",
                    textfont={"size":10},
                    colorbar={"title":"Frequency"},
                    colorscale = 'Viridis'))
    
    fig2 = go.Figure(data = go.Heatmap(
                    z=matrix2,
                    hovertemplate='Z: %{z}',
                    text=Institutions, 
                    texttemplate="%{text}",
                    textfont={"size":8},
                    colorbar={"title":"Frequency"},
                    colorscale = 'Blackbody'))
    
    # Define hover information with URLs
    hover_text = [[f'<a href="{name}" target="_blank" style="color:#FFFFFF">{url}</a>' for name, url in zip(ta,row)] for row,ta in zip(ta,ta_url)]
    
    fig3 = go.Figure(data = go.Heatmap(
                    z=matrix3,
                    text=hover_text, 
                    hovertemplate='Z: %{z}',        
                    customdata = ta_url,
                    texttemplate="%{text}",
                    textfont={"size":12},
                    colorbar={"title":"Frequency"},
                    colorscale = 'Bluered'))

    # Update figure layouts
    fig.update_layout(
        height = 400,
        width = 1200,
        xaxis1=dict(showticklabels=False, showline=False),
        yaxis1=dict(showticklabels=False, showline=False),
        xaxis2=dict(showticklabels=False, showline=False),
        yaxis2=dict(showticklabels=False, showline=False),
        title = "Top Journals"
    )
    
    fig2.update_layout(
        height = 400,
        width = 1200,
        xaxis1=dict(showticklabels=False, showline=False),
        yaxis1=dict(showticklabels=False, showline=False),
        xaxis2=dict(showticklabels=False, showline=False),
        yaxis2=dict(showticklabels=False, showline=False),
        title = "Top Institutions"
    )
    
    fig3.update_layout(
        height = 400,
        width = 1200,
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
