import os
import webbrowser
import json
from shutil import copy
MOD_PATH = os.path.dirname(os.path.realpath(__file__))
ECHARTS_PATH = os.path.abspath(os.path.join(MOD_PATH,"../echarts/dist"))
THEMES_PATH  = os.path.abspath(os.path.join(MOD_PATH, "themes"))

class RogerAxes():
    def __init__(self) -> None:
        self.option = {
            "xAxis" : {
                "type": 'category',
            },
            "yAxis": {
                "type": 'value'
            },
            "series": [
            ]
            }
        self._plot_objs = []
        self._plot_type = 'line'

    def stackplot(self,*args,**kwargs):
        self._plot_type = 'stack'
        x = args[0]

        for i,line in enumerate(args[1:]):
            p = {}
            p["data"] = list(zip(x, line.tolist()))
            p["type"] = "line"
            p["name"] = kwargs['label'][i]

            self._plot_objs.append(p)

    def plot(self,xdata,ydata,name="Series",type="line"):
        self._plot_type = 'line'
        p = {}
        p["data"]  = list(zip(xdata,ydata))
        p["type"]  = type
        p["name"]  = name
        self._plot_objs.append(p)

    def legend(self,show=True):
        data = [str(i) for i in range(len(self.option["series"]))]
        self.option["legend"] = {
            # "data":data,
            # "orient": 'vertical',
            # "right": 10,
            # "top": 'center'
        }
    def toolbox(self,show=True):
        self.option["toolbox"] = {
            "show": show,
            "feature": {
                "saveAsImage": {},
                "restore": {},
                "dataZoom": {"filterMode": 'none'},
            }
        }

    def set_title(self,title,**kwargs):
        self.option["title"] = {
            "show": 'true',
            "text": title
        }

        if 'align' in kwargs.keys():
            self.option["title"]["textAlign"] = kwargs['align']
            self.option["title"]["left"]      = kwargs['align']
    def to_html(self):
        for p in self._plot_objs:
            ser = {
                "data": p["data"],
                "type": p["type"],
                "name": p["name"],
            }
            if self._plot_type == 'stack':
                ser['stack']        = "Total"
                ser['areaStyle']    = {}

            self.option["series"].append(ser)
        return json.dumps(self.option)


class RogerFigure():
    def __init__(self, grid=(1, 1)):
        self.axes = [[RogerAxes() for h in range(grid[1])] for g in range(grid[0])]

    def to_html(self, name="Test"):
        if not os.path.isdir(name):
            os.mkdir(name)

        vw = int(100/len(self.axes[0]))
        vh = int(max(50,100/len(self.axes))) #Cap to 50%.

        PAGE = "<html>"
        PAGE += '<script src="echarts.min.js"></script>'
        for theme in os.listdir(THEMES_PATH):
            copy(os.path.join(THEMES_PATH,theme),f"{name}/")
            PAGE += f"<script src={theme}></script>"


        PAGE += f"<div id='main' style='width:100vw;height:100vh;display: grid; grid-template-columns: {' '.join([str(vw)+'%' for i in range(len(self.axes[0]))])};grid-template-rows:{' '.join([f'{vh}%' for i in range(len(self.axes))])};'>"
        for i,a in enumerate(self.axes):
            # PAGE += f"<div id = 'row_{i}' style='width:100%;height:{vh}%;'>"
            for j,b in enumerate(a):
                PAGE += f"<div id = 'row_{i}_col_{j}' style='width:100%;height:100%;'></div>"
            # PAGE += "</div>"
        PAGE += '</div>'

        PAGE += "<script>"

        for i,a in enumerate(self.axes):
            for j,b in enumerate(a):
                PAGE += f"var option_{i}{j} = JSON.parse('{b.to_html()}');"
                PAGE += f'var chartDom_{i}{j} = document.getElementById("row_{i}_col_{j}");'
                PAGE += f'var chart_{i}{j}  = echarts.init(chartDom_{i}{j},"vintage");'
                PAGE += f'chart_{i}{j}.setOption(option_{i}{j});'
                PAGE += f'window.addEventListener("resize", function () {{chart_{i}{j}.resize();}});'
        PAGE += "</script></html>"

        with open(f"{name}/{name}.html", 'w+') as f:
            f.write(PAGE)

        copy(os.path.join(ECHARTS_PATH,"echarts.min.js"),f"{name}/")
        webbrowser.get().open("file://" + os.path.abspath(f"{name}/{name}.html"))
        return 1




