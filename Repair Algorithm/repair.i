%module jmotif
%{
#define __attribute__(x)
#include "jmotif.h"
#include <RcppArmadillo.h>
%}
%include "jmotif.h"
%include Rcpp.i 
%include <RcppArmadillo.h>
