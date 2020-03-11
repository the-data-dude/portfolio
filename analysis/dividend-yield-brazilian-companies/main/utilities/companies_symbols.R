#push all the companies symbols

url <- "https://br.advfn.com/bolsa-de-valores/bovespa/"
  
companies_symbols = data.frame(empresa = character(), simbolo = character())

  
for(letter in c(LETTERS)){

  html <- read_html(glue(url,letter))

  page_table <- tryCatch(html %>% html_node("table") %>% html_table(), error = function(e) NULL)

  if(!is.null(page_table)) {

    colnames(page_table) <- c("empresa", "simbolo")
    page_table$empresa <- toupper(page_table$empresa)
    companies_symbols <- rbind(companies_symbols, page_table)
  
  }
  
}


companies_symbols$simbolo <- paste(companies_symbols$simbolo, ".SA", sep = "")

