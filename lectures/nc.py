#!/usr/bin/env python3
"""
This program acts as a command-line interface to xarray 
"""
import xarray as xr
import argparse


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("file_in", help="NetCDF file to open")
	parser.add_argument("-p", "--print", action="store_true")
	parser.add_argument("-m", "--time_mean", help="Calculate the time mean and output to ARG")
	args = parser.parse_args()
	
	try:
		ds = xr.open_dataset(args.file_in)
	except Exception as e:
		print(f"Error opening file: {e}")
	else:
		if args.print:
			print(ds)
		elif args.time_mean:
			ds.mean('time').to_netcdf(args.time_mean)
		else:
			print("Choose an option to print or calculate mean")

