CFLAGS=-std=c99
CFLAGS+=-fsignaling-nans
CFLAGS+=-g -ggdb3
CFLAGS+= -O5
LDFLAGS=-lm


all: gauss_solve

OBJS = gauss_solve.o main.o helpers.o
gauss_solve.o : gauss_solve.h
helpers.o: helpers.h

gauss_solve : $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $@ $(LDFLAGS)

check: gauss_solve
	./$<



LIB_SOURCES = gauss_solve.c
libgauss.so: $(LIB_SOURCES)
	gcc -shared -I/usr/include/python3.12 -o $@ -fPIC $(LIB_SOURCES)

clean: FORCE
	@-rm gauss_solve *.o
	@-rm *.so

FORCE:
