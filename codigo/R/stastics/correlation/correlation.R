library(corrplot)

# Import the datasets needed for chapter 1

PSDS_PATH <- file.path(dirname(dirname(getwd())))

sp500_px <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'sp500_data.csv.gz'), row.names=1)
sp500_sym <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'sp500_sectors.csv'), stringsAsFactors = FALSE)

telecom <- sp500_px[, sp500_sym[sp500_sym$sector == 'telecommunications_services', 'symbol']]
telecom <- telecom[row.names(telecom) > '2012-07-01',]
telecom_cor <- cor(telecom)

telecom_cor

etfs <- sp500_px[row.names(sp500_px) > '2012-07-01', 
                  sp500_sym[sp500_sym$sector == 'etf', 'symbol']]

corrplot(cor(etfs), method='ellipse')