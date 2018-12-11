closeAllConnections()
rm(list=ls())

library(Metrics)
library(grpreg)
library(caret)
library(ggplot2)
data(Birthwt)
# Predictors: age   age   age   lwt   lwt   lwt   race  race  smoke ptl   ptl   ht    ui    ftv  ftv   ftv  
# Levels: age lwt race smoke ptl ht ui ftv
titles <- Birthwt
X <- Birthwt$X
X <- cbind(X, 1)
W <- c(-0.30, 0.46, 0.35, 0.63, 0.16, 0.42, 0.15, 0, - 0.13, 0, 0, - 0.26, -0.22, 0, 0, 0, 1.1)
Y <- as.vector(Birthwt$bwt)
Yhatlog <- X %*% W
Yhat <- exp(Yhatlog)
err <- mse(Y, Yhat)
