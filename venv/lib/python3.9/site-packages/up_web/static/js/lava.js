var lamp = document.querySelector('#upness-lamp'),
	popover = document.querySelector('#lava-popover'),
	popover_title = popover.querySelector('.popover-title'),
	popover_content = popover.querySelector('.popover-content'),
	popover_up_number = popover.querySelector('.up.number'),
	popover_samples_numbers = popover.querySelector('.samples.number'),
	popover_half_height = 0,
	CURSOR_HALF_WIDTH = 10;

function redraw_scatter(element, data) {
	function pluck_x(d) {
		return Math.random();
	}

	function pluck_y(d) {
		return d.value.avg;
	}

	function pluck_r(d) {
		//console.log(typeof d.value.sum);
		return d.value.stddev;
	}

	function pluck_color(d) {
		return d._id.split('/').length - 1;
	}

	var WIDTH = 400,
		HEIGHT = 600,
		x_scale = d3.scale.linear()
			.nice()
			.domain([0, 1])
			.range([10, WIDTH - 10]),
		y_scale = d3.scale.linear()
			.nice()
			.domain([1, 0])
			.range([10, HEIGHT - 10]),
		r_scale = d3.scale.linear()
			.nice()
			.domain([0, d3.max(data, pluck_r)])
			.range([4, 20]),
		color_scale = d3.scale.category20()
			.domain([0, d3.max(data, pluck_color)]);

	var svg = d3.select(element)
		.append("svg")
		.attr("width", WIDTH)
		.attr("height", HEIGHT);

	// draw scatter plot
	var circles = svg.selectAll('.circle')
		.data(data)
		.enter()
		.append('a')
			.attr('xlink:href', function (d) {
				return '/#' + d._id;
			})
			.attr('class', 'circle')
			.attr('transform', function (d) {
				return 'translate(' + x_scale(pluck_x(d)) + ',' + y_scale(pluck_y(d)) + ')';
			})
			.sort(function (a, b) {
				return pluck_color(b) - pluck_color(a);
			})
			.on('mouseover', function (d) {
				// highlight the item
				d3.select(this)
					.select('.circle-highlight')
					.transition()
					.duration(250)
					.attr('opacity', 1);

				// populate text content
				popover_title.textContent = d._id;
				popover_up_number.textContent = (d.value.avg * 100).toFixed(2);
				popover_samples_numbers.textContent = d.value.count;

				// show it
				popover.style.display = 'block';

				// measure it
				popover_half_height = popover.offsetHeight / 2;
			})
			.on('mousemove', function (d) {
				popover.style.top = (d3.event.pageY - popover_half_height) + "px";
				popover.style.left = (d3.event.pageX + CURSOR_HALF_WIDTH) + "px";
			})
			.on('mouseout', function (d) {
				d3.select(this)
					.select('.circle-highlight')
					.transition()
					.duration(250)
					.attr('opacity', 0);

				popover.style.display = '';
			});

	circles
		.append('circle')
			.attr('r', function (d) {
				//console.log(r_scale(pluck_r(d)));
				return r_scale(pluck_r(d));
			})
			.attr('fill', function (d) {
				//console.log(pluck_color(d), d._id);
				return color_scale(pluck_color(d));
			});

	circles
		.append('circle')
			.attr('stroke', 'white')
			.attr('stroke-width', '2px')
			.attr('fill', 'none')
			.attr('class', 'circle-highlight')
			.attr('r', function (d) {
				//console.log(r_scale(pluck_r(d)));
				var radius = r_scale(pluck_r(d)) - 4;
				return (radius > 0)? radius : 0;
			})
			.attr('opacity', 0);
}

d3.json('/aggregate/by_name/by_upness', function (err, data) {
	if (err) {
		throw err;
	}

	redraw_scatter(lamp, data);
});
