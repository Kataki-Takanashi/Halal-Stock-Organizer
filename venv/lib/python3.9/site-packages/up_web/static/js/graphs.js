function from_hash() {
	var hash = window.location.hash;

	if (hash.length) {
		return decodeURIComponent(hash.substr(1));
	} else {
		return '';
	}
}

function to_hash(hash) {
	if (hash.length) {
		window.location.hash = '#' + hash;
	}
}

function truncate(number, digits) {
	var factor = Math.pow(10, digits);
	return Math.floor(number * factor) / factor;
}

function unsample(data, key) {
	var result = data.reduce(function (state, currentValue, index, array) {
		if (!state.length) {
			console.log(currentValue, key);
			state.push({
				'up': currentValue[key],
				'date': currentValue.date,
				'count': 0
			});
		}

		var last = state[state.length - 1];

		if (last[key] == currentValue[key]) {
			last.count++;
		} else {
			state.push({
				'up': currentValue[key],
				'date': currentValue.date,
				'count': 1
			});
		}

		console.log(last[key], currentValue[key]);

		last.duration = currentValue.date - last.date;

		return state;
	}, []);

	return result;
}

var Formatters = {
	short_duration: function (y) {
		var abs_y = Math.abs(y);
		if (abs_y >= (60 * 60 * 24))  { return truncate(y / (60 * 60 * 24), 2) + "d"; }
		else if (abs_y >= (60 * 60))  { return truncate(y / (60 * 60), 2) + "hr"; }
		else if (abs_y >= 60)         { return truncate(y / 60, 2) + " min"; }
		else if (abs_y >= 1)          { return truncate(y, 2) + "s"; }
		else if (abs_y >= 0.001)      { return y / 0.001 + "ms"; }
		else if (abs_y >= 0.00001)    { return (y / 0.001).toFixed(2) + 'ms'; }
		else if (abs_y < 0.00001)     { return '0'; }
		else                          { return y; }
	},
	months_of_year: function (x) {
		var months = [
			"January",
			"February",
			"March",
			"April",
			"May",
			"June",
			"July",
			"August",
			"September",
			"October",
			"November",
			"December"
		];

		return months[x];
	},
	day_of_week: function (x) {
		var days = [
			"Sunday",
			"Monday",
			"Tuesday",
			"Wednesday",
			"Thursday",
			"Friday",
			"Saturday"
		];

		return days[x];
	},
	hours_of_day: function (x) {
		return x + ':00 UTC';
	},
	percent: function (y) {
		return (Math.floor(y * 10000) / 100) + '%';
	}
};

var path_selector = document.querySelector('#path-selector'),
	date_selector = document.querySelector('#date-selector'),
	up_selector = document.querySelector('#up-selector'),
	path = from_hash(),
	min_date = 0,
	min_up = 0,
	// store a copy of the charts container for later
	charts_container_prime = document.querySelector('.js-chart-container').cloneNode(true);

document.addEventListener('DOMContentLoaded', function () {
	console.log(path);
	path_selector[path_selector.selectedIndex].value = path;
	redraw_graph(path, min_date, min_up);
}, true);

path_selector.addEventListener('change', function (e) {
	path = path_selector[path_selector.selectedIndex].value;
	to_hash(path);
	redraw_graph(path, min_date, min_up);
}, true);

function prime_object(len) {
	var prime = [];

	while(len--) {
		prime[len] = {
			x: len,
			y: 0,
			count: 0
		};
	}

	return prime;
}

