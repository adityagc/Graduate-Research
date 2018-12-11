closeAllConnections()
rm(list=ls())

library(glmnet)
library(grpreg)
data(Birthwt)
X <- Birthwt$X
Y <- Birthwt$bwt
# groups <- c(1,1,1,2,2,2,3,3,4,5,5,6,7,8,8,8)
glm_object <- cv.glmnet(x=X, y=Y, nfolds=4, type.measure = "mse", grouped=TRUE, type.multinomial = "grouped")
weights <- coef(glm_object, s=c(0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1))
colnames(weights, do.NULL = FALSE)
colnames(weights) <- c(0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1)
write.csv(as.array(weights), file = "~/Desktop/MS-Research/Experiments/LowBirthWeight/large-lbw/R/glmnet-out.csv")
weights