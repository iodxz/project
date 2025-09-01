import pygame as pg

root = pg.display.set_mode((600, 600))
pg.display.set_caption('TSP')
root.fill('black')
run = True
circle_color = (255, 236, 216)
line_color = (255, 255, 0)
point_rad = 6
points = []
road_width = 2
limit_dist = 30
def draw_point(x, y):
	p = pg.draw.circle(root, circle_color, (x, y), point_rad)
	points.append([p.x, p.y])
def draw_lines():
	in_road = [points[-1]]
	out_road = points[0:-1]
	while len(out_road) != 0:
		for _in_ in in_road:
			if len(out_road) == 0:
				break
			last_point = in_road[-1]
			min_d = float('inf')
			point_to_build = None
			for _out_ in out_road:
				xi = last_point[0]
				yi = last_point[-1]
				xo = _out_[0]
				yo = _out_[-1]
				d = ((xo - xi) ** 2 + (yo - yi) ** 2) ** 0.5
				if d < min_d:
					min_d = d
					point_to_build = _out_
			xds = in_road[-1][0] + 3
			yds = in_road[-1][-1] + 3
			xde = point_to_build[0] + 3
			yde = point_to_build[-1] + 3
			pg.draw.line(root, line_color, (xds, yds), (xde, yde), road_width)
			in_road.append(point_to_build)
			out_road.remove(point_to_build)
def cheak_point(xp, yp):
	if len(points) <= 1:
		return True
	else:
		for p in points:
			px = p[0]
			py = p[-1]
			if abs(xp - px) < limit_dist or abs(yp - py) < limit_dist:

				return False
		return True
setup_end = False
while run:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		if event.type == pg.MOUSEBUTTONDOWN and (event.button == 1 and setup_end == False):
			if cheak_point(event.pos[0], event.pos[1]):
				draw_point(event.pos[0], event.pos[1])
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
				setup_end = True
				draw_lines()
			if event.key == pg.K_BACKSPACE:
				root.fill('black')
				pg.display.flip()
				points = []
				setup_end = False

		pg.display.update()
pg.quit()
