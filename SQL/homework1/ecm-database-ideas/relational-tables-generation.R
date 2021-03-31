install.packages("flextable")
library(tidyverse)
library(flextable)

strip_empty_rows <- function(df){
  df %>% 
    filter(if_all(.fns = ~!is.na(.)))
}

strip_empty_cols <- function(df){
  df %>% 
    select(where(~!all(is.na(.))))
}

dfs <- list.files(path = 'SQL/ecm-database-ideas/', pattern = "\\.csv$", full.names = T) %>% 
  purrr::set_names(nm = str_replace(string = ., "\\.csv$", "\\.pdf")) %>% 
  map(read_csv)%>% 
  map(strip_empty_cols) %>% 
  map(strip_empty_rows) %>% 
  map(flextable) %>% 
  map(fit_to_width, max_width = 3)

out_names <- names(dfs)

map2(dfs,out_names, flextable::save_as_image, webshot = 'webshot2')
