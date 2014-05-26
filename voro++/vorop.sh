#!/usr/bin/env bash

voro++ -px -py -c "%i %n" 0 $1 0 $2 0 1 $3 && \
    mv $3.vol $3pxpy.vol

voro++ -px -c "%i %n" 0 $1 0 $2 0 1 $3 && \
    mv $3.vol $3px.vol

voro++ -py -c "%i %n" 0 $1 0 $2 0 1 $3 && \
    mv $3.vol $3py.vol

voro++ -c "%i %n" 0 $1 0 $2 0 1 $3 && \
    mv $3.vol $3np.vol

voro++ -p -g 0 $1 0 $2 0 1 $3

