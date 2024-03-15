import os
import webbrowser
import json
from shutil import copy
MOD_PATH = os.path.dirname(os.path.realpath(__file__))
ECHARTS_PATH = os.path.abspath(os.path.join(MOD_PATH,"./echarts/dist"))
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
        self._xsize = grid[0]
        self._ysize = grid[1]
        self.axes = [RogerAxes() for h in range(grid[1]*grid[0])]

    def to_html(self, name="Test"):
        if not os.path.isdir(name):
            os.mkdir(name)

        PAGE = "<html>\n"
        PAGE += "<div id='main'></div>\n"
        PAGE += "<script src='echarts.min.js'></script>\n"
        PAGE += "<script>\n"
        PAGE += f"var raw_plot_options        = {[x.to_html() for x in self.axes]};\n"
        PAGE += f"var page_shape          = {[[1 for y in range(self._ysize)] for x in range(self._xsize)]};\n"
        PAGE += "var plot_options = [];\n"
        PAGE += "var charts = [];\n"
        PAGE += "</script>\n"
        PAGE += "<script src='RogerChart.js'></script>\n"
        PAGE += "</html>"


        for theme in os.listdir(THEMES_PATH):
            copy(os.path.join(THEMES_PATH,theme),f"{name}/")
            PAGE += f"<script src={theme}></script>"

        with open(f"{name}/{name}.html", 'w+') as f:
            f.write(PAGE)

        copy(os.path.join(ECHARTS_PATH,"echarts.min.js"),f"{name}/")
        copy(os.path.join(MOD_PATH,"RogerChart.js"),f"{name}/")
        webbrowser.get().open("file://" + os.path.abspath(f"{name}/{name}.html"))
        return 1




