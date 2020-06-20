
INIT=init.nc
INPUT=input/LDASIN.19980101T000000.nc

all:$(INIT) $(INPUT)

# initial condition
$(INIT): init.cdl
	ncgen $^ -o $@

# input
$(INPUT): input/make_input.py input/bondville.dat
	(cd input ; ./make_input.py)


clean:
	-rm $(INIT)
	-rm input/LDASIN.*.nc
	-rm output/LDASOUT.*.nc
	-rm state/RESTART.*.nc
