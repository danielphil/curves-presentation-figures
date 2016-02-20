all: output/labelled_plot.png output/basic_animation.gif output/sequence_of_points.png output/sequence_of_points100.png output/hermite_tangents.gif

output/sequence_of_points100.png: sequence_of_points.py helpers.py
	python sequence_of_points.py

output/sequence_of_points.png: sequence_of_points.py helpers.py
	python sequence_of_points.py

output/labelled_plot.png: test.py helpers.py
	python test.py
    
output/basic_animation.gif: test2.py helpers.py
	python test2.py

output/hermite_tangents.gif: hermite_tangents.py helpers.py
	python hermite_tangents.py
	
clean:
	rm output/labelled_plot.png output/basic_animation.gif output/sequence_of_points.png output/sequence_of_points100.png output/hermite_tangents.gif