function redraw_raw_data(element, data, prop, interpolation, annotations, format, color) {
	var raw = data.map(function (item) {
		return {
			x: item.date,
			y: item[prop]
		};
	});

	var graph = new Rickshaw.Graph({
		element: element,
		width: 300,
		height: 200,
		interpolation: interpolation,
		series: [
			{
				color: color,
				data: raw,
				name: prop
			}
		]
	});

	var notes = new Rickshaw.Graph.Annotate({
		graph: graph,
		element: element.parentNode.querySelector('.timeline')
	});

	annotations.forEach(function (item) {
		notes.add(item.date, item.message);
	});

	var x_axis = new Rickshaw.Graph.Axis.Time( { graph: graph } );

	var y_axis = new Rickshaw.Graph.Axis.Y( {
		graph: graph,
		tickFormat: format
	} );

	var hoverDetail = new Rickshaw.Graph.HoverDetail( {
		graph: graph,
		yFormatter: format,
		formatter: function(series, x, y, formattedX, formattedY) {
			var date = '<span class="date">' + formattedX + '</span>';
			var content = date + '<br />' + series.name + ": " + formattedY;
			return content;
		}
	} );

	graph.render();
}

function redraw_time_histogram(element, data, prop, method, format_data, color) {

	var method_lookup = {
			month: {
				method: 'getUTCMonth',
				intervals: 12,
				format: Formatters.months_of_year
			},
			day: {
				method: 'getUTCDay',
				intervals: 7,
				format: Formatters.day_of_week
			},
			hour: {
				method: 'getUTCHours',
				intervals: 24,
				format: Formatters.hours_of_day
			},
			minute: {
				method: 'getUTCMinutes',
				intervals: 60,
				format: undefined
			},
			second: {
				method: 'getUTCSeconds',
				intervals: 60,
				format: undefined
			}
		},
		time_props = method_lookup[method];

	// Calculate the histogram
	var histogram = data.map(function (item) {
		return {
			x: (new Date(item.date * 1000))[time_props.method](),
			y: item[prop]
		};
	});

	histogram = histogram.reduce(function (previousValue, currentValue, index, array) {
		var x = currentValue.x;

		previousValue[x].y += currentValue.y;
		previousValue[x].count++;

		return previousValue;
	}, prime_object(time_props.intervals));

	histogram = histogram.map(function (item) {
		return {
			x: item.x,
			y: (item.count ? item.y / item.count : 0)
		};
	});

	console.log(histogram);

	// Draw the graph
	var graph = new Rickshaw.Graph({
		element: element,
		width: 300,
		height: 200,
		renderer: 'bar',
		series: [
			{
				color: color,
				data: histogram,
				name: 'average ' + prop
			}
		]
	});

	var x_axis = new Rickshaw.Graph.Axis.X( {
		graph: graph,
		tickFormat: time_props.format
	} );

	var y_axis = new Rickshaw.Graph.Axis.Y( {
		graph: graph,
		tickFormat: format_data
	} );

	var hoverDetail = new Rickshaw.Graph.HoverDetail( {
		graph: graph,
		xFormatter: time_props.format,
		yFormatter: format_data,
		formatter: function(series, x, y, formattedX, formattedY) {
			var date = '<span class="date">' + formattedX + '</span>';
			var content = date + '<br />' + series.name + ": " + formattedY;
			return content;
		}
	} );

	graph.render();
}

// the prop is assumed to be normalized between 0..1
function redraw_buckets_histogram(element, data, prop, color, buckets) {
	// Calculate the histogram
	var PIVOT = 10,
		histogram = data.map(function (item) {
			return {
				x: Math.floor(item[prop] * (buckets - 1)),
				y: 1
			};
		});

	histogram = histogram.reduce(function (previousValue, currentValue, index, array) {
		var x = currentValue.x;

		previousValue[x].y += currentValue.y;

		return previousValue;
	}, prime_object(buckets));

	// Draw the graph
	var graph = new Rickshaw.Graph({
		element: element,
		width: 300,
		height: 200,
		renderer: 'bar',
		series: [
			{
				color: color,
				data: histogram,
				name: 'samples'
			}
		]
	});

	function buckets_formatter(y) {
		return truncate(y * (PIVOT / buckets) * PIVOT, 2) + '%';
	}

	var x_axis = new Rickshaw.Graph.Axis.X( {
		graph: graph,
		tickFormat: buckets_formatter
	} );

	var y_axis = new Rickshaw.Graph.Axis.Y( {
		graph: graph
	} );

	var hoverDetail = new Rickshaw.Graph.HoverDetail( {
		graph: graph,
		xFormatter: buckets_formatter,
		formatter: function(series, x, y, formattedX, formattedY) {
			var date = '<span class="date">' + formattedX + '</span>';
			var content = date + '<br />' + series.name + ": " + formattedY;
			return content;
		}
	} );


	graph.render();
}

