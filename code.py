import csv
import plotly.express as px
import numpy as np
def plotfigure(datapath):
  with open(datapath) as csvfile:
    df = csv.DictReader(csvfile)
    fig = px.scatter(px, x = "Days Present", y = "Marks In Percentage")
    fig.show()
 def getdatasource(datapath):
  marksinpercentage = []
  dayspresent = []
  with open(datapath) as csvfile:
    df = csv.DictReader(csvfile)
    for row in tf:
      marksinpercentage.append(float(row["Marks In Percentage"]))
      dayspresent.append(float(row["Days Present"]))
  return {"x": marksinpercentage, "y": dayspresent}
def findingcorrelation(dataSource):
  correlation = np.corrcoef(dataSource["x"], dataSource["y"])
  print(correlation)
def setup():
  datapath = "./data/StudentMarksVSDaysPresent.csv"
  dataSource = getdatasource(datapath)
  findingcorrelation(dataSource)
  plotfigure(datapath)
setup()
