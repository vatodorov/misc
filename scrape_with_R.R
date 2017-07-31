


##### Scrape with CSS

install.packages("rvest")

url <- "https://www.expatistan.com/cost-of-living/boston?" 
indicators <- url %>% read_html(url) %>% html_nodes(".downlighted") %>% html_text() 
price <- url %>% read_html(url) %>% html_nodes(".price") %>% html_text() 
boston <- data.frame(indicators,price)






##### Scrape with XPath

install.packages(c("XML", "RCurl"))

library(RCurl)
library(XML)


## Extract information from resumes on Indeed.com
get_html <- getURL("http://www.indeed.com/r/Tessa-Merna/b209def65cf1a16d",
                   followlocation = TRUE)

doc <- htmlParse(get_html, asText = TRUE)
plain.text <- xpathSApply(doc, "//div/p[3]", xmlValue)

cat(paste(plain.text, collapse = "\n"))




## Search on Reuters
search_query <- "crude+oil" # separate words by "+" sign
sort_by <- "relevance"
date_range <- "pastYear"

get_html <- getURL(paste("http://www.reuters.com/search/news?blob=", search_query,
                         "&sortBy=", sort_by,
                         "&dateRange=", date_range,
                         sep = ""),
                   followlocation = TRUE)

doc <- htmlParse(get_html, asText = TRUE)

print(doc)


# plain.text <- xpathSApply(doc, "/section[2]/div/div[1]/div[3]/div/div[3]/div[1]/div[2]/h3/a", xmlValue)
# cat(paste(plain.text, collapse = "\n"))


