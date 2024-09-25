CFLAGS=-std=c99
CFLAGS+=-fsignaling-nans
CFLAGS+=-g -ggdb3
CFLAGS+= -O5
CFLAGS+= /usr/include/python3.12 # Only to make a Python extension
LDFLAGS=-lm


all: gauss_solve

OBJS = gauss_solve.o main.o helpers.o
gauss_solve.o : gauss_solve.h
helpers.o: helpers.h

gauss_solve : $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $@ $(LDFLAGS)


foo.so: foo.c foo.h
	gcc -shared -o libfoo.so -fPIC foo.c



check: gauss_solve
	./$<

clean: FORCE
	@-rm gauss_solve *.o

FORCE:
