$(function () {

	var stats1 = [];
	var stats2 = [];
	var min_stat = null;
	var max_stat = null;
	jQuery.ajax({
		url: "../stats.txt",
		success: function (data) {
			var lines = data.split('\n');
			for (var i = 0; i < lines.length; i++) {
				values = lines[i].split(',');
				if (values.length == 3) {
					var temp1 = Number(values[1])
					var temp2 = Number(values[2])
					var date = Number(values[0]) * 1000
					stats1.push([date, temp1])
					stats2.push([date, temp2])

					if (!min_stat || temp1 < min_stat) {
						min_stat = temp1
						if (temp2 < min_stat) {
							min_stat = temp2
						}
					}
					if (!max_stat || temp1 > max_stat) {
						max_stat = temp1
						if (temp2 > max_stat) {
							max_stat = temp2
						}
					}
				}

			}
		},
		async: false
	})

	// first correct the timestamps - they are recorded as the daily
	// midnights in UTC+0100, but Flot always displays dates in UTC
	// so we have to add one hour to hit the midnights in the plot

	// for (var i = 0; i < stats1.length; ++i) {
	// 	stats1[i][0] += 60 * 60 * 1000;
	// }

	// helper for returning the weekends in a period

	function weekendAreas(axes) {

		var markings = [],
			date = new Date(axes.xaxis.min);

		// go to the first Saturday

		date.setUTCDate(date.getUTCDate() - ((date.getUTCDay() + 1) % 7))
		date.setUTCSeconds(0);
		date.setUTCMinutes(0);
		date.setUTCHours(0);

		var i = date.getTime();

		// when we don't set yaxis, the rectangle automatically
		// extends to infinity upwards and downwards

		do {
			markings.push({
				xaxis: {
					from: i,
					to: i + 2 * 24 * 60 * 60 * 1000
				}
			});
			i += 7 * 24 * 60 * 60 * 1000;
		} while (i < axes.xaxis.max);

		return markings;
	}

	var graphData = [{
		data: stats1,
		color: '#71c73e',
		// label: "Temperature 1:  NaN  °C"
	}, {
		data: stats2,
		color: '#11773e',
		// label: "Temperature 2:  NaN  °C"
	}];

	var options = {
		xaxis: {
			mode: "time",
			tickLength: 5
		},
		selection: {
			mode: "xy",
			color: '#11c73e'
		},
		// crosshair: {
		// 	mode: "xy"
		// },
		series: {
			points: {
				show: true,
				radius: 1
			},
			lines: {
				show: true,
				radius: 0.01
			},
			shadowSize: 0
		},
		grid: {
			markings: weekendAreas,
			// hoverable: true,
			// autoHighlight: false
		}
	};

	var plot = $.plot("#placeholder", graphData, options);

	var overview = $.plot("#overview", graphData, {
		series: {
			lines: {
				show: true,
				lineWidth: 1
			},
			shadowSize: 0
		},
		xaxis: {
			ticks: [],
			mode: "time"
		},
		yaxis: {
			ticks: [],
			min: min_stat,
			max: max_stat,
			autoscaleMargin: 0.1
		},
		selection: {
			mode: "xy",
			color: '#11c73e'
		}
	});

	// now connect the two

	$("#placeholder").bind("plotselected", function (event, ranges) {

		// do the zooming
		$.each(plot.getXAxes(), function (_, axis) {
			var opts = axis.options;
			opts.min = ranges.xaxis.from;
			opts.max = ranges.xaxis.to;
		});
		plot.setupGrid();
		plot.draw();
		plot.clearSelection();

		// don't fire event on the overview to prevent eternal loop

		overview.setSelection(ranges, true);
	});

	$("#overview").bind("plotselected", function (event, ranges) {
		plot.setSelection(ranges);
	});


	// var legends = $("#placeholder .legendLabel");

	// legends.each(function () {
	// 	// fix the widths so they don't jump around
	// 	$(this).css('width', $(this).width());
	// });

	// var updateLegendTimeout = null;
	// var latestPosition = null;

	// function updateLegend() {

	// 	updateLegendTimeout = null;

	// 	var pos = latestPosition;

	// 	var axes = plot.getAxes();
	// 	if (pos.x < axes.xaxis.min || pos.x > axes.xaxis.max ||
	// 		pos.y < axes.yaxis.min || pos.y > axes.yaxis.max) {
	// 		return;
	// 	}

	// 	var i, j, dataset = plot.getData();
	// 	for (i = 0; i < dataset.length; ++i) {

	// 		var series = dataset[i];

	// 		// Find the nearest points, x-wise

	// 		for (j = 0; j < series.data.length; ++j) {
	// 			if (series.data[j][0] > pos.x) {
	// 				break;
	// 			}
	// 		}

	// 		// Now Interpolate

	// 		var y,
	// 			p1 = series.data[j - 1],
	// 			p2 = series.data[j];

	// 		if (p1 == null) {
	// 			y = p2[1];
	// 		} else if (p2 == null) {
	// 			y = p1[1];
	// 		} else {
	// 			y = p1[1] + (p2[1] - p1[1]) * (pos.x - p1[0]) / (p2[0] - p1[0]);
	// 		}

	// 		legends.eq(i).text(series.label.replace(" NaN  ", y.toFixed(1)));
	// 	}
	// }

	// $("#placeholder").bind("plothover",  function (event, pos, item) {
	// 	latestPosition = pos;
	// 	if (!updateLegendTimeout) {
	// 		updateLegendTimeout = setTimeout(updateLegend, 50);
	// 	}
	// });

	// Tooltip #################################################
	function showTooltip(x, y, contents) {
		$('<div id="tooltip">' + contents + '</div>').css({
			top: y - 16,
			left: x + 20
		}).appendTo('body').fadeIn();
	}

	var previousPoint = null;

	$('#placeholder').bind('plothover', function (event, pos, item) {
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
					tooltip_text += y.toFixed(2) + ' °C on ' + date + ' at ' + time;
				}
				showTooltip(item.pageX, item.pageY, tooltip_text);
			}
		} else {
			$('#tooltip').remove();
			previousPoint = null;
		}
	});

});