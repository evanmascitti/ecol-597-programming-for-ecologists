#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws (for now) a dummy scatterplot taking one or two years as
# inputs and choices about how to summarize or compare the data

ui <- fluidPage(
  
  # Application title
  titlePanel("Weather of PA"),
  
  # Sidebar with a slider input for year
  # Also use a checkbox to allow user to display data as county-level summary
  # instead of the full raster data set
  
  sidebarLayout(
    sidebarPanel(
      sliderInput("year1", label = "Year 1", value = 1985,
                  min = 1980, max = 2015, step = 1, sep = ""),
      checkboxInput(inputId = "county_level", label = "Use county-level summaries"),
      checkboxInput(inputId = "historical_comp", label = "Compare with another year:"),
      sliderInput("year2", label = "Year 2", value = 2015,
                  min = 1980, max = 2015, step = 1, sep = ""),
      width = 3
    ),
    
    # Include a map and a data table, on separate rows
    
    mainPanel(
      column( width = 9,
              fluidRow(
                plotOutput("weather_map"),
                style = "height:90%"
              ),
              fluidRow(
                tableOutput("weather_table")
              )
      )
    )
  )
)

# Define server logic required to draw the map and table 

server <- function(input, output) {
  
  # Data wrangling happens inside a call to `reactive()`
  # This assigns the results to a reactive variable 
  # `reactive()` permits multiple output components to reference 
  # the same reactive element but for the element to be computed only once.
  
  # In this statement, the variable `map_data_year1` is conditionally assigned
  # as either the county-level summaries or the full data set.
  # By placing the summary first in the call, the full data set will never 
  # be computed if the user specifies that they want to see the county-level
  # summaries. Should make app faster?
  
  map_data_year1 <- reactive({
    
    if(input$county_level == TRUE){
      
      # code to produce county-level summaries goes here
      
      # here's a dummy data frame:
      
      data.frame(
        x <-  1:input$year1, 
        y = 1:input$year1 + rnorm(input$year1, 0, 100),
        year = input$year1
      )
      
    } else{
      
      # code to create full data goes here
      
      # here's a dummy data frame which is twice as large as the county-level one:
      
      data.frame(
        x = rep(1:input$year1, 2),
        y = c(replicate(expr = 1:input$year1 + rnorm(input$year1, 0, 100), n = 2)),
        year = input$year1
      )
      
    }
  })
  
  
  ########
  
  # Compute data for second year to compare against first year, but only 
  # if user has checked box for historical comparison
  
  map_data_year2 <- reactive({
    
    if(input$historical_comp == TRUE){
      
      # code to produce county-level summaries goes here
      # should be same code as for the year 1 data ?
      
      
    } else{
      
      # code to create full data goes here
      # should be same code as for the year 1 data ?
      
    }
  })
  
  ########
  
  
  # To reference a reactive variable, use parentheses as if it were a 
  # a function, for example: `summary(map_data())`
  # Here the variable is referenced in both the plot and the table
  
  
  # This is where the code to create the map goes....I put a dummy 
  # plot here which computes some random numbers, but the structure should
  # work the same way using the real data and calling map_data_year1() and  
  # (if applicable) map_data_year2()
  
  # You will notice that the size of the data set changes 
  # based on the checkbox for "use county-level summaries"
  
  # I did not yet create any output based on the `historical_comp` input.
  
  output$weather_map <- renderPlot({plot(x = map_data_year1()$x,
                                         y = map_data_year1()$y,
                                         xlab = "x", 
                                         ylab = "y", 
                                         main = "Some random numbers")
  })
  
  # This is another dummy output, it is a table containing information
  # about the set of random numbers. We could put a weather summary in here 
  
  output$weather_table <- renderTable({data.frame(
    `Year chosen` = unique(map_data_year1()$year),
    `Number of points` = length(map_data_year1()$year)
  )
  })
  
  
}

# Run the application 
shinyApp(ui = ui, server = server)
