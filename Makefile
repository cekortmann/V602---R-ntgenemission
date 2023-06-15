all: build/v602.pdf

build/v602.pdf: v602.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v602.tex
	lualatex  --output-directory=build v602.tex
	biber build/v602.bcf
	lualatex  --output-directory=build v602.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
