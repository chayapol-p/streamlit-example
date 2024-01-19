def simple_dashboard():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import time # to simulate a real time data, time loop 
    import plotly.express as px # interactive charts
    from streamlit_echarts import st_pyecharts
    import streamlit.components.v1 as components
    import datetime
    import random

    from pyecharts import options as opts
    from pyecharts.charts import Calendar, Line
    from pyecharts.globals import ThemeType


    st.title("Simple Dashboard")

    expander = st.expander("Select Factory Type")
    country_list = ('Australia', 'Thailand', 'USA')
    country = expander.selectbox(
        'Please select your country?',
        country_list,
        index=None,
        placeholder='Please Select Country'
    )

    factory_type = [['A', 'B', 'C'], ['ก', 'ข', 'ค'], ['a', 'b', 'c']]

    town = expander.selectbox(
        'Please select your Factory Type?',
        factory_type[country_list.index(country)] if country else (),
        index=None,
        placeholder='Please Select Country First' if not country else "",
        disabled=country is None,
    )

    if town is not None:
        # read csv from a github repo
        df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

        # top-level filters 

        job_filter = st.selectbox("Select the Job", pd.unique(df['job']))


        # creating a single-element container.
        placeholder = st.empty()

        # dataframe filter 

        df = df[df['job']==job_filter]

        # near real-time / live feed simulation 

        for seconds in range(200):
            
            #while True: 
                
            df['age_new'] = df['age'] * np.random.choice(range(1,5))
            df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

            # creating KPIs 
            avg_age = np.mean(df['age_new']) 

            count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))

            balance = np.mean(df['balance_new'])

            with placeholder.container():
                # create three columns
                kpi1, kpi2, kpi3 = st.columns(3)

                # fill in those three columns with respective metrics or KPIs 
                kpi1.metric(label="Age ⏳", value=round(avg_age), delta= round(avg_age) - 10)
                kpi2.metric(label="Married Count 💍", value= int(count_married), delta= - 10 + count_married)
                kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)

                # create two columns for charts 

                fig_col1, fig_col2 = st.columns(2)
                with fig_col1:
                    st.markdown("### First Chart")
                    fig = px.density_heatmap(data_frame=df, y = 'age_new', x = 'marital')
                    st.write(fig)
                with fig_col2:
                    st.markdown("### Second Chart")
                    fig2 = px.histogram(data_frame = df, x = 'age_new')
                    st.write(fig2)
                
                fig_col1, fig_col2 = st.columns(2)
                with fig_col1:
                    week_name_list = ["Sunday", "Monday", "Tuesday", "Wenesday", "Thursday", "Friday", "Saturday"]
                    high_temperature = [11, 11, 15, 13, 12, 13, 10]
                    low_temperature = [1, -2, 2, 5, 3, 2, 0]


                    c1 = (
                        Line(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
                        .add_xaxis(xaxis_data=week_name_list)
                        .add_yaxis(
                            series_name="Co2 created in last week",
                            y_axis=high_temperature,
                            markpoint_opts=opts.MarkPointOpts(
                                data=[
                                    opts.MarkPointItem(type_="max", name="Maximum"),
                                    opts.MarkPointItem(type_="min", name="Minimum"),
                                ]
                            ),
                            markline_opts=opts.MarkLineOpts(
                                data=[opts.MarkLineItem(type_="average", name="Average")]
                            ),
                        )
                        .add_yaxis(
                            series_name="O2 created in last week",
                            y_axis=low_temperature,
                            markpoint_opts=opts.MarkPointOpts(
                                data=[opts.MarkPointItem(value=-2, name="Guess", x=1, y=-1.5)]
                            ),
                            markline_opts=opts.MarkLineOpts(
                                data=[
                                    opts.MarkLineItem(type_="average", name="Average"),
                                    opts.MarkLineItem(symbol="none", x="90%", y="max"),
                                    opts.MarkLineItem(symbol="circle", type_="max", name="Maximum"),
                                ]
                            ),
                        )
                        .set_global_opts(
                            title_opts=opts.TitleOpts(title="Gas Created from Factory A", subtitle="Co2 and O2"),
                            tooltip_opts=opts.TooltipOpts(trigger="axis"),
                            toolbox_opts=opts.ToolboxOpts(is_show=True),
                            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
                        )
                        .render_embed()
                    )
                    components.html(c1, width=1000, height=600)

                with fig_col2:
                    pass

                begin = datetime.date(2023, 1, 1)
                end = datetime.date(2023, 12, 31)
                data = [
                    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
                    for i in range((end - begin).days + 1)
                ]

                c = (
                    Calendar()
                    .add("", data, calendar_opts=opts.CalendarOpts(range_="2023"))
                    .set_global_opts(
                        title_opts=opts.TitleOpts(title="Calendar-2023 Carbon Created"),
                        visualmap_opts=opts.VisualMapOpts(
                            max_=20000,
                            min_=500,
                            orient="horizontal",
                            is_piecewise=False,
                            pos_top="230px",
                            pos_left="center",
                        ),
                    )
                    .render_embed()
                )
                components.html(c, width=1000, height=400)
                

                
                st.markdown("### Detailed Data View")
                st.dataframe(df)
                time.sleep(100000)

        
            # data_heatmap = [[a, b, np.random.randint(0, 10)] for a in range(7) for b in range(24)]
            # data_heatmap = [[d[1], d[0], d[2] if d[2] != 0 else "-"] for d in data_heatmap]

            # df['age_new'] = df['age'] * np.random.choice(range(1,5))
            # df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

            # # creating KPIs 
            # avg_age = np.mean(df['age_new']) 

            # count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))

            # balance = np.mean(df['balance_new'])
            # st.experimental_rerun()
            #placeholder.empty()