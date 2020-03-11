#install all necessary packages from the necessary_packages.txt

necessary_packages <- suppressWarnings(read.delim(paste(getwd(), "/necessary_packages.txt", sep = ""), header = FALSE, stringsAsFactors = FALSE)[,1])

packages_i_dont_have <- subset(necessary_packages, !(necessary_packages %in% installed.packages()[,1]))

if(length(packages_i_dont_have) > 0) {
  install.packages(packages_i_dont_have)
}


                    
                    