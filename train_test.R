# reading the data set from excel into R
library("xlsx")
setwd("~/Documents/WD_R_Python")
dat <- read.xlsx(file = "dat.xlsx")
sample(10, 4)
# randomly select 500 from 1000 numbers
# so we separate our data into train and test sets randomly
indices <- sample(1000, 500)
train <- dat[indices, ]
test <- dat[-indices, ]
