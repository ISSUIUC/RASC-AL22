CC=gcc
FF=gfortran
CFLAGS=-O0 -Wall -I. -g
FFLAGS=-ffree-line-length-512 -ffree-form

main: main.c
	$(CC) $(CFLAGS) -o main.out $^

test: main
	./main.out

fortran: Rodwell_Code_2.f
	$(FF) $(CFLAGS) $(FFLAGS) -o fortran.out $^

test-fortran: fortran
	rm OUTPUT_MARS.DAT
	./fortran.out

clean:
	rm *.out

goto: goto.c
	$(CC) $(CFLAGS) -o goto.out $^

test-goto: goto
	./goto.out

fortran-goto: fortran_goto.f
	$(FF) $(CFLAGS) $(FFLAGS) -o fortran_goto.out $^

test-fortran-goto: fortran-goto
	rm fortrangoto.txt
	./fortran_goto.out
