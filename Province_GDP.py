import pandas as pd 
import plotly.graph_objects as go
#导入相关的csv文件
df=pd.read_csv('GDP.csv',encoding='gbk')
df['colors']=['aliceblue','antiquewhite','aqua','aquamarine','azure','beige','bisque','black','blanchedalmond','blue',
'blueviolet','brown','burlywood','cadetblue','chartreuse','chocolate','coral','cornflowerblue','red','crimson','cyan','darkblue',
'darkcyan','darkgoldenrod','darkgray','darkgreen','darkkhaki','darkmagenta','darkolivegreen','darkorange','darkorchid']

ani_frames=[]
for i in df.columns[1:-1][::-1]:
    df.sort_values(by=i,inplace=True)
    bar=go.Bar(x=df[i],y=df['地区'],orientation='h',textposition='outside',marker_color=df['colors'],text=df[i])
    frame=go.Frame(data=bar,layout=go.Layout(title=i+'各省份（不含港澳台）的GDP（亿元）',title_x=0.5,title_y=0.9))
    ani_frames.append(frame)

ini_bar= go.Bar(x=df['2000年'],y=df['地区'],orientation='h',textposition='outside',marker_color=df['colors'],text=df['2000年'])   

buttons={
    "type":"buttons",
    "direction":"right",
    "pad":{"r":80,"t":0},
    "buttons":[{"label":"Play","method":"animate","args":[
        None,
        dict(frame=dict(duration=600,redraw=True),
            transition=dict(duration=1800,easing="linear-in-out"),
            fromcurrent=True,
            mode='immediate')
    ]}]
}
    

fig=go.Figure(
    data=[ini_bar],
    layout=go.Layout(
    title="2000年各省份（不含港澳台）的GDP（亿元）",
    title_x=0.5,
    title_y=0.9,
    width=1000,height=750,
    updatemenus=[buttons],
    xaxis=dict(showgrid=True,zeroline=False,automargin=True,range=[0,119000]),
    yaxis=dict(showgrid=True,zeroline=False,automargin=True)
    ),
    frames=ani_frames
    )
fig.update_yaxes(nticks=40)
fig.show()
# 