function redraw_scatter(element, data, props, format_data, color) {
	function pluck_x(d) {
		return d[props.x];
	}

	function pluck_y(d) {
		return d[props.y];
	}

	function pluck_color(d) {
		return d[props.color];
	}

	var WIDTH = 900,
		HEIGHT = 200,
		x_scale = d3.scale.linear()
			.nice()
			.domain([0, d3.max(data, pluck_x)])
			.range([24, WIDTH - 28]),
		y_scale = d3.scale.linear()
			.nice()
			.domain([0, d3.max(data, pluck_y)])
			.range([24, HEIGHT - 28]),
		color_scale = d3.scale.linear()
			.domain([0, 0.5, 1])
			.range(['#E34282', '#F2C2D2', color]);

	var svg = d3.select(element)
			.append("svg")
			.attr("width", WIDTH)
			.attr("height", HEIGHT),
		popover = document.querySelector('#up-duration-popover'),
		popover_date_number = popover.querySelector('.date.number'),
		popover_up_number = popover.querySelector('.up.number'),
		popover_duration_number = popover.querySelector('.duration.number'),
		popover_half_height = 0,
		CURSOR_HALF_WIDTH = 10;

	// draw scatter plot
	svg.selectAll('circle')
		.data(data)
		.enter()
		.append('circle')
		.attr('cx', function (d) {
			return x_scale(pluck_x(d));
		})
		.attr('cy', function (d) {
			return y_scale(pluck_y(d));
		})
		.attr('r', 2.5)
		.attr('fill', function (d) {
			return color_scale(pluck_color(d));
		})
		.on('mouseover', function (d) {
			console.log(d);
			popover.style.display = 'block';
			popover_date_number.textContent = (new Date(d.date * 1000)).toString();
			popover_up_number.textContent = format_data.x(d.up);
			popover_duration_number.textContent = format_data.y(d.duration);
			popover_half_height = popover.offsetHeight / 2;
		})
		.on('mousemove', function (d) {
			popover.style.top = (d3.event.pageY - popover_half_height) + "px";
			popover.style.left = (d3.event.pageX + CURSOR_HALF_WIDTH) + "px";
		})
		.on('mouseout', function (d) {
			console.log(d);
			popover.style.display = '';
		});

	// draw axes
	var x_axis = d3.svg.axis()
		.scale(x_scale)
		.tickFormat(format_data.x)
		.orient('bottom');

	svg.append('g')
		.attr('class', 'axis x-axis')
		.call(x_axis);

	var y_axis = d3.svg.axis()
		.scale(y_scale)
		.tickFormat(format_data.y)
		.orient('right');

	svg.append('g')
		.attr('class', 'axis y-axis')
		.call(y_axis);
}

