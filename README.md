![RogierPlot_WB](https://github.com/Amdixer/rogerplot/assets/15040680/08b43fff-656e-484f-a479-48aa0baaae42)

# RogerPlot
RogerPlot is a python based plotting library that creates output in the form of all-in-one HTML files. The purpose of RogerPlot is
to make it easy to share data in a visually appealing way without requiring any form of software other than a webbrowser.

## Python Based
The python backend of RogerPlot makes use of a matplotlib-like interface to take data such as numpy arrays or simple lists and add them to plotting objects. (axes) These plotting objects are then grouped together into a RogerFigure which can be converted to an html file by calling the _to_html()_ function.



## Apache Echarts
The browser component of RogerPlot is based on apache Echarts in order to out-of-the-box support a great deal of features already iplemented on that platform.
