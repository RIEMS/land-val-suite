
SETUP=setup.nc
INIT=state/res.19980101T000000.nc
INPUT=input/in.19980101T000000.nc

all:$(SETUP) $(INPUT)

# setup
$(SETUP): setup.cdl
	ncgen -o $@ $^

# init
$(INIT): init.cdl
	ncgen -o $@ $^

# input
$(INPUT): input/make_input.py input/bondville.dat
	(cd input ; ./make_input.py)


clean:
	-rm $(SETUP)
	-rm $(INIT)
	-rm input/in.*.nc
	-rm output/out.*.nc
	-rm state/res.*.nc
