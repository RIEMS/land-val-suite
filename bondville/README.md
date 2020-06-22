# Bondville

This `README` helps you set a simulation up.

It also describes the prerequisite files for simulation. The files contain the information of configurations, static parameters, and atmospheric forcings. With the descriptions, you should be able to prepare your own simulations.

## Build

The model reads and writes NetCDF files for static parameters, initial conditions, forcings, outputs, and restarts. NetCDF is a binary file format. In this repository, the content of all these NetCDF files is saved in a text format, for the convenience of content tracking.

Run `make` at the command line to convert these text files back to NetCDFs. To be specific, `make` does the following.

- Generate `init.nc` from `init.cdl`. The `init.cdl` describes the content of `init.nc` using the Common Data Language. You can use a text editor to inspect the initial conditions and parameters and modify them if necessary.
- Generate a series of forcing files into the `input` directory. A Python script, `input/make_input.py`, carries the generation out. The script reads the forcing data stored in `input/bondville.dat` and writes them to NetCDF files based on the template `input.yyyymmddTHHMMSS.cdl`.

## Run

Under this directory, type `ldas.exe` at the command line to run the simulation.

Model outputs can be found in the `output` directory, while the `state` directory stores restart files.

## Clean

Run `make clean` to clean the generated initialization, forcing, output, and restart files.

## Files explained for preparing your own data

The following files are mandatory for a simulation. They contain the information of model configurations, static parameters, initial conditions, and atmospheric forcings. To run your own simulations, you have to prepare your configurations and data in the same format.

| File | Descriptions |
| :-- | :-- |
| `ldas.namelist` | The configurations of the simulation and model. |
| `init.nc` | Static parameters and initial conditions. Check `init.cdl` for detailed formats. The file name can be changed in `ldas.namelist`. |
| `input/LDASIN.yyyymmddTHHMMSS.nc` | Atmospheric forcings. Check `input.yyyymmddTHHMMSS.cdl` for details. The timestamp `yyyymmddTHHMMSS` is in UTC. The directory containing the forcing files (e.g., `input`) can be changed in `ldas.namelist`. |
