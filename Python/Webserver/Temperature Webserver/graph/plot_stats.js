
$(document).ready(function () {
    // var games = -1;
    var url = window.location.search.substring(1);
    // var parameters = url.split('=');
    // if (parameters[0] == "games"){
    //     games = parameters[1]
    // }
    var stats1 = [];
    var stats2 = [];
    var stats3 = [];
    var stats4 = [];
    var min_stat = Number.MAX_VALUE;
    var max_stat = Number.MIN_VALUE;
    jQuery.ajax({
        url: `../stats.txt?${url}`,
        success: function (data) {
            var lines = data.split('\n');
            for (var i = 0; i < lines.length; i++) {
                values = lines[i].split(',');
                if (values.length == 5) {
                    var temp1 = Number(values[1]);
                    var temp2 = Number(values[2]);
                    var temp3 = Number(values[3]);
                    var temp4 = Number(values[4]);
                    var date = Number(values[0]) * 1000;

                    if (!isNaN(temp1)) {
                        stats1.push([date, temp1]);
                        min_stat = Math.min(min_stat, temp1);
                        max_stat = Math.max(max_stat, temp1);
                    }
                    if (!isNaN(temp2)) {
                        stats2.push([date, temp2]);
                        min_stat = Math.min(min_stat, temp2);
                        max_stat = Math.max(max_stat, temp2);
                    }
                    if (!isNaN(temp3)) {
                        stats3.push([date, temp3]);
                        min_stat = Math.min(min_stat, temp3);
                        max_stat = Math.max(max_stat, temp3);
                    }
                    if (!isNaN(temp4)) {
                        stats4.push([date, temp4]);
                        min_stat = Math.min(min_stat, temp4);
                        max_stat = Math.max(max_stat, temp4);
                    }

                }

            }
        },
        async: false
    });

    // Graph Data ##############################################
    var graphData = [{
        data: stats1,
        color: '#71c73e',
        points: { radius: 2 },
        yaxis: 1,
        unit: '°C'
    }, {
        data: stats2,
        color: '#11c73e',
        points: { radius: 2 },
        yaxis: 1,
        unit: '°C'
    }, {
        data: stats3,
        color: '#3ec744',
        points: { radius: 2 },
        yaxis: 1,
        unit: '°C'
    }, {
        data: stats4,
        color: '#4286f4',
        points: { radius: 3 },
        lines: { radius: 0.1 },
        yaxis: 2,
        unit: '%'
    }
    ];

    var lastDay = null;
    
    // Lines Graph #############################################
    $.plot($('#graph-lines'), graphData, {
        series: {
            points: {
                show: true,
            },
            lines: {
                show: true,
                radius: 0.02
            },
            shadowSize: 0
        },
        grid: {
            color: '#646464',
            borderColor: 'transparent',
            borderWidth: 20,
            hoverable: true
        },
        xaxis: {
            mode: "time",
            tickFormatter: function formatter(val, axis) {
              var d = new Date(val);
              var rV = null;          
              if (lastDay == null || d.getDay() == lastDay.getDay()) //lastDay is a global, set to null outside of plot call
              {
                rV = $.plot.formatDate(d, "%H:%M"); // first date return time
              }
              else
              {
                rV = $.plot.formatDate(d, "<b>%d.%m.%y</br>%H:%M</b>"); // return different format
              }
              lastDay = d; 
              return rV;
            }
        },
        yaxis: {
          tickFormatter: function formatter(val, axis) {
              return `${val} ${axis.options.unit}`;
            },
          font: {
            size: 12,
            family: 'Arial'
          },
          width: '100px'
        },
        yaxes: [
          { position: "left",
            color: "#11c73e",
            unit: '°C' },
          { position: "right",
            color: '#4286f4',
            unit: '%' }
        ]
        // ,
        // yaxis: {
        //     min: min_stat - 5,
        //     max: max_stat + 5
        // }
    });

    // Tooltip #################################################
    function showTooltip(x, y, contents) {
        $('<div id="tooltip">' + contents + '</div>').css({
            top: y - 16,
            left: x + 20
        }).appendTo('body').fadeIn();
    }

    var previousPoint = null;

    $('#graph-lines, #graph-bars').bind('plothover', function (event, pos, item) {
        if (item) {
            if (previousPoint != item.dataIndex) {
                previousPoint = item.dataIndex;
                $('#tooltip').remove();
                var this_datapoint = item.series.data[item.dataIndex]
                var tooltip_text = ""
                if (this_datapoint.length >= 2) {
                    var timestamp = new Date(this_datapoint[0]);
                    var date = timestamp.getDate() + '.' + timestamp.getMonth() + '.' + timestamp.getFullYear()
                    var time = timestamp.getHours() + ':' + timestamp.getMinutes() + ':' + timestamp.getSeconds()
                    var y = this_datapoint[1];
                    tooltip_text += `${y.toFixed(2)} ${item.series.unit} on ${date} at ${time}`;
                    // tooltip_text +=  + ' °C on ' + date + ' at ' + time;
                }
                showTooltip(item.pageX, item.pageY, tooltip_text);
            }
        } else {
            $('#tooltip').remove();
            previousPoint = null;
        }
    });

});