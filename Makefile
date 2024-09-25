CFLAGS=-std=c99
CFLAGS+=-fsignaling-nans
CFLAGS+=-g -ggdb3
CFLAGS+= -O5
LDFLAGS=-lm


all: gauss_solve libbar.so

OBJS = gauss_solve.o main.o helpers.o
gauss_solve.o : gauss_solve.h
helpers.o: helpers.h

gauss_solve : $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $@ $(LDFLAGS)


libbar.so: bar.c
	gcc -shared -I/usr/include/python3.12 -o $@ -fPIC bar.c


check: gauss_solve
	./$<

clean: FORCE
	@-rm gauss_solve *.o
	@-rm *.so

FORCE:
