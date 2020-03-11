#load libraries

necessary_packages <- suppressWarnings(read.delim(paste(getwd(), "/necessary_packages.txt", sep = ""), header = FALSE, stringsAsFactors = FALSE)[,1])

lapply(necessary_packages, require, character.only = TRUE)
 