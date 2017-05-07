
$(document).ready(function () {
    var games = -1;
    var url = window.location.search.substring(1);
    var parameters = url.split('=');
    if (parameters[0] == "games"){
        games = parameters[1]
    }
    var stats = [];
    var min_stat = null;
    jQuery.ajax({
        url: "../stats.txt?"+games,
        success: function(data){
            var lines = data.split('\n');
            for (var i = 0; i < lines.length; i++) {
                values = lines[i].split(',');
                if (values.length == 4){
                    stats.push([values[1], values[0], values[2], values[3]])
                    var points = Number(values[0])
                    if (!min_stat || points < min_stat){
                        min_stat = points
                    }
                }

            }
        },
        async: false
    })
    // Graph Data ##############################################
    var graphData = [{
            // Visits
            data: stats,
            color: '#71c73e',
            points: {radius: 1}
        }
        // , {
        // 	// Returning Visits
        // 	data: [ [6, 500], [7, 600], [8, 550], [9, 600], [10, 800], [11, 900], [12, 800], [13, 850], [14, 830], [15, 1000] ],
        // 	color: '#77b7c5',
        // 	points: { radius: 4, fillColor: '#77b7c5' }
        // }
    ];

    // Lines Graph #############################################
    $.plot($('#graph-lines'), graphData, {
        series: {
            points: {
                show: true,
                radius: 5
            },
            lines: {
                show: true
            },
            shadowSize: 0
        },
        grid: {
            color: '#646464',
            borderColor: 'transparent',
            borderWidth: 20,
            hoverable: true
        }
            // ,
            // xaxis: {
            // 	tickColor: 'transparent',
            // 	tickDecimals: 2
            // }
        ,
        yaxis: {
            // tickSize: 1000,
            min: min_stat
        }
    });

    // Bars Graph ##############################################
    // $.plot($('#graph-bars'), graphData, {
    // 	series: {
    // 		bars: {
    // 			show: true,
    // 			barWidth: .9,
    // 			align: 'center'
    // 		},
    // 		shadowSize: 0
    // 	},
    // 	grid: {
    // 		color: '#646464',
    // 		borderColor: 'transparent',
    // 		borderWidth: 20,
    // 		hoverable: true
    // 	},
    // 	// xaxis: {
    // 	// 	tickColor: 'transparent',
    // 	// 	tickDecimals: 2
    // 	// },
    // 	// yaxis: {
    // 	// 	tickSize: 1000
    // 	// }
    // });

    // Graph Toggle ############################################
    // $('#graph-bars').hide();

    // $('#lines').on('click', function (e) {
    //     $('#bars').removeClass('active');
    //     $('#graph-bars').fadeOut();
    //     $(this).addClass('active');
    //     $('#graph-lines').fadeIn();
    //     e.preventDefault();
    // });

    // $('#bars').on('click', function (e) {
    //     $('#lines').removeClass('active');
    //     $('#graph-lines').fadeOut();
    //     $(this).addClass('active');
    //     $('#graph-bars').fadeIn().removeClass('hidden');
    //     e.preventDefault();
    // });

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
                    var x = this_datapoint[0],
                        y = this_datapoint[1];
                    tooltip_text += y + ' points at game ' + x;
                }
                if (this_datapoint.length == 3){
                    var date = this_datapoint[2];
                    tooltip_text += ' on ' + date;
                }
                if (this_datapoint.length == 4){
                    var time = this_datapoint[3];
                    tooltip_text += ' at ' + time;
                }
                showTooltip(item.pageX, item.pageY, tooltip_text);
            }
        } else {
            $('#tooltip').remove();
            previousPoint = null;
        }
    });

});