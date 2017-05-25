
$(document).ready(function () {
    // var games = -1;
    var url = window.location.search.substring(1);
    // var parameters = url.split('=');
    // if (parameters[0] == "games"){
    //     games = parameters[1]
    // }
    var stats1 = [];
    var stats2 = [];
    var min_stat = null;
    var max_stat = null;
    jQuery.ajax({
        url: "../stats.txt",
        success: function(data){
            var lines = data.split('\n');
            for (var i = 0; i < lines.length; i++) {
                values = lines[i].split(',');
                if (values.length == 3){
                    var temp1 = Number(values[1])
                    var temp2 = Number(values[2])
                    var date = Number(values[0])*1000
                    stats1.push([date, temp1])
                    stats2.push([date, temp2])
                    
                    if (!min_stat || temp1 < min_stat){
                        min_stat = temp1
                        if (temp2 < min_stat){
                            min_stat = temp2
                        }
                    }
                    if (!max_stat || temp1 > max_stat){
                        max_stat = temp1
                        if (temp2 > max_stat){
                            max_stat = temp2
                        }
                    }
                }

            }
        },
        async: false
    })

    // Graph Data ##############################################
    var graphData = [{
            data: stats1,
            color: '#71c73e',
            points: {radius: 2}
        },{
            data: stats2,
            color: '#11c73e',
            points: {radius: 2}
        }
    ];

    // Lines Graph #############################################
    $.plot($('#graph-lines'), graphData, {
        series: {
            points: {
                show: true,
            },
            lines: {
                show: true,
                radius: 0.01
            },
            shadowSize: 0
        },
        grid: {
            color: '#646464',
            borderColor: 'transparent',
            borderWidth: 20,
            hoverable: true
        }
            ,
            xaxis: {
            	mode: "time"
            }
        ,
        yaxis: {
            min: min_stat-5,
            max: max_stat+5
        }
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
                if (this_datapoint.length >= 2){
                    var timestamp = new Date(this_datapoint[0]);
                    var date = timestamp.getDate() + '.' + timestamp.getMonth() + '.' + timestamp.getFullYear()
                    var time = timestamp.getHours() + ':' + timestamp.getMinutes() + ':' + timestamp.getSeconds()
                    var y = this_datapoint[1];
                    tooltip_text += y + ' °C on ' + date + ' at ' + time;
                }
                showTooltip(item.pageX, item.pageY, tooltip_text);
            }
        } else {
            $('#tooltip').remove();
            previousPoint = null;
        }
    });

});