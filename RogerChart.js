function createPlotDiv(){
    let div = document.createElement("div");
    document.getElementById("main").appendChild(div);
    div.style.width  = "100%";
    div.style.height = "100%";
    div.style.margin = '0';
    div.style.padding = '0';
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
    Rows = page_shape.length;
    Cols = page_shape[0].length;

    //Dependin gon the amount of rows and columns, setup the grid template columns
    //parameters.
    var templateCols    = "";
    var templateRows    = "";

    //Iteratoe over the rows.
    for (var row = 0; row < Rows; row++){
        if(Rows === 1){
            templateRows += "100% ";        //If there's only 1 row, full height.
        }
        else{
            templateRows += "50% ";         //Else, cap it at 50%. TODO: Make this a setting in the future.
        }
    }

    //Iterate over the columns, the width is 100/n_cols % per column.
    for (var col = 0; col < Cols; col++){
        templateCols += String(100/Cols) + "% ";
    }

    //Set up the grid.
    mainDiv.style.gridTemplateColumns = templateCols;
    mainDiv.style.gridTemplateRows = templateRows;


    for (p in raw_plot_options){
        //Parse the plot options and add to global list of options..
        var o    = JSON.parse(raw_plot_options[p]);
        plot_options.push(o);

        //Initiate the chart. Adding a new div in the process.
        var chart = echarts.init(createPlotDiv());

        //Set the options.
        chart.setOption(o); 

        //Add the chart to the list of charts.
        charts.push(chart);
    }

    //Bind the resize function to rescale all plots when the window is resized.
    window.addEventListener("resize", function () {
        for (c in charts){
            charts[c].resize();
        }
    });   
}

//Call function to create the page.
createPage();