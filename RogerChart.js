<html><script src="echarts.min.js"></script>


var opts   = [];
var charts = []

function createCharts(options){
    var vw = int(100/len(self.axes[0]))
    var vh = int(max(50,100/len(self.axes)))

    for(o in options){
        let opt = JSON.parse(options[o]);
        opts.push(opt);
        var dom =
        PAGE += f"var option_{i}{j} = JSON.parse('{b.to_html()}');"
        PAGE += f'var chartDom_{i}{j} = document.getElementById("row_{i}_col_{j}");'
        PAGE += f'var chart_{i}{j}  = echarts.init(chartDom_{i}{j},"vintage");'
        PAGE += f'chart_{i}{j}.setOption(option_{i}{j});'
        PAGE += f'window.addEventListener("resize", function () {{chart_{i}{j}.resize();}});'

    }
}