/**
 * Rogier Colijn - 03-2024
 *
 * long description for the file
 *
 * @summary Main JS class for RogerPlot
 * @author Rogier Colijn
 *
 * Created at     : 2024-03
 */


function createPlotDiv(){
    /**
     * Create a div to store a plot element in. Configure
     * the plot div width,height, margin and padding.
     * 
     * Return the div object.
     */
    let div = document.createElement("div");
    document.getElementById("main").appendChild(div);
    div.style.width  = "100%";
    div.style.height = "100%";
    div.style.margin = '0';
    div.style.padding = '0';
    return div;
}


function createPage(){
    /**
     * Create the main RogerPlot layout.
     * 
     */


    //Find the main div and set it's properties.
    let mainDiv = document.getElementById("main");
    mainDiv.style.width  = '100vw';                 //100% View Width
    mainDiv.style.height = '100vh';                 //100% View Height
    mainDiv.style.display = 'grid';                 //Display mode grid
    mainDiv.style.margin = '0';                     //Zero margin
    mainDiv.style.padding = '0';                    //Zero padding

    //Determine number of rows and cols.
    var Rows = page_shape.length;;
    var Cols = page_shape[0].length;;

    //Depending on the amount of rows and columns, setup the grid template columns
    //parameters.
    var templateCols    = "";
    var templateRows    = "";

    //Iterate over the rows and add to templateRows.
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

    //Set up the grid by configuring the gridtemplate
    //parameters.
    mainDiv.style.gridTemplateColumns = templateCols;
    mainDiv.style.gridTemplateRows = templateRows;

    //Iterate over the plot options added to the template and turn them
    //into charts.
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