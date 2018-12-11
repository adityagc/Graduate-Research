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
Y <- as.vector(Birthwt$bwt)
set.seed(0)
groups <- c(1,1,1,2,2,2,3,3,4,5,5,6,7,8,8,8)
lambdas <- c(0.01, 0.03, 0.035, 0.04, 0.045, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19)
lambdas <- seq(0.01, 0.03, by=0.001)
# lambdas <- seq(0.035, 0.04, by=0.001)

# Log transforming the response variable for training.
Ylog <- log(Y)
Y_log_fit <- cv.grpreg(X, Ylog, group=groups, returnY = TRUE, nfolds = 4, lambda = lambdas)
Ytrans <- exp(Y_log_fit$Y)
errors <- NULL
for (i in 1:length(lambdas)) {
  errors <- c(errors, mse(Y, Ytrans[,i]))
}
jpeg("error-vs-lambda.jpg")
# plot(Y_fit, log.l = FALSE)
dev.off()
# summ <- summary(Y_log_fit)
# errors <- summ$cve
write.csv(errors, file = "~/Desktop/MS-Research/Experiments/LowBirthWeight/large-lbw/R/retransform-log-transform-errors.csv")
weights <- Y_log_fit$fit$beta
write.csv(weights, file = "~/Desktop/MS-Research/Experiments/LowBirthWeight/large-lbw/R/retransform-log-transform-weights.csv")
out <- rbind(weights, errors)
write.csv(out, file = "~/Desktop/MS-Research/Experiments/LowBirthWeight/large-lbw/R/retransform-log-tranform-out.csv")
out 