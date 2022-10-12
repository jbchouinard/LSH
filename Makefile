default: build

build-deps:
	pip install cython pybind11 numpy

build:
	python setup.py build_ext --inplace
	python setup.py bdist_wheel

install: build
	python setup.py install

clean:
	python setup.py clean
	rm -rf build dist
	rm -f lsh/*.so
	rm -f lsh/cMinhash.cpp

.PHONY: build build-deps clean
