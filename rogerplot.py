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
        self.axes = [RogerAxes() for h in range(grid[0]*grid[1])]

    def to_html(self, name="Test", onefile=True):
        with open(os.path.join(MOD_PATH,"assets","rogerplot_base.html")) as f:
            PAGE = "".join(f.readlines())
        
        PAGE = PAGE.replace("##PLOT_OPTS##",str([x.to_html() for x in self.axes]))
        PAGE = PAGE.replace("##PAGESHAPE##",str([[1 for y in range(self._ysize)] for x in range(self._xsize)]))
        

        # Insert echarts & rogerplot javascript.
        if onefile:
            with open(os.path.join(ECHARTS_PATH,"echarts.min.js")) as f:
                echarts     = "".join(f.readlines())
            with open(os.path.join(MOD_PATH,"rogerplot.js")) as f:
                rogerplot  = "".join(f.readlines())
            PAGE = PAGE.replace("##ROGERPLOT_SCRIPT##",f"<script>{rogerplot}</script>")
            PAGE = PAGE.replace("##ECHARTS_SCRIPT##",f"<script>{echarts}</script>")
            with open(f"{name}.html", 'w+') as f:
                f.write(PAGE)
            webbrowser.get().open("file://" + os.path.abspath(f"{name}.html"))
        else:
            # Create Directory.
            if not os.path.isdir(name):
                os.mkdir(name)
            PAGE = PAGE.replace("##ECHARTS_SCRIPT##",f"<script src='echarts.min.js'></script>")
            PAGE = PAGE.replace("##ROGERPLOT_SCRIPT##",f"<script src='rogerplot.js'></script>")
            copy(os.path.join(ECHARTS_PATH,"echarts.min.js"),f"{name}/")
            with open(f"{name}/{name}.html", 'w+') as f:
                f.write(PAGE)
            webbrowser.get().open("file://" + os.path.abspath(f"{name}/{name}.html"))
        return 1