function redraw_graph(path, min_date, min_up) {

	var charts_container = document.querySelector('.js-chart-container');

	// empty charts_container
	charts_container.innerHTML = '';

	// repopulate it from the status we stored earlier
	for (var chart = 0; chart < charts_container_prime.childNodes.length; chart++) {
		charts_container.appendChild(charts_container_prime.childNodes[chart].cloneNode(true));
	}

	var palette = new Rickshaw.Color.Palette({
			scheme: 'spectrum14'
		}),
		up_chart =  document.querySelector("#up-chart"),
		up_buckets_chart = document.querySelector("#up-buckets-chart"),
		up_monthly_chart = document.querySelector("#up-monthly-chart"),
		up_weekly_chart = document.querySelector("#up-weekly-chart"),
		up_daily_chart = document.querySelector("#up-daily-chart"),
		duration_chart = document.querySelector("#duration-chart"),
		duration_monthly_chart = document.querySelector("#duration-monthly-chart"),
		duration_weekly_chart = document.querySelector("#duration-weekly-chart"),
		duration_daily_chart = document.querySelector("#duration-daily-chart"),
		up_duration_chart = document.querySelector("#up-duration-chart");

	d3.json('/aggregate/by_name/?name=' + path, function (err, flat_data) {

		if (err) {
			throw err;
		}

		var data = flat_data;

		//var unsampled_data = unsample(data, 'up');
		//console.log(unsampled_data);

		if (!data.length) {
			return;
		}

		d3.json('/annotations/', function (err, annotations) {

			if (err) {
				throw err;
			}

			color = palette.color();
			redraw_scatter(up_duration_chart, data, {
				y: 'duration',
				x: 'up',
				color: 'up'
			}, {
				y: Formatters.short_duration,
				x: Formatters.percent
			}, color);

			color = palette.color();
			redraw_raw_data(up_chart, data, 'up', 'step-after', annotations, Formatters.percent, color);
			//redraw_raw_data(up_chart, unsampled_data, 'up', 'step-after', annotations, Formatters.percent, color);
			redraw_buckets_histogram(up_buckets_chart, data, 'up', color, 20);
			redraw_time_histogram(up_monthly_chart, data, 'up', 'month', Formatters.percent, color);
			redraw_time_histogram(up_weekly_chart, data, 'up', 'day', Formatters.percent, color);
			redraw_time_histogram(up_daily_chart, data, 'up', 'hour', Formatters.percent, color);

			color = palette.color();
			redraw_raw_data(duration_chart, data, 'duration', 'linear', annotations, Formatters.short_duration, color);
			redraw_time_histogram(duration_monthly_chart, data, 'duration', 'month', Formatters.short_duration, color);
			redraw_time_histogram(duration_weekly_chart, data, 'duration', 'day', Formatters.short_duration, color);
			redraw_time_histogram(duration_daily_chart, data, 'duration', 'hour', Formatters.short_duration, color);

		});
	});
}


/*var path_selector = document.querySelector('#path-selector'),
	path = '';

path_selector.addEventListener('change', function (e) {
	path = path_selector[path_selector.selectedIndex].value
	redraw_graph(path);
}, true);

function draw_raw_data(options, filter, grouped) {
	var by_month = filter.dimension(function (d) {
			return {
				date: d.date,
				up: d.up
			};
		}),
		upness_by_month = by_month.group();

	group

	dc.lineChart(options.selector)
		.width(300)
		.height(200)
		.dimension(by_month)
		.group(upness_by_month)
		.elasticX(true)
		.keyAccessor(function (record) {
			console.log(record);
			return record.date;
		})
		.valueAccessor(function (record) {
			console.log(record);
			return record.up;
		})
		.x(d3.time.scale.utc());
}

function draw_histogram(options, filter, grouped) {
	var by_month = filter.dimension(function (d) {
			return d.up;
		}),
		upness_by_month = by_month.group(function (v) {
			return Math.floor(v * 10) * 10;
		});

	upness_by_month.reduceCount();

	dc.barChart(options.selector)
		.width(300)
		.height(200)
		.dimension(by_month)
		.group(upness_by_month)
		.x(d3.scale.linear().domain([0, 100]));
}

function redraw_graph(path) {
	d3.json('/aggregate/by_name/?name=' + path, function (err, data) {
		if (err) {
			throw err;
		}

		var filter = crossfilter(data),
			grouped = filter.groupAll();

		draw_raw_data({
			selector: '#up-chart'
		}, filter, grouped);

		draw_histogram({
			selector: '#up-buckets-chart'
		}, filter, grouped);

		dc.renderAll();

	});
}*/
