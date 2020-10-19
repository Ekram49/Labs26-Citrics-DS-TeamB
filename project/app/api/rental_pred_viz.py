from fastapi import APIRouter, HTTPException
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os

router = APIRouter()

DATA_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "..","data", "rental_all.csv")

@router.get('/rental_viz/{city_id}')
async def rental_viz_to_dict(city_id: int):
    """
    Rental Prediction Visualization 
    """

    rt_dict = {}
    rt_data_dict = {}
    rt_data_dict_viz = {}
    
    df = pd.read_csv(DATA_FILEPATH, encoding='utf-8')
    dataframe = df[df['city_id']==city_id]
    rt_data = dataframe.to_numpy()
    
    rt_data_dict['id'] = rt_data[0][1]
    rt_data_dict['city'] = rt_data[0][2]
    rt_data_dict['state'] = rt_data[0][3]
    rt_data_dict['city_state'] = rt_data[0][4]
    rt_dict['data'] = rt_data_dict
    rt_dict['viz'] = rt_data_dict_viz

    rt_data_dict_viz["studio"] = studio_rental_viz(city_id=rt_data[0][1])
    rt_data_dict_viz["1br"] = one_bed_viz(city_id=rt_data[0][1])
    rt_data_dict_viz["2br"] = two_bed_viz(city_id=rt_data[0][1])
    rt_data_dict_viz["3br"] = three_bed_viz(city_id=rt_data[0][1])
    rt_data_dict_viz["4br"] = four_bed_viz(city_id=rt_data[0][1])

    return rt_dict


def studio_rental_viz(city_id):

  df = pd.read_csv(DATA_FILEPATH, encoding='utf-8')

  df = df.loc[df['city_id'] == city_id]
  x = df['year'].tolist()
  x_rev = x[::-1]

  y = df['st_yhat'].tolist()
  y_upper = df['st_yhat_upper'].tolist()
  y_lower = df['st_yhat_lower'].tolist()
  y_lower = y_lower[::-1]

  fig = go.Figure()

  fig.add_trace(go.Scatter(
      x=x+x_rev,
      y=y_upper+y_lower,
      fill='toself',
      fillcolor='rgba(0,100,80,0.2)',
      line_color='rgba(255,255,255,0)',
      showlegend=False,
      name='Studio',
  ))

  fig.add_trace(go.Scatter(
      x=x, y=y,
      line_color='rgb(0,100,80)',
      name='Studio',
  ))

  fig.update_traces(mode='lines')

  return fig.to_json()

def one_bed_viz(city_id):
  
  df = pd.read_csv(DATA_FILEPATH, encoding='utf-8')

  df = df.loc[df['city_id'] == city_id]
  x = df['year'].tolist()
  x_rev = x[::-1]

  y = df['one_yhat'].tolist()
  y_upper = df['one_yhat_upper'].tolist()
  y_lower = df['one_yhat_lower'].tolist()
  y_lower = y_lower[::-1]

  fig = go.Figure()

  fig.add_trace(go.Scatter(
      x=x+x_rev,
      y=y_upper+y_lower,
      fill='toself',
      fillcolor='rgba(0,176,246,0.2)',
      line_color='rgba(255,255,255,0)',
      showlegend=False,
      name='1BR',
  ))

  fig.add_trace(go.Scatter(
      x=x, y=y,
      line_color='rgb(0,176,246)',
      name='1BR',
  ))

  fig.update_traces(mode='lines')

  return fig.to_json()

def two_bed_viz(city_id):

  df = pd.read_csv(DATA_FILEPATH, encoding='utf-8')

  df = df.loc[df['city_id'] == city_id]
  x = df['year'].tolist()
  x_rev = x[::-1]

  y = df['two_yhat'].tolist()
  y_upper = df['two_yhat_upper'].tolist()
  y_lower = df['two_yhat_lower'].tolist()
  y_lower = y_lower[::-1]

  fig = go.Figure()

  fig.add_trace(go.Scatter(
      x=x+x_rev,
      y=y_upper+y_lower,
      fill='toself',
      fillcolor='rgba(231,107,243,0.2)',
      line_color='rgba(255,255,255,0)',
      showlegend=False,
      name='2BR',
  ))

  fig.add_trace(go.Scatter(
      x=x, y=y,
      line_color='rgb(231,107,243)',
      name='2BR',
  ))

  fig.update_traces(mode='lines')

  return fig.to_json()

def three_bed_viz(city_id):

  df = pd.read_csv(DATA_FILEPATH, encoding='utf-8')

  df = df.loc[df['city_id'] == city_id]
  x = df['year'].tolist()
  x_rev = x[::-1]

  y = df['three_yhat'].tolist()
  y_upper = df['three_yhat_upper'].tolist()
  y_lower = df['three_yhat_lower'].tolist()
  y_lower = y_lower[::-1]

  fig = go.Figure()

  fig.add_trace(go.Scatter(
      x=x+x_rev,
      y=y_upper+y_lower,
      fill='toself',
      fillcolor='rgba(255,178,102,0.2)',
      line_color='rgba(255,255,255,0)',
      showlegend=False,
      name='3BR',
  ))

  fig.add_trace(go.Scatter(
      x=x, y=y,
      line_color='rgb(255,178,102)',
      name='3BR',
  ))

  fig.update_traces(mode='lines')

  return fig.to_json()

def four_bed_viz(city_id):

  df = pd.read_csv(DATA_FILEPATH, encoding='utf-8')

  df = df.loc[df['city_id'] == city_id]
  x = df['year'].tolist()
  x_rev = x[::-1]

  y = df['four_yhat'].tolist()
  y_upper = df['four_yhat_upper'].tolist()
  y_lower = df['four_yhat_lower'].tolist()
  y_lower = y_lower[::-1]

  fig = go.Figure()

  fig.add_trace(go.Scatter(
      x=x+x_rev,
      y=y_upper+y_lower,
      fill='toself',
      fillcolor='rgba(51,51,255,0.2)',
      line_color='rgba(255,255,255,0)',
      showlegend=False,
      name='4BR',
  ))

  fig.add_trace(go.Scatter(
      x=x, y=y,
      line_color='rgb(51,51,255)',
      name='4BR',
  ))

  fig.update_traces(mode='lines')

  return fig.to_json()