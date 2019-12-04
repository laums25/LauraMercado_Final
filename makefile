sigma.png : primer.py
	python primer.py

resultado.png : primer.dat primer.py
	python primer.py

primer.dat  : primer.x
	./primer.x 

primer.x : primer.cpp
	c++ primer.cpp -o primer.x
	
