all: labelled_plot.png basic_animation.gif sequence_of_points.png sequence_of_points100.png

sequence_of_points100.png: sequence_of_points.py helpers.py
	python sequence_of_points.py

sequence_of_points.png: sequence_of_points.py helpers.py
	python sequence_of_points.py

labelled_plot.png: test.py helpers.py
	python test.py
    
basic_animation.gif: test2.py helpers.py
	python test2.py
	
clean:
	rm labelled_plot.png basic_animation.gif
