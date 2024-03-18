
![RogerPlotLogo](https://github.com/Amdixer/rogerchart/assets/15040680/20a176db-9bf3-438d-b52f-a96ae61c9f65)

# RogerPlot
RogerPlot is a python based plotting library that creates output in the form of all-in-one HTML files. The purpose of RogerPlot is
to make it easy to share data in a visually appealing way without requiring any form of software other than a webbrowser.

## Python Based
The python backend of RogerPlot makes use of a matplotlib-like interface to take data such as numpy arrays or simple lists and add them to plotting objects. (axes) These plotting objects are then grouped together into a RogerFigure which can be converted to an html file by calling the _to_html()_ function.



## Apache Echarts
The browser component of RogerPlot is based on apache Echarts in order to out-of-the-box support a great deal of features already iplemented on that platform.
