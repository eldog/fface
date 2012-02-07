IFLAGS = `pkg-config --cflags opencv` 
LFLAGS = `pkg-config --libs opencv`

all: congealReal funnelReal

clean:
	rm congealReal funnelReal

congealReal: congealReal.cpp
	g++ -o congealReal congealReal.cpp $(IFLAGS) $(LFLAGS) 

funnelReal: funnelReal.cpp
	g++  -o funnelReal funnelReal.cpp $(IFLAGS) $(LFLAGS)
