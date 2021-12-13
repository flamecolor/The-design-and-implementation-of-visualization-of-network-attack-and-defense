from flask import Flask, render_template
from pyecharts import options as opts
from pyecharts.charts import Graph, Bar
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from datetime import timedelta
import topology as tp
import attdef as ad
import risk as rs
import network as nt

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

app = Flask(__name__, template_folder="templates")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


nodes = tp.nodes
links = tp.links

def graph_base()->Graph:
    graph = (
        Graph()
        .add("", nodes, links, repulsion=8000)
        .set_global_opts(
            toolbox_opts=opts.ToolboxOpts(
                feature=opts.ToolBoxFeatureOpts(
                    data_zoom=opts.ToolBoxFeatureDataZoomOpts(is_show=False),
                    magic_type=opts.ToolBoxFeatureMagicTypeOpts(is_show=False),
                    brush=opts.ToolBoxFeatureBrushOpts(type_="none")
                ),
                pos_left="right"
            )
        )
    )
    return graph

adnodes = ad.nodes
adlinks = ad.links

def adpro_base()->Graph:
    graph = (
        Graph()
        .add(
            "",
            adnodes,
            adlinks,
            repulsion=8000
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="")
        )
    )
    return graph

x = rs.x
y = rs.y

def bar_base()->Bar:
    bar = (
        Bar()
        .add_xaxis(xaxis_data=x)
        .add_yaxis(
            series_name="risk",
            yaxis_data=y,
            label_opts=opts.LabelOpts(
               is_show=False
            )
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                name="time",name_location="end",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#4c9bfd",)
                )
            ),
            title_opts=opts.TitleOpts(title=""),
            toolbox_opts=opts.ToolboxOpts(is_show=True,
                feature=opts.ToolBoxFeatureOpts(
                    data_zoom=opts.ToolBoxFeatureDataZoomOpts(yaxis_index=False),
                    brush=opts.ToolBoxFeatureBrushOpts(type_="none")
                ),
                pos_left="right"
            ),
            datazoom_opts=opts.DataZoomOpts(type_="slider"),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                name="risk",
                name_location="end",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#4c9bfd",)
                )
            ),
        )
    )
    return bar

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def index_():
    return render_template("index.html")

@app.route("/topologyChart")
def get_topology_chart():
    topology = graph_base()
    return topology.dump_options_with_quotes()

@app.route("/topology")
def topology():
    return render_template("topology.html")

@app.route("/attdefChart")
def get_attdef_chart():
    attdef = adpro_base()
    return attdef.dump_options_with_quotes()

@app.route("/attdef")
def attdef():
    return render_template("adpro.html")

@app.route("/adpro1")
def attdef1():
    return render_template("adpro1.html")

@app.route("/adpro2")
def attdef2():
    return render_template("adpro2.html")

@app.route("/adpro3")
def attdef3():
    return render_template("adpro3.html")

@app.route("/adpro4")
def attdef4():
    return render_template("adpro.html")

@app.route("/adpro5")
def attdef5():
    return render_template("adpro5.html")

@app.route("/adpro6")
def attdef6():
    return render_template("adpro6.html")

@app.route("/adpro7")
def attdef7():
    return render_template("adpro7.html")

@app.route("/adpro8")
def attdef8():
    return render_template("adpro8.html")

@app.route("/riskChart")
def get_risk_chart():
    risk = bar_base()
    return risk.dump_options_with_quotes()

@app.route("/risk")
def risk():
    return render_template("risk.html")

@app.route("/matrix")
def matrix():
    labels = nt.handers
    content = nt.rows
    content1 = nt.rrows
    return render_template("matrix.html", labels=labels, content=content, content1=content1)

if __name__ == '__main__':
    app.run()
