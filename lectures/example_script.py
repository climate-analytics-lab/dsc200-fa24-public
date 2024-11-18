#!/usr/bin/env python3
import argparse

# This is a more complex Python module, that I can execute directly and accepts arguments

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("x", type=int, help="the base")
	parser.add_argument("y", type=int, help="the exponent")
	parser.add_argument("-v", "--verbosity", action="count", default=0)
	args = parser.parse_args()
	answer = args.x**args.y
	if args.verbosity >= 2:
	    print(f"Running '{__file__}'")
	if args.verbosity >= 1:
	    print(f"{args.x}^{args.y} == ", end="")
	print(answer)

