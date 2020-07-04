# freeCodeCamp data science video notes

<https://www.youtube.com/watch?v=ua-CiDNNj30&>

From: <https://datalab.cc>

## Data Science Pathway

1. Planning
    1. Define goals
    2. Organized resources
    3. Coordinate people
    4. Schedule project
2. Data Prep
    1. Get data
    2. Clean data
    3. Explore data
    4. Refine data
        - choosing variables
        - choosing cases to include/exclude
        - data transformations
3. Modeling
    1. Create statistical model
        - regression analysis
        - neural network
        - etc
    2. Validate model
    3. Evaluate model
    4. Refine model
        - remove / add new variables
        - transform data
4. Follow Up
    1. Present model
    2. Deploy model
    3. Revisit model
    4. Archive assets

### Roles

1. Engineer
    - Focus on backend hardware and software
    - Makes DS possible
    - Developer, DBA
2. Big data
    - Focus on computer sience & math
    - Machine learning
    - Data products
3. Researchers
    - Focus on domain specific research
    - Physics, genetics
    - Strong statistics
4. Analysts
    - Day to day tasks
    - Web analytics, SQL
    - Provides info that is good for business
5. Business
    - Must be able to frame business relevant questions
    - Manages projects
    - Must "speak data"
6. Entrepreneur
    - Data startups
    - Needs data and business skills
    - Creative throughout
7. "Full stack unicorn"
    - Can do everything at a proficient level; may not exist

### Methods Overview

1. Sourcing
    - Getting the raw materials
        - Existing data
            - In house
            - Open data
            - Third party data
        - APIs
        - web scraping
        - creating data
            - Interviews
            - Surveys
            - Experiments
    - Pay attention to metrics & methods
        - Business metrics
        - KPI's
        - SMART goals (smart / actional / timely )
        - Classification accuracy
2. Coding
    - Any technology that lets you manipulate the data
    - Specialized apps for working with data
        - Spreadsheets
        - Visualization tools (Tableau)
        - SPSS
        - JASP
    - Special formats for web data
        - HTML
        - XML
        - JSON
    - Programming languages that give full control
        - R
        - Python
        - SQL
        - C / C++ / Java
        - BASH
        - Regex
3. Math - math behind DS methods
    - The foundation of data science
        - Need to know which procedures to use & why
        - Know what to do when things don't work right
        - Some math is easier/quicker to do by hand
    - What kinds of math
        - Elementary algebra
        - Linear (matrix) algebra
        - Linear equations
        - Calculus
        - Big O
        - Probability
        - Bayes' theorem
4. Stats
    - Find order in chaos
    - Explore data
        - Exploratory graphics
        - Exploratory statistics
        - Descriptive statistics
    - Inference
        - Take info about a smaple and infer something about population
        - Hypothesis testing
        - Estimation
    - Concerned with details
        - Feature selection (picking variables)
        - Problems
        - Validation
        - Estimators
5. Machine Learning
    - Categorize & predict
    - Many choices available
    - Insight is the goal (like statistics)

### Goals

Analysis is goal-driven
Story should match goals
Answer clearly

- State the question
- Give your answer
- Qualify as needed
- Go in order
- Discuss process sparingly
- More charts, less text
- Simplify charts
- Avoid tables
- Stories give value to data analysis
- Be minimally sufficient
- Give next steps
- Justify data
- Be specific
- Steps should be doable by the client
- Build on each step
- Data gives correlation, client wants causation
- Presentation graphics need clarity and narrative flow
  - Distractions include:
    - Colors
    - 3D
    - Interaction
    - Animation
- Reproduceable research
  - Archive data sets, both raw and processed
  - Archive all code to process / analyze data
  - Comment liberally
  - Explain why you did it the way you did

### Data

- Store in non-proprietary formats (like CSV)
- Place files in secure, accessible location (Github)
- Use dependency management package
  - Packrat (R)
  - virtualenv (Python)
- Put narrative in notebook, or digital notebook (Jupyter)

datakind.org - volunteer info

## Data Sourcing

Goals and metrics:
Action: Goal is to do something
Explicit: Goals can guide effort
Client: Prevent frustration
Analyst: Use your time well

- Define success
- Define metrics
  - Business metrics (sales revenue, leads generated, etc)
    - KPI's (key performance indicator)
      - Non-financial
      - Timely
      - CEO focus
      - Simple
      - Team based
      - Significant impact
      - Limited dark side (does not reinforce wrong behaviors)
  - SMART
    - Specific
    - Measurable
    - Assignable
    - Realistic
    - Time-bound

- Classification table:

|               | Event Present   | Event Absent    | Total           |
|---------------|-----------------|-----------------|-----------------|
| Test positive | True positives  | False positives | Total positives |
| Test Negative | False negatives | True negatives  | Total negatives |
|               | Total present   | Total absent    | Total           |

### Four kinds of accuracy

- Sensitivity
  - "If there is a fire, does the alarm ring"
  - True positives divided by total alarms
