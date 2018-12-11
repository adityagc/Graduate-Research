library(grpreg)
library(grplasso)
data(Birthwt)
X <- Birthwt$X
Y <- Birthwt$bwt
groups <- c(1,1,1,2,2,2,3,3,4,5,5,6,7,8,8,8)
lambdas <- c(0.01, 0.03, 0.035, 0.04, 0.045, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19)
model <- grplasso(X, Y, groups, lambdas, weights = model = LinReg())