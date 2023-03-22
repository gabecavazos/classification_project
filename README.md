# classification_project
Goal¶
Identify what causes cx churn for Telco
Use those features to build a model to determine if a customer is likely to churn
Churn is defined as a customer who has left Telco
This information can be useful to help Telco find ways to retain customers who are likely to churn.

# Project Description/planning
- Aquire data
    - get data from sql server
    - chache a csv of data to create an easily repeatable process
- Prep data
    - strip out nulls
    - get column names uniform
    - convert numeric strings to numbers
    - check for duplicates
    - remove 'id's for catagorical features
    - check for nulls
    - removed 11 cx with null total charges
    - encoded churn, removed string version
    - encoded categorical variables
    - split that data up
- Explore data to find correlations and investigate significance
    - initial hypothisis: Age and Gender play a factor in churn
    - initial questions: are payment type, contract type or paperless billing significant?
    - initial thought: scaling will likely influence these outcomes
- Build multiple ml models to predict churn
    - 1 Decision Tree, max depth= 2
    - 2 Decision Tree, no max depth
    - 3 Random Forest
- Test and impliment the best one
    - DT1 had the best preformance
- Give recommendations based on findings



# Data dictionary
              Column Name Data Type              Column Description
0                  gender    object                  male or female
1          senior_citizen     int64           binary for cx over 65
2                 partner    object        y or n if cx has partner
3              dependents    object     y or n if cx has dependents
4                  tenure     int64    months cx has stayed with co
5           phone_service    object  y or n if cx has phone service
6          multiple_lines    object         y n or no phone service
7         online_security    object             y n or no internet 
8           online_backup    object              y n or no internet
9       device_protection    object              y n or no internet
10           tech_support    object              y n or no internet
11           streaming_tv    object              y n or no internet
12       streaming_movies    object              y n or no internet
13      paperless_billing    object    y or n for paperless billing
14        monthly_charges   float64       amount cx charged monthly
15          total_charges   float64         total amount cx charged
16          contract_type    object       m-2-m, one year, two year
17  internet_service_type    object         dsl, fiber, no internet
18           payment_type    object               cx payment method
19          churn_encoded     int64         binary values for churn





# Conclusion
- 73.4% of cx are still with the company!
- Gender does not effect churn
- Age does but this likely due to the majority of cx being under 65, a scaling issue
- cx with month to month contracts churn at higher rates, likely due to the ease of cancelation
- cx paying by electronic check churn at higher rates
- cx with with paperless billing churn more, this is likely due to most cx using paperless billing, a scaling issue
- Using the 1st model we can out perform our current churn estimations by 4.01%, and account for extra revenue of $114,803.39
- The model found cx with under 16.5 months of tenure and without fiber optic internet are the most likely to churn.

# Recommendations
- migrate cx with month to month contracts to yearly
- phase out electronic check payments in favor of credit card by offer a slim discount
- implement model 1 to predict churn and better leverage the expected revenue into retention discounts
- when cx reach 15 months offer a discount to encourage retention
- expand fiber optic service area to capture more cx and improve retention
- provide location data to influence fiber optic expansion planning

# Room for improvement
- focus more on continuous variables like monthly charges
- fix scaling issues
- find and investigate more correlations
- preform more statistical testing to drive correlation testing
- clear code cells from presentable notebook
- run iterative decision tree model building to improve accuracy
- test subsets with hand picked variables



# instructions to reproduce:

- 1 clone this git hub repo
- 2 put your env file in the same location 
- 3 run the cells in report.ipynb top to bottom

