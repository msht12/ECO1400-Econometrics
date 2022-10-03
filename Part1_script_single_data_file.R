# Author: Eric Nussbaum
# Date created: 2022-09-23

library(readr)
library(tidyverse)
library(sysfonts)
library(tidyquant)
library(stringr)

library(dplyr)
library(qwraps2)
library(stargazer)
library(xtable)

#font_add_google("Fira Sans Condensed", "Fira Sans Condensed")
theme_set(theme_bw(base_family = "Fira Sans Condensed"))

rm(list = ls())

# Load data ----
data <- read_csv("stocks_and_3yearbonds_long_format_monthly.csv", 
                                                 skip = 9)
data <- data %>%
  as_tibble() %>% 
  mutate(Date = as.Date(Date, format = "%m/%d/%Y"))

#data <- mutate(data, 
#               .after = Date,
#               year = as.double(strftime(data$Date, format = "%Y")),
#               month = as.double(strftime(data$Date, format = "%m")),
#               day = as.double(strftime(data$Date, format = "%d")))

# stock tickers
tickers = c("RTX", "BBBY", "PFE", "SHOP", "LBLCF", "TRI")

stocks_monthly_returns <- data %>% 
  filter(Ticker %in% tickers) %>% 
  group_by(Ticker) %>% 
  tq_transmute(select = Close,
               mutate_fun = periodReturn,
               period = 'monthly',
               col_rename = 'returns')

stocks_monthly_returns %>%
  ggplot(aes(x = Date, y = returns, color = Ticker)) +
  geom_line()

## Combine stocks and bond data ----

# Bond close values are in percent per annum

data_bond_returns <- data %>% 
  filter(Ticker %in% c("IGCAN3D", "IGUSA3D")) %>% 
  mutate(.after = Date,
         returns = (1 + Close/100)^(1/12) - 1)

#stocks_and_bonds <- full_join(stocks_monthly_returns, 
#                              data_bond_returns,
#                              by = c("Date", "Ticker"))

stocks_and_bonds <- rbind(stocks_monthly_returns,
                          select(data_bond_returns, 
                                 colnames(stocks_monthly_returns)))

# Dropping first date where return is 0 by convention
stocks_and_bonds <- filter(stocks_and_bonds, Date != "2016-01-31") 
# Change to percentage monthly returns from decimal monthly returns
stocks_and_bonds <- mutate(stocks_and_bonds, returns = returns * 100) 

stocks_and_bonds %>%
  ggplot(aes(x = Date, y = returns, color = Ticker)) +
  geom_line()

## Make summary table ----

stats <- stocks_and_bonds %>% 
  group_by(Ticker) %>% 
  summarize(Min = min(returns),
            Q1 = quantile(returns, 0.25),
            Median = median(returns),
            Mean = mean(returns),
            Q3 = quantile(returns, 0.75),
            Max = max(returns),
            Var = var(returns),
            SD = sd(returns),
            VaR = qnorm(0.05, mean=mean(returns), sd=sd(returns) ) )
table <- xtable(stats, type = "latex", digits = 3)
print(table, file = "filename2.tex", include.rownames=FALSE)
 
# Using Tidyquant to download and process data ----

# TNX - US Treasury Yield 10 years
tickers = c("RTX", "BBBY", "PFE", "SHOP", "LBLCF", "TRI")

stocks <- tq_get(tickers,
                 from = "2016-01-01",
                 to = "2022-09-01",
                 get = "stock.prices")
# Plot prices
stocks %>% 
  ggplot(aes(x = date, y = adjusted, color = symbol)) +
  geom_line()

# Calculate monthly returns

stocks_monthly_returns <- stocks %>% 
  group_by(symbol) %>% 
  tq_transmute(select = adjusted,
               mutate_fun = periodReturn,
               period = 'monthly',
               col_rename = 'returns')

# Plot monthly returns
stocks_monthly_returns %>%
  ggplot(aes(x = date, y = returns, color = symbol)) +
  geom_line()

# Calculate stats on monthly returns



