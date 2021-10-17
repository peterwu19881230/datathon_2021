currentDir=dirname(rstudioapi::getActiveDocumentContext()$path) #only works in RStudio console
setwd(currentDir)

library(tidyverse)
library(readxl)
t1=read_excel('Pizza_Case.xlsx')
t2=read_excel('Pizza_Customer Info.xlsx')
t3=read_excel('Pizza_Event.xlsx')

#t1 leftjoin t2 on Customer_Type leftjoin on _CASE_KEY
names(t1)[names(t1)=='Customer Type']='Customer_Type'
names(t1)[names(t1)=='Customer Location']='Customer_Location'

out=left_join(t3,t1,by='_CASE_KEY')
out=left_join(out,t2,by=c('Customer_Location','Customer_Type'))
out=unique(out[,c('_CASE_KEY','Variant','Pizza Type','Pizza Size','Weekday','Daytime','Customer_Location','Customer_Type','Revenue')])

write.table(out,file='out.tsv',quote=FALSE,sep="\t",row.names = FALSE)

