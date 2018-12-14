closeAllConnections()
rm(list=ls())

library(grpreg)
library(caret)
library(ggplot2)
t0 = proc.time()
data(Birthwt)
# Predictors: age   age   age   lwt   lwt   lwt   race  race  smoke ptl   ptl   ht    ui    ftv  ftv   ftv  
# Levels: age lwt race smoke ptl ht ui ftv

titles <- Birthwt
X <- Birthwt$X
Y <- Birthwt$bwt
set.seed(0)
groups <- c(1,1,1,2,2,2,3,3,4,5,5,6,7,8,8,8)
lambdas <- c(0.001, 0.01, 0.025, 0.05, 0.075, 0.1, 0.2, 0.5, 1)
# Y <- log(Y)
Y_fit <- cv.grpreg(X, Y, group=groups, returnY = TRUE, nfolds = 4, lambda = lambdas)
jpeg("error-vs-lambda.jpg")
# plot(Y_fit, log.l = FALSE)
dev.off()
summ <- summary(Y_fit)
errors <- summ$cve
# write.csv(errors, file = "~/Desktop/MS-Research/Experiments/LowBirthWeight/large-lbw/R/errors.csv")
weights <- Y_fit$fit$beta
# write.csv(weights, file = "~/Desktop/MS-Research/Experiments/LowBirthWeight/large-lbw/R/weights.csv")
out <- rbind(weights, errors)
t1 = proc.time()
time = t1-t0
write.csv(out, file = "./out.csv")
out