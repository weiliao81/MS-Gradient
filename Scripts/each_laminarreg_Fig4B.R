#####################################################################
### 
### Fig4B: relative importance of each laminar regression
### using the testing data as Fig4B_testdata.csv
### Please cite: Yang Siqi, et al. Cortical patterning of morphometric similarity gradient reveals diverged hierarchical organization in sensory-motor cortices
###
#####################################################################

## if no relaimpo, install it first
## install.packages("relaimpo")

library(relaimpo)

## load MS gradient data (n*1) and six laminar thickness (n*6)
## NOTE: MS_data is a n*7 matrix including MS gradient following laminar thickness
MS_data<-read.csv('G:/Fig4B_testdata.csv')

crf <- calc.relimp(MS_data,  type = c("pmvd" ))

##show the results
crf


## calcauting bootstrap confidence intervals for relative importances
bootMS=boot.relimp(MS_data, bty = "perc", level = 0.95, type = c( "pmvd"), rela = TRUE, fixed = FALSE)
bootcrf <-booteval.relimp(bootMS, bty = "perc", level = 0.95)

##show the bootstrap CI 
bootcrf