- Specificity
  - "If there isn't a fire, does the alarm stay quiet"
  - True negatives / total absent events
- Positive predictive value
  - If alarm rings, was there a fire?
  - True positives / Total positives
- Negative predictive value
  - If alarm doesn't ring, is there no fire?
  - True negatives / Total negatives

### Existing data

- In house data
  - Data already in the organization
  - Fast and easy
  - May be in appropriate format
  - May have good documentation
- Open data
  - Prepared data that's freely available
  - Government data, corporate data, scientific data
  - <http://data.gov>
    - May also have state level data sources
  - <http://open-data.europa.eu>
  - <http://unicef.org/statistics>
  - <http://who.int/gho>
  - <http://pewinternet.org/datasets>
  - <http://developer.nytimes.com>
  - <http://google.com/publicdata>
  - <http://aws.amazon.com/datasets>
  - Pros: Valuable data sets, wide range of topics, often well formatted and well documented
  - Cons: May be biased samples, meaning may not be clear, may need to share analyses to use, may have privacy issues
- Third party data
  - Proprietary, public, purchased
  - Data-as-a-Service (Daas)
  - Data brokers

### APIs

- Application programming interface
- Lets programs talk to each other
- Allows you to get web data
- REST API
  - Access data on web page via HTTP
  - Usually in JSON format
  - Can send to other programs
  - Language agnostic
- Social APIs (social networks)
- Visual APIs (google maps, youtube, accuweather)

### Scraping data

Formats:

- HTML text
  - Pull structured text from web pages
  - Use HTML tags
- HTML tables
  - HTML table tags
  - If you know the table number, can easily import into Google Sheets
    - =IMPORTHTML(url, "table", tablenumber)
- PDFs
  - Native vs. Scanned
  - Native looks for text elements
  - Can deal with raster/vector images
  - Tabular data
- Media (images/video/audio)
  - Getting images is easy
  - Reading data by looping pixel-by-pixel

Pay attention to copyright and privacy

How:

- Apps
  - import.io
  - ScraperWiki
  - Tabula
  - Google Sheets
  - Excel
- Code
  - R, Python, BASH, Java, PHP

### Making data

- Role?
  - Passive
  - Active
- Q/Q
  - Quantitative (numerical)
  - Qualitative
- How?
  - Online
  - In person
  - Interviews
    - Reasons to do interviews:
      - New topic
      - New audience
      - Need to find ways to improve
      - You don't want to constrain responses
    - Structured
      - Predetermined set of questions; everyone gets same questions
      - Consistent
    - Unstructured
      - More like a conversation
      - Questions come from answers
      - Can be different for each person
    - Interviews can take time (minutes to hour)
    - Interviews usually require specific training
    - Analysis is difficult, searching for themes
    - Can learn things you never expected
  - Surveys
    - Do you know your topic and audience enough to anticipate answers?
    - Types
      - Closed-ended
      - Open-ended
      - In person
      - Online
    - Easy to do
    - Easy to do _badly_
    - Beware the push poll
      - Biased attempt to get data
    - Watch out for bias in question wording, response options, and sample selection
  - Card Sorting
    - Write topics on separate cards
    - Respondents sort the cards
    - From responses can take dissimilarity data
    - Types of tasks
      - Generative
        - Respondents create own sets of cards
        - Used to design a website
      - Evaluative
        - Fixed number/names of categories
        - Can be used to see if website navigation makes sense
    - Dendogram
  - Experiments
    - Laboratory (in person projects)
      - Determine cause & effect
      - Researchers play active role with manipulation
      - Features
        - Focused research
        - Hypothesis Driven
        - Random assignment
          - Can reduce confounds & artifacts
      - Eye tracking in web design
      - Research and medicine
      - Education
      - Psychology
      - Cons
        - Requires extensive training
        - Often time and labor intensive
        - Can be expensive
    - A/B testing (automated variation testing)
      - Pick one element and create multiple versions
      - Randomly assign people to versions
      - Compare response rates
        - Time on page
        - Mouse tracking
        - Click throughs
        - Shopping cart value/abandonment
      - Implement the best version
      - Can perform continuously

## Coding

**80/20 rule**: 80% of output comes from 20% of tools/input

- Applications
  - Spreadsheets
    - Everywhere
    - Often the client's format
    - Often used for data transfers (csv)
    - Easy to use
    - Uses
      - Data browsing
      - Sorting
      - Rearranging
      - Formatting
      - Transposing
      - Tracking changes
      - Making pivot tables
      - Arranging output
    - Tidy data
      - Column == variable
      - Row == case
      - One sheet per file
      - One level per file
  - Tableau
    - Tableau Public is the free version (public.tableau.com)
      - Cannot save files to PC, saves them on the web
      - Not private
    - Visualization tool
  - SPSS
    - Statistical package for social sciences
  - JASP
    - New application ("free SPSS")
- Web Data
- Essentials
  - R
  - Python
  - SQL
- More
  - C, C++, Java
  - Bash
  - Regex

3:15:46
