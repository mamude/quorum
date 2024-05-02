# Quorum Coding Challenge

**Server App (Python 3.11)**

```bash
cd server
make install
make run
```

Coverage tests
```bash
make coverage
```


**Frontend App (Node 18.20)**

```bash
cd front
make install
make run
```

# Questions

1. Discuss your strategy and decisions implementing the application. Please, considertime
complexity, effort cost, technologies used and any other variable that you understand
important on your development process.

> As a framework I decided on FastAPI, as I consider it a better designed project for building APIs, and also because it offers great flexibility and freedom to develop your project.
>
> To read CSV files, the Pandas library was selected as it is the most popular in the Python ecosystem.
>
> I believe that I managed to succeed in the implementation even with little experience in using Pandas, my context has always been working with Web applications and not much with Data Science.

2. How would you change your solution to account forfuture columns that might be
requested, such as “Bill Voted On Date” or“Co-Sponsors”?

> Bill Voted On Date:
> It could be added to the vote_results.csv file, example:
>
> ```bash
> id,legislator_id,vote_id,vote_type,voted_on
> 92516784,400440,3321166,2,1714655429.4409034
> ```
>
> Co-sponsors:
> We should have a new data structure, like sponsors.csv
> ```bash 
> id,name
> 1,Rep. Lorem Ipsum
> ```

3. How would you change your solution if instead ofreceiving CSVs of data, you were given a
list of legislators or bills that you should generate a CSV for?

> There could be several options:
> - Receive information via another API
> - Read information from a database
> - Read information from an Excel spreadsheet.

4. How long did you spend working on the assignment?

> I managed to complete it in 4 days, with an average of 6 hours per day.
