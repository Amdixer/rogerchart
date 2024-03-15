
var colours = ["#FF0000","#00FF00","#0000FF","#0F0F0F","#FF0000","#00FF00","#0000FF","#0F0F0F","#FF0000","#00FF00","#0000FF","#0F0F0F"]
var i = 0;

function createPlotDiv(){
    let div = document.createElement("div");
    document.getElementById("main").appendChild(div);

    div.style.width  = "100%";
    div.style.height = "100%";
    div.style.margin = '0';
    div.style.padding = '0';
    // div.style.backgroundColor = colours[i];
    // div.innerHTML = "TEST123";
    i++;
    return div;

}


function createPage(){
    //Setup the main div.
    let mainDiv = document.getElementById("main");
    mainDiv.style.width  = '100vw';
    mainDiv.style.height = '100vh';
    mainDiv.style.display = 'grid';
    mainDiv.style.margin = '0';
    mainDiv.style.padding = '0';

    //Determine how many rows and columns there are.
    var Rows = 0;
    var Cols = 0;
    var templateCols    = "";
    var templateRows    = "";

    Rows = page_shape.length;
    Cols = page_shape[0].length;

    // for (row in page_shape){
    //     for (col in page_shape[row]){
    //         createPlotDiv();
    //     }
    // }

    //Set up the grid.
    for (var row = 0; row < Rows; row++){
        if(Rows === 1){
            templateRows += "100% ";
        }
        else{
            templateRows += "50% ";
        }
    }
    for (var col = 0; col < Cols; col++){
        templateCols += String(Math.floor(100/Cols)) + "% ";
    }

    mainDiv.style.gridTemplateColumns = templateCols;
    mainDiv.style.gridTemplateRows = templateRows;


    for (p in raw_plot_options){
        console.log(p);
        var o    = JSON.parse(raw_plot_options[p]);
        plot_options.push(o);

        var chart = echarts.init(createPlotDiv());
        chart.setOption(o); 
        charts.push(chart);
    }

    window.addEventListener("resize", function () {
        for (c in charts){
            charts[c].resize();
        }
    });   
}

createPage();