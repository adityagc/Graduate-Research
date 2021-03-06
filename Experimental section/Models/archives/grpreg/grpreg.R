closeAllConnections()
rm(list=ls())

library(grpreg)
library(caret)
library(ggplot2)
data(Birthwt)
# Predictors: age   age   age   lwt   lwt   lwt   race  race  smoke ptl   ptl   ht    ui    ftv  ftv   ftv  
# Levels: age lwt race smoke ptl ht ui ftv
titles <- Birthwt
X <- Birthwt$X
Y <- Birthwt$bwt
set.seed(0)
groups <- c(1,1,1,2,2,2,3,3,4,5,5,6,7,8,8,8)
# lambdas <- c(0.01, 0.03, 0.035, 0.04, 0.045, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19)
lambdas <- seq(0.035, 0.04, by=0.001)
  
# Y <- log(Y)
Y_fit <- cv.grpreg(X, Y, group=groups, returnY = TRUE, nfolds = 4, lambda = lambdas)
jpeg("error-vs-lambda.jpg")
# plot(Y_fit, log.l = FALSE)
dev.off()
summ <- summary(Y_fit)
errors <- summ$cve
write.csv(errors, file = "~/Desktop/MS-Research/Experiments/LowBirthWeight/large-lbw/R/errors.csv")
weights <- Y_fit$fit$beta
write.csv(weights, file = "~/Desktop/MS-Research/Experiments/LowBirthWeight/large-lbw/R/weights.csv")
out <- rbind(weights, errors)
write.csv(out, file = "~/Desktop/MS-Research/Experiments/LowBirthWeight/large-lbw/R/out.csv")
out