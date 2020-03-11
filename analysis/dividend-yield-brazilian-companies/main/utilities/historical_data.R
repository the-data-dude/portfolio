historical_data <- tq_get(companies_symbols$simbolo, get = "stock.prices", from = "2019-01-01", complete_cases = TRUE)

dividends <- tq_get(companies_symbols$simbolo, get = "dividends", from = "2019-01-01", complete_cases = TRUE)

historical_data <- left_join(historical_data, dividends, by = c("symbol", "date"))
