# Data Engineer Interview Questions

## Data Modeling: Conceptual vs Logical vs Physical Data Model

(https://online.visual-paradigm.com/knowledge/visual-modeling/conceptual-vs-logical-vs-physical-data-model)

Data modeling is a technique where we document a software system via an entity relationship diagram (ERD). This is a representation of the data structures in use via a table within a company's database.

It is a very powerful and useful tool for the expression of a company's business requirements.

We make use of these for many different purposes: High level conceptual models, logical, and physical models. These are typically represented by the entity-relationship diagram. It serves as a guide used by database analysts and software developers in the design and implementation of a system and the underlying database.

### What is the Entity Relationship Diagram

An entity relationship diagram (ERD) is the pictorial representation of the information that can be captured by a database. This serves two purposes. It will allow database professionals to describe an overall design concisely yet accurately. An ER diagram can also be easily transformed into the relational schema.

There are further more three components in the ERD: Entities, Attributes, and Relationships.

[what-is-erd.png]

### Entities

The number of tables that you will need for your database. Entities is the basic objects of the ERD. These are the tables of your database. A specific example of an entity is called an instance. Each intance becomes a record or a row in a table.

### Attributes

Information such as property, facts you need to describe each table. Attributes are facts or descriptions of entities. They are also often nouns and become the columns of the table. Example: for entity students, the attributes can be first name, last name, email, address, and phone numbers.

-   Primary key is an attribute or a set of attributes that uniquely identifies an instance of the entity. For example, for a student entity, student number is the primary key since no two students have the same idea. We can only have 1 primary key per table, and it cannot be null.
-   Foreign Key is a key used to link two tables together. Typically you take the primary key field from one table and insert it into the other table where it becomes a foreign key (it remaines a primary key in the original table). We can have more than one foreign key in a table.

### Relationships

How tables are linked together. Relationships are the association between these entities. Verbs often describe relationships between entities. We will use Crow's foot symbols to represent the relationships. There are three main types of relationships. If you see the term cardinality rations, it also refers to the types of relationships.

### Cardinality

This defines the possible number of occurences in one entity which is associated with the number of occurences in another. Example of this would be one team has many players. When present in an ERD, the entity team and player are inter-connected with a one-to-many relationship.

In an ER diagram, cardinality is represented as a crow's foot at the conenctor's ends. The three common cardinal relationships are one-to-one, one-to-many, and many-to-many:

[erd-cardinality.png]

### ERD Example - Customer Appointment:

-   One customer may be making one or more appointments.
-   One appointment must be made by one and only one customer.
-   The cardinality linked from customer to appointmnets is 0 to many.

[simple-erd-example.png]

The ERD above uses the Crow's foot  notation:

-   Entities are shown in a box with attributes listed below the entity name.
-   Relationships are shown as Solid Lines between Two Entities.
-   The minimum and maximum cardinalities of the relationship linked between customer and appointment are shown with either a straight line and hash marks, or a crow's foot as shown in the figure below.

### Conceptual, Logical, and Physical data models

Both the conceptual and logical model is used to model the business object that exist in a system, typically by a business analyst. A database designer or database engineer will then elaborate the conceptual and logical ER model to produce the physical model the represents the physical database structure ready for database creation. The below table shows the difference between the three data models.

It is important to remember than an ER model is typically drawn at up to three levels of abstraction:

-   Conceptual ERD / Conceptual Data Model
-   Logical ERD / Logical Data Model
-   Physical ERD / Physical Data Model

While all three of these levels of an ER model contain entities with attributes and relationships, they differ in the purposes they are created for and the audiences they are meant to target:

[purpose-of-erd.PNG]

As can be seen, the characteristics of all three data models are:

-   The conceptual model is to establish the entities, their attributes, and their relationships.
-   The logical data model defines the structure of the data elements and set the relationships between them.
-   The physical data model describes teh database-specific implementation of the data model.

### Conceptual data model

[conceptual-data-model.png]

The conceptual erd models the business objects that should exist in a system and the relationships between them. A conceptual model is developed to present an overall picture of the system by recognizing the business objects involved. It defines which entities exist, not which tables.

The conecptual erd model supports generalization and the `a kind of` relationship, such as a dog is a kind of animal.

### Logical data model

Logical ERD is a detailed version of a Conceptual ERD. A logical ER model is developed to enrich a conceptual model by defining explicitly the columns in each entity and introducing operational and transactional entities. Although a logical data model is still independent of the actual database system in which the database will be created, you can still consider that if it affects the design.

[logical-er-model-1.png]

### Physical Data Model

Physical ERD represents the actual design blueprint of a relational database. A physical data model elaborates on the logical data model by assigning each column with type, length, nullable, etc. Since a physical ERD represents how data should be structured and related in a specific DBMS it is important to consider the convention and restriction of the actual database system in which the database will be created. Make sure the column types are supported by the DBMS and reserved words are not used in naming entites and columns.

[physical-er-model-1.png]

## Database Normalization

(https://en.wikipedia.org/wiki/Database_normalization)

Database normalization is the process of structuring a relational database in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity.

Normalization entails organizing the columns (attributes) and tables (relations) of a database to ensure that their dependencies are properly enforced by database integrity constraints. It is accomplished by applying some formal rules either by a process of synthesis (creating a new database design) or decomposition (improving an existing database design).

### Objectives

A basic objective of the first normal form defined by Codd in 1970 was to permit data to be queried and manipulated using a "universal data sublanguage" grounded in first-order logic. An example of such being sql, though Codd considered sql flawed.

The objectives of normalization beyond 1NF (first normal form) were stated by Codd as:

1.  To free the collection of relations from undesirable insertion, update, and deletion dependencies.
2.  To reduce the need for restructuring the collection of relations, as new types of data are introduced, and thus increase the life span of application programs.
3.  To make the relational model more informative to users.
4.  To make the collection of relations neutral to the query statistics, where these statistics are liable to change as time goes by.

When an attempt is made to modify (update, insert into, or delete from) a relation, the following undersirable side effects may arise in relations that have not been sufficiently normalized:

### Insertion Anomaly

There are circumstances in which certain facts cannot be recorded at all. For example, each record in a "faculty and their courses" relation might contain a faculty id, faculty name, faculty hire date, and course code. Therefore the details of any faculty member who teaches at least one course can be recorded, but a newly hired member who has not yet been assigned to teach any courses cannot be recorded, except by setting the course code to null.

[280px-Insertion_anomaly.svg.png]

### Update Anomaly

The same information can be expressed on multiple rows; therefore updates to the relation may result in logical inconsistencies. For example, each record in an "Employees Skills" relation might contain an Employee ID, Employee Address, and Skill; Thus a change of address for a particular employee may need to be applied to multiple records (one for each skill). If the update is only partially successful - the employee's address is updated on some records but not others - then the relation is left in an inconsistent state. Specifically, the relation provides conflicting answers to the question of what this particular employee's address is.

[280px-Update_anomaly.svg.png]

### Deletion anaomaly

Under certain circumstances, the deletion of data representing certain facts necessitates the deletion of data representing completely different facts. The "Faculty and their courses" relation described in the previous example suffers from this type of anomaly, for if a faculty member temporarily ceases to be assigned any courses, the last of the records on which that faculty member appears must be deleted, effectively also deleting the faculty member, unless the cource code is set to null.

[280px-Deletion_anomaly.svg.png]

### Minimize redesign when extending the database structure

A fully normalized database allows its structure to be extended to accomodate new types of data without changing existing structure too much. As a result, applications interacting with the database are minimally affected.

Normalized relations, and the relationship between one normalized relation and another, mirror real-worl concepts and their interrelationships.

## What is the difference between ETL and ELT

(https://aws.amazon.com/compare/the-difference-between-etl-and-elt/#:~:text=ELT%20is%20faster%20than%20ETL,and%20transforms%20it%20in%20parallel.)

Both Extract, Transform, and Load (ETL) and Extract, Load, Transform (ELT) are tow data-processing approaches for analytics. Large organizations have several hundred (or even thousands) of data sources from all aspects of their operations - like applications, sensors, IT infrastructure, and third-party partners. They have to filter, sort, and clean this large data volume to make it useful for analytics and business intelligence. The ETL approach uses a set of business rules to process data from several sources before centralized integration. The ELT approach loads data as it is and transforms it at a later stage, depending on the use case and analytics requirements. The ETL process requires more definition at the beginning. Analytics must be involved from the start to define target data types, structures, and their relationships. Data scientists mainly use ETL to load legacy databases in the data warehouse, while ELT has become the norm today.

### What are the similarities between ETL and ELT

Both ETL and ELT are sequences of processes that prepare data for further analysis. They capture, process, and load data for analysis across three steps.

### Extraction

Extraction is the first step of both ETL and ELT. This step is about colelcting raw data from different sources. These could be databases, files, software as a service (SaaS) applications, Internet of Things (IOT) sensors, or application events. You can collect semi-structured, structured, or unstructured data at this stage.

### Transformation

In the ETL process, tranformation is the second step, while in ELT it is the third. This step focuses on changing raw data from its original structure into a format that meets the requirements of the target system where you plan to store the data for analytics. Here are some examples of transformations.

-   Changing data types or formats.
-   Removing inconsistent or inaccurate data.
-   Removing data duplication.

You apply rules and functions to clean and prepare data for analysis in the target system.

### Load

In this phase, you store data into the target database. ETL processes load data as a final step, so that reporting tools can use it directly to generate actionable reports and insights. However, in ELT, you still need to transform the extracted data after loading it.

### How do the ELT and ETL processes differ from each other?

The ETL process has three steps:

1.  You extract raw data from various sources.
2.  You use a secondary processing server to transform that data.
3.  You load that data into a target database.

The transformation stage ensures compliance with the target database's structural requirements. You only move the data once it is transformed and ready.

[ETLandELTRedshift1.png]

The ELT process also has three steps:

1.  You extract raw data from various sources.
2.  You load it in its natural state into a data warehouse or data lake.
3.  You transform it as needed while in the target system.

With ELT, all data cleansing, transformation, and enrichment occur within the data warehouse. You can interact with and transform the raw data as many times as needed.

### History of ETL and ELT

ETL has been around size the 1970s, becoming especially popular with the rise of data warehouses. However, traditional data warehouses required custom ETL processes for each data source.

The evolution of cloud technologies changed what was possible. Companies could now store unlimited raw data as scale and analyze it later as required. ETL became the modern data integration method for efficient analytics.

### Key difference: ETL vs ELT

Extract, load, and transform (ELT) has improved extract, transform, and load (ETL) in several ways.

### Transform and Load location

Transformation and load occur in different locations and use distinct processes. The ETL process transforms data on a secondary processing server.

In contrast, the ELT process loads raw data directily into the target data warehouse. Once there, you can transform the data whenever you need it.

### Data Compatibility

ETL is best suited for structured data that you can represent in tables with rows and columns. It transforms one set of structured data into another structured format and then loads it.

In contrast, ELT handles all types of data, including unstructured data like images or documents that you can't store in tabular format. WIth ELT, the process loads the various data formats into the target data warehouse. From there, you can transform it further into the format you require.

### Speed

ELT is faster than ETL. ETL has an additional step before it loads data into the target that is difficult to scale and slows the system down as data size increases.

In contrast, ELT loads data directly into the destination system and transforms it in parallel. It uses the processing power and parallelization that cloud data warehouses offer to deliver real-time or near real-time data transformation for analytics.

### Costs

The ETL process requires analytics involvement from the start. It needs analysts to plan ahead on the reports they want to generate and define data structures and formatiing. The time required for setup increases, which adds to costs. Additional server infrastructure for transformations may also cost more.

ELT has fewer systems than ETL, as all transformations occur within the target data warehouse. With fewer systems, there is less to maintain, leading to a simpler data stack and lower setup costs.

### Security

When you work with personal data, you must comply with data privacy regulations. Companies must protect personally identifiable information (PII) from unauthorized access.

In ETL, developers have to build custom solutions, like masking PII to monitor and protect data.

On the other hand, ELT solutions provide many security features - like granular access control and multifactor authentication - directly within the data warehouse. You can invenst more time in analytics and less time meeting data regulation requirements.

### When to use ETL vs. ELT

Extract, load, and transform (ELT) is the standard choice for modern analytics. However, you might consider extract, transform, and load (ETL) in the following scenarios:

### Legacy Databases

It is sometimes more beneficial to use ETL to integrate with legacy databases or third-party data sources with predetermined data formats. You only have to transform and load it once into your system. Once transformed, you can use it more efficiently for all future analytics.

### Experimentation

In large organizations, data engineers conduct experiments - things like discovering hidden data sources for analytics and trying out new ideas to answer business queries. ETL is useufl in data experiments to understand the database and its usefulness in a particular scenario.

### Complex analytics

ETL and ELT may both be used together for complex analytics that use multiple data formats from varied sources. Data scientists may set up ETL pipelines from some of the sources and use ELT with the rest. This improves analytics efficiency and increases application performance in some cases.

## What is ETL (Extract Transform Load)

(https://aws.amazon.com/what-is/etl/)

ETL is the process of combining data from multiple sources into a large, central repository called a data warehouse. ETL uses a set of business rules to clean and organize raw data and prepare it for storage, data analytics, and machine learning (ML). You can address specific business intelligence needs through data analytics (such as predicting the outcome of business decisions, generating reports and dashboards, reducing operational inefficiency, and more).

### Why is ETL important

Organizations today have both structured and unstructured data from various sources including:

-   Customer data from online payment and customer relationship management (CRM) systems.
-   Inventory and operations data from vendor systems.
-   Sensor data from IOT devices
-   Marketing data from social media and customer feedback.
-   Employee data from internal human resources systems.

By applying the process of extract, transform, and load (ETL), individual raw datasets can be prepared in a format and structure that is more consumable for analytics purposes, resulting in more meaningful insights. For example, online retailers can analyze data from points of sale to forecast demand and manage inventory. Marketing teams can integrate CRM data with customer feedback on social media to study consumer behavior.

### How does ETL benefit business intelligence?

ETL improves business intelligence and analytics by making the process more reliable, accurate, detailed, and efficient.

### Historical Context

ETL gives deep historical context to the organizations data. An enterprise can combine legacy data with data from new platforms and applications. You can view older datasets alongside more recent information, which gives you a long-term view of data.

### Consolidated Data View

ETL provides a consolidated view of data for in-depth analysis and reporting. Managing multiple datasets demends time and coordination and can result in inefficiencies and delays. ETL combines databases and various forms of data into a single unified view. The data integration process improves the data quality and saves time required to move, categorize, or standardize data. This makes it easier to analyze, visualize, and make sense of large datasets.

### Accurate data analysis

ETL gives more accurate data analysis to meet compliance and regulatory standards. You can integrate ETL tools with data quality tools to profile, audit, and clean data, ensuring that the data is trustworthy.

### Task Automation

ETL automates repeatable data processing tasks for efficient analysis. ETL tools automate the data migration process, and you can set them up to integrate data changes periodically or even at runtime. As a result, data engineers can spend mroe time innovating and less time managing tedious tasks like moving and formatting data.

### How has ETL evolved

Extract, transform, and load (ETL) originated with the emergence of relational databases that stored data in the form of tables for analysis. Early ETL tools attempted to convert data from transactional data formats to relational data formats for analysis.

### Traditional ETL

Raw data was typically stored in transactional databases that supported many read and write requests but did not lend well to analytics. You can think of it as a row in a spreadsheet. For example, in an ecommerce system, the transactional database stored the purchased item, customer details, and order details in one transaction. Over the year, it contained a long list of transactions with repeat entries for the same customer who purchased multiple items during the year. Given the data duplication, it became cumbersome to analyze the most popular items or purchase trends in that year.

To overcome this issue, ETL tools automatically converted this transactional data into relational data with interconnected tables. Analysts could use queries to identify relationships between the tables, in addition to patterns and trends.

### Modern ETL

As ETL technology evolved, both data types and data sources increased exponentially. Cloud technology emerged to create vast databases (also called data sinks). Such data sinks can receive data from multiple sources and have underlying hardware resources that can scale over time. ETL tools have also become more sophisticated and can work with modern data sinks. They can convert data from legacy data formats to modern data formats. Examples of modern databases follow.

### Data Warehouses

A data warehouse is a central repository that can store multiple databases. Within each database, you can organize your data into tables and columns that describe the data types in the table. The data warehouse software works across multiple types of storage hardware - such as solid state drives, hard drives, and other cloud storage - to optimize your data processing.

### Data Lakes

With a data lake, you can store your structured and unstructured data in one centralized repository and at any scale. You can store data as is wihtout having to first structure it based on questions you might have in the future. Data lakes also allow you to run different types of analytics on your data, like SQL queries, big data analytics, full-tet-search, real time analytics, and machine learning ML to guide better decisions.

### How does ETL work

Extract, transform, and load (ETL) works by moving data from the source system to the destination system at periodic intervals. The ETL process works in three steps:

1.  Extract the relevant data from the source database
2.  Transform the data so that it is better suited for analytics
3.  Load the data into the target database

[Fig1-etljob.feff8a73afe5fbbdb8ebb2f8255c1147deda6106.png]

### What is data extraction

In data extraction, etl tools extract or copy raw data from multiple sources and store it in a staging area. A staging area (or landing zone) is an intermediate storage area for temporarily storing extracted data. Data staging areas are often transient, meaning their contents are erased after data extraction is complete. However, the staging area might also retain a data archive for troubleshooting purposes.

How frequently the system sends data from the data source to the target data store depends on the underlying change data capture mechanism. Data extraction commonly happens in one of the three following ways:

### Update Notification

In update notification, the source system notifies you when a data record changes. You can then run the extraction process for that change. Most databases and web applications provide update mechanisms to support this data integration method.

### Incremental extraction

Some data sources can't provide update notifications, but can identify and extract data that has been modified over a given time period. In this case, the system checks for changes at periodic intervals, such as once a week, once a month, or at the end of a campaign. You only need to extract data that has changed.

### Full extraction

Some systems can't identify data changes or give notifications, so reloading all data is the only option. This extraction method requires you to keep a copy of the last extract to check which records are new. Because this approach involves high data transfer volumes, we recommend you use it only for small tables.

### What is data transformation

In data transformation, ETL tools transform and consolidate the raw data in the staging area to prepare it for the target data warehouse. The data transformation phase can involve teh following types of data changes:

### Basic data transformation

Basic tranformations improve data quality by removing errors, emptying data fields, or simplifying data. Examples of these transformations follow:

-   Data Cleansing
    -   Data cleansing removes errors and maps source data to the target data format. For example, you can map empty data fields to the number 0, map the data value "Parent" to "P", or map "Child" to "C".
-   Data deduplication
    -   Deduplication in data cleansing identifies and removes duplicate records.
-   Data format revision
    -   Format revision converts data, such as character sets, measurement units, and date/time values, into a consistent format. For example, a food company might have different recipe databased with ingredients measured in kilograms and pounds. ETL will convert everything to pounds.

### Advanced data transformation

Advanced transformations use business rules to optimize the data for easier analysis. Examples of these transformations follow:

-   Derivation
    -   Derivation applies business rules to your data to calculate new values from existing values. For example, you can convert revenue to profit by subtracting expenses or calculating the total cost of a purchase my multiplying the price of each item by the number of orders.
-   Joining
    -   In data preparation, joining links the same data from different data sources. For example you can find the total purchase cost of one item by adding the purchase value from different vendors and storing only the final total in the target system.
-   Splitting
    -   You can divide a column or data attribute into multiple columns in the target system. For example, if the data source saves the customer name as "Jane John Doe", you can splt it into First, Middle, and Last Name.
-   Summarization
    -   Summarization improves data quality by reducing a large number of data values into a smaller dataset. For example, customer order invoice values can have many different small amounts. You can summarize the data by adding them up over a given period to build a customer lifetime value (CLV) metric.
-   Encryption
    -   You can protect sensitive data to comply with data laws or data privary by adding encryption before the data streams to the target database.

### What is data loading

In data loading, etl tools move the transformed data from the staging area into the target data warehouse. For most organizations that use etl, the process is automated, well defined, continual, and batch driven. Two methods for loading data follow.

### Full Load

In full load, the entire data from the source is transformed and moved to the data warehouse. The full load usually takes place the first time you load data from a source system into the data warehouse.

### Incremental load

In incremental load, the ETL tool loads the delta between target and source systems at regular intervals. It stores the last extract date so that only records added after this date are loaded. There are two ways to implement incremental load.

### Streaming incremental load

If you have small data volumes, you can stream continual changes over data pipelines to the target data warehouse. When the speed of data increases to millions of events per second, you can use even stream processing to monitor and process the data streams to make more-timely decisions.

### Batch Incremental Load

If you have large data volumes, you can colelct load data changes into batches periodically. During this set period of time, no actions can happen to either the source or taget system as data is synchronized.

### What is ELT

ELT is an extension of ETL that reverses the order of operations. You can load data directly into the target system before processing it. The intermediate staging area is not required because the target data warehous has data mapping capabilities within it. ELT has become more populare with the adoption of cloud infrastructure, which gives target databases the processing power they need for transformations.

### ETL compared to ELT

ELT works well for high-volume, unstrcutured datasets that require frequent loading. It is also ideal for big data because the planning for analytics can be done after the data extraction and storage. It leaves the bulk of transformations for the analytics stage and focuses on loading minimally processed raw data into the data warehouse.

The ETL process requires more definition at the beginning. Analytics needs to be involved from the start to define target data types, structures, and relationships. Data scientists mainly use ETL to load legacy databases into the warehouse, and ELT has become the norm today.

### What is data virtualization

Data virtualization uses a software abstraction layer to create an integrated data view without physically extracting, transforming, or loading the data. Organizations use this functionality as a virtual unified data repository without the expense and complexity of building and managing separate platforms for source and target. While you can use data virtualization alongside etl, it is increasingly seen as an alternative to ETL and other physical data integration methods.

## Difference Between ELT and ETL

(https://www.geeksforgeeks.org/difference-between-elt-and-etl/)

The differences between ELT and ETL can be brought into the following:

|ELT|ETL|
|---|---|
|ELT tools do not require additional hardware|ETL tools requires specific hardware with their own engines to perform transformations.|
|Mostly Hadoop or NoSql database to store data. Rarely RDBMS is used|RDBMS is used exclusively to store data.|
|As all components are in one system, loading is done only once|As ETL uses staging area, extra time is required to load the data.|
|Time to transform data is independent of the size of data|The system has to wait for large sizes of data. As the size of data increases, transformation time also increases.|
|It is cost effective and available to all business using SaaS solution|Not cost effective for small and medium business|
|The data transformed is used by data scientists and advanced analysts|The data transformed is used by users reading report and sql coders.|
|Creates ad hoc views. Low cost for building and maintaining|Views are created based on multiple scripts. Deleting view means deleting data.|
|Best for unstructured and non-relational data. Ideal for data lakes. Suited for very large amounts of data.|Best for relational and structured data. Better for small to medium amounts of data.|

## Star Schema

(https://www.databricks.com/glossary/star-schema#:~:text=A%20star%20schema%20is%20used,like%20transaction%20amounts%20and%20quantities).)

### What is a star schema

A star schema is a multi-dimensional data model used to organize data in a database so that it is easy to understand and analyze. Star schemas can be applied to data warehouses, databases, data marts, and other tools. The star schema design is optimized for querying large data sets.

Introduced by Ralph Kimball in the 1990s, star schemas are efficient at storing data, maintaining history, and updating data by reducing the duplication of repetitive business definitions, making it fast to aggregate and filter data in the data warehouse.

[star-schema-erd.png]

### Fact tables and dimension tables

A star schema is used to denormalize business data into dimensions (like time and product) and facts (like transactions in amounts and qunatities).

A star schema has a single fact table in the center, containing buisness "facts" (like transaction amounts and quantities). The fact table connects to multiple other dimension tables along dimensions like time or product. Star schemas enable users to slice and dice the data however they see fit, typically by joinging two or more fact tables and dimension tables together.

### Denormalized data

Star Schemas denormalize the data, which means adding redundant columns to some dimension tables to make querying and working with the data faster and easier. The purpose is to trade some redundancy (duplication of data) in the data model for increased query speed, by avoiding computationally expensive join operations.

In this model, the fact table is normalized but the dimensions tables are not. That is, data from the fact table exists only on the fact table, but dimensional tables may hold redundant data.

### Benefits of star schemas

-   Fact/Dimensional models like star schemas are simple to understand and implement, and make it easy for end users to find the data they need. They can be applies to data marts and other data resources.
-   Greate for simple queries because of their reduced dependency on joins when accessing the data, as compared to normalized models like snowflake schemas.
-   Adapt well to fit OLAP models.
-   Improved query performance as compared to normalized data, because star schemas attempt to avoid computationally expensive joins.

### How does a star schema differ from 3NF (Third Normal Form)

3NF, or Third Normal Form, is a method of reducing data-redundancy through normalization. It is a common standard for databases that are considered fully normalized. It typically has more tables than a star schema due to data normalization. On the flip-side, querier tend to be more complex due to the increased number of joins between large tables.

## Difference between fact table and dimension table

(https://stackoverflow.com/questions/20036905/difference-between-fact-table-and-dimension-table)

In data warehouse modeling, a star schema and a snowflake schema constists of Fact and Dimension tables.

### Fact Table:

-   It contains all the primary keys of the dimension and associated facts or measures (is a property on which calculations can be made) like quantity sold, amount sold, and average sales.

### Dimension Tables

-   Dimension tables provides descriptive information for all the measurements recorded in fact table.
-   Dimensions are relatively very small as comparison of fact table.
-   Commonly used dimensions are people, products, place, and time.

[aB9k9.jpg]

## Database Normalization vs. Denormalization

(https://medium.com/analytics-vidhya/database-normalization-vs-denormalization-a42d211dd891)

Database normalization is the proceass of structuring a relational database in accordance with a series of so-called normal forms to reduce data redundancy and improve data integrity.

In the database design scope, Normalization is a database design technique that organizes tables in a manner that reduces redundancy and dependency of data by minimizing the insertion, deletion, and update anomalies through eliminating the redundant data. Using  the Normalization technique to design databases causes us to divide larger tables into smaller tables and links them using relationships. The purpose of Normalization is to eliminate redundant (useless) data and ensure data is stored logically.

[1_QzI6M9zSMG33SUm4eg8u8Q.png]

At the opposite, Denormalization is the inverse process of normalization where the redundancy is added to the data intentionally to improve the performance of the specific application and data integrity. The reason for performing denormalization is the overheads produced in the query processor by an over-normalized structure. Denormalization reduces the number of tables, and the complicated table joins because a higher number of joins can slow down the process.

[1_FNMp1Ntu7P44bdPtIVZI6g.png]

### Key Differences Between Normalization and Denormalization

Both the Normalized and Denormalized techniques have their own benefits and drawbacks. The following table compared these two techniques in a short but understandable way.

|-|Normalization|Denormalization|
|--|--|--|
|Basic|Normalization is the process of creating a set schema to store non-redundant and consistent data.|Denormalization is the process of combining the data so that it can be queried speedily.|
|Purpose|To reduce the data redundancy and inconsistency|To achieve the faster execution of the queries through introducing redundancy.|
|Used In|OLTP system, where the emphasize is on making the insert, delete, and update anomalies faster and storing the quality data|OLAP system, where the emphasis is on making the search and analysis faster.|
|Data Integrity|Maintained|May not retain|
|Redundancy|Eliminated|Added|
|Number of Tables|Increases|Decreases|
|Disk Space|Optimized usage|wastage|

1.  Normalization is the technique of dividing the data into multiple tables to reduce data redundancy and inconsistency and to achieve data integrity. On the other hand, Denormalization is the technique of combining the data into a single table to make data retrieval faster.
2.  Normalization is used in an OLTP system, which emphasizes making the insert, delete, and update anomalies faster. As the opposite, Denormalization is used in an OLAP system, which emphasizes making the search and analysis faster.
3.  Data Integrity is maintained in the normalization process while in denormalization data integrity harder to retain.
4.  Redundant data is eliminated when normalization is performed whereas denormalization increases the redundant data.
5.  Normalization increases the number of tables and joins. In constrast, denormalization reduces the number of tables and joins.
6.  Disk space is wasted in denormalization because the same data is stored in different places. On the contrary, disk space is optimized in a normalized table.

## Snowflake Schema

(https://www.databricks.com/glossary/snowflake-schema)

### What is a snowflake schema

A snowflake schema is a multi-dimensional data model that is an extension of a star schema, where dimension tables are broken down into subdimensions. SNOWFLAKE schemas are commonly used for business intelligence and reporting in OLAP data warehouses, data marts, and relational databases.

In a snowflake schema, engineers break down individual dimension tables into logical subdimensions. THIS makes the data model more complex, but it can be easier for analysts to work with, especially for certain data types.

It is called a snowflake schema because it's ERD (entity-relationship diagram) looks like a snowflake as seen below:

[snowflake-schema-120723_0.png]

### Snowflake schemas vs. star schemas

Like star schemas, snowflake schemas have a central fact table which is connected to multiple dimension tables via foreign keys. However, the main difference is taht they are more normalized than star schemas.

Snowflake schemas offer more storage efficiency, due to their tighter adherence to high normalization standards, but query performance is not as good as with more denormalized data models. Denormalized data models like star schemas have more data redundancy (duplication of data), which makes query performance faster at the cost of duplicated data.

### Benefits of snowflake schemas

-   Fast data retrieval
-   Enforces data quality
-   Simple, common data model for data warehousing

### Drawbacks if snowflake schemas

-   Lots of overhead upon initial setup
-   Rigid data model
-   High maintenance costs

## What is OLAP (Online Analytical Processing)

(https://aws.amazon.com/what-is/olap/#:~:text=Online%20analytical%20processing%20(OLAP)%20is,smart%20meters%2C%20and%20internal%20systems.)

### What is online analytical processing

Online analytical processing (OLAP) is software technology you can use to analyze business data from different points of view. Organizations collect and store data from multiple data sources, such as websites, applications, smart meters, and internal systems. OLAP combines and groups this data into categories to provide actionable insights for strategic planning. For example, a retailer stores data about all the products it sells, such as color, size, cost, and location. The retailer also collects customer purchase data, such as the name of the items ordered and total sales value, in a different system. OLAP combines the datasets to answer questions such as which color products are mor popular or how product placement impact sales.

### Why is OLAP important

Online analytical processing (OLAP) helps organizations process and benefit from a growing amount of digital information. Some benefits of OLAP include the following.

### Faster decision making

Business use OLAP to make quick and accurate decisions to remain competitive in a fast-paced economy. Performing analytical queries on multiple relational databases is time consuming because the computer system searches through multiple data tables. On the other hand, OLAP systems precalculate and integrate data so business analysts can generate reports faster when needed.

### Non-technical user support

OLAP systems make complex data analysis easier for non-technical business users. Business users can create complex analytical calculations and generate reports instead of learning hot to operate databases.

### Integrated data view

OLAP provides a unified platform for marketing, finance, production, and other business units. Managers and decision makers can see the bigger picture and effectively solve problems. THey can perform what-if analysis, which shows the impact of decisions taken by on department on other areas of the business.

### What is OLAP architecture

Online analytical processing (OLAP) systems store multidimensional data by representing information in more than two dimensions, or categories. Two-dimensional data involves columns and rows, but multidimensional data has multiple characteristics. For example, multidimensional data for product sales might consist of the following dimensions:

-   Product type
-   Location
-   Time

Data engineers build a multidimensional OLAP system that consists of the following elements:

### Data Warehouse

A data warehouse collects information from different sources, including applications, files, and databases. It processes the information using various tools so that the data is ready for analytical purposes. For example, the data warehouse might collect information from a relational database that stores data in tables of rows and columns.

### ETL Tools

ETL tools are database processes that automatically retrieve, change, and prepare the data to a format fit for analytical purposes. Data warehouses use ETL to convert and standardize information from various sources before making it available to OLAP tools.

### OLAP Server

An OLAP server is the underlying machine that powers the OLAP system. It uses ETL tools to transform information in the relational databases and prepare them for OLAP operations.

### OLAP database

An olap database is a separate database taht connects to the data warehouse. Data engineers sometimes use an olap database to prevent the data warehouse from being burdened by OLAP analysis. They also use an OLAP database to make it easier to create OLAP data models.

### OLAP Cubes

A data cube is a model representing a multidimensional array of information. While it's easier to visualize is as a three-dimensional data model, most data cubes have more than three dimensions. An OLAP cube, or hyper cube, is the term for data cubes in an OLAP system. OLAP cubes are rigid becauses you can't change the dimensions and underlying data once you model it. For example, if you add the warehouse dimension to a cube with product, location, and time dimensions, you have to remodel the entire cube.

### OLAP analytic tools

Business analysts use OLAP tools to interact with the OLAP cube. They perform operations such as slicing, dicing, and pivoting to gain deeper insights into specific information within the OLAP cube.

### How does OLAP worl

An online analytical processing system works by colleecting organizing, aggregating, and analyzing data using the following steps:

1.  The OLAP server collects data from multiple data sources, including relational databases and data warehouses.
2.  Then, the ETL tools clean, aggregate, precalculate, and store data in an OLAP cube according to the number of dimensions specified.
3.  Business analysts use OLAP tools to query and generate reports from the multidimensional data in the OLAP cube.

OLAP uses multidimensional expressions (MDX) to query the OLAP cube. MDX is a query, like SQL, that provides a set of instructions for manipulating databases.

### What are the types of OLAP

OLAP operates in three ways:

### MOLAP

Multidimensional online analytical processing involves creating a data cube that represents multidimensional data from a data warehouse. The molap system stores precalculated data in the hypercube. Data engineers use MOLAP because this type of OLAP technology provides fast analysis.

### ROLAP

Instead of using a data cube, relational online analyical processing allows data engineers to perform multidimensional data analysis on a relational database. In other words, data engineers use SQL queries to search for and retrieve specific information based on the required dimensions. ROLAP is suitable for analyzing extensive and detailed data. However, ROLAP has slow query performance compared to MOLAP.

### HOLAP

Hybrid online analytical processing combines MOLAP and ROLAP to provide the best of both architectures. HOLAP allows data engieers to quickly retireve analytical results from a data cube and extract detailed information from relational databases.

### What is data modeling in OLAP

Data modeling is the representation of data in data warehouses or online analytical processing (OLAP) databases. Data modeling is essential in relational online analytical processing (ROLAP) because it analyzes data straight from the relational database. It stores multidimensional data as a star or snowflake schema. 

### What are OLAP operations

Business analysts perform several basic analytical operations with a multidimensional online analytical processing (MOLAP) cube.

### Roll Up

In roll up, the online analytical processing (OLAP) system summarizes the data for specific attributes. In other words, it shows less-detailed data. For example, you might view product sales according to New York, California, London, and Tokyo. A roll-up operation would provide a view of the sales data based on countries, such as the US, the UK, and Japan. 

### Drill Down

Drill down is the opposite of the roll-up operation. Business analysts move downward in the concept hierarchy and extract the details they require. For example, they can move from viewing sales data by years to visualizing it by months.

### Slice

Data engineers use the slice operation to create a two-dimensional view from the OLAP cube. For example, a MOLAP cube sorts data according to products, cities, and months. By slicing the cube, data engineers can create a spreadsheet-like table consisting of products and cities for a specific month. 

### Dice

Data engineers use the dice operation to create a smaller subcube from an OLAP cube. They determine the required dimensions and build a smaller cube from the original hypercube.

### Pivot

The pivot operation involves rotating the OLAP cube along one of its dimensions to get a different perspective on the multidimensional data model. For example, a three-dimensional OLAP cube has the following dimensions on the respective axes:

-   X-axis—product 
-   Y-axis—location
-   Z-axis—time

Upon a pivot, the OLAP cube has the following configuration:

-   X-axis—location
-   Y-axis—time
-   Z-axis—product

### How does OLAP compare with other data analytics methods

### Data Mining

Data mining is analytics technology that processes large volumes of historical data to find patterns and insights. Business analysts use data-mining tools to discover relationships within the data and make accurate predictions of future trends.

OLAP and data mining
Online analytical processing (OLAP) is a database analysis technology that involves querying, extracting, and studying summarized data. On the other hand, data mining involves looking deeply into unprocessed information. For example, marketers could use data-mining tools to analyze user behaviors from records of every website visit. They might then use OLAP software to inspect those behaviors from various angles, such as duration, device, country, language, and browser type. 

### OLTP

Online transaction processing (OLTP) is a data technology that stores information quickly and reliably in a database. Data engineers use OLTP tools to store transactional data, such as financial records, service subscriptions, and customer feedback, in a relational database. OLTP systems involve creating, updating, and deleting records in relational tables. 

OLAP and OLTP
OLTP is great for handling and storing multiple streams of transactions in databases. However, it cannot perform complex queries from the database. Therefore, business analysts use an OLAP system to analyze multidimensional data. For example, data scientists connect an OLTP database to a cloud-based OLAP cube to perform compute-intensive queries on historical data.

## OLAP (online analytical processing)

(https://www.techtarget.com/searchdatamanagement/definition/OLAP)

### What is OLAP

OLAP (online analytical processing) is a computing method that enables users to easily and selectively extract and query data in order to analyze it from different points of view. OLAP business intelligence queries often aid in trends analysis, financial reporting, sales forecasting, budgeting and other planning purposes.

For example, a user can request data analysis to display a spreadsheet showing all of a company's beach ball products sold in Florida in the month of July. They can compare revenue figures with those for the same products in September and then see a comparison of other product sales in Florida in the same time period.

### How OLAP systems work

To facilitate this kind of analysis, data is collected from multiple sources and stored in data warehouses, then cleansed and organized into data cubes. Each OLAP cube contains data categorized by dimensions (such as customers, geographic sales region and time period) derived by dimensional tables in the data warehouses. Dimensions are then populated by members (such as customer names, countries and months) that are organized hierarchically. OLAP cubes are often pre-summarized across dimensions to drastically improve query time over relational databases.

Analysts can then perform five types of OLAP analytical operations against these multidimensional databases:

-   Roll-up. Also known as consolidation, or drill-up, this operation summarizes the data along the dimension.
-   Drill-down. This allows analysts to navigate deeper among the dimensions of data. For example, drilling down from "time period" to "years" and "months" to chart sales growth for a product.
-   Slice. This enables an analyst to take one level of information for display, such as "sales in 2017."
-   Dice. This allows an analyst to select data from multiple dimensions to analyze, such as "sales of blue beach balls in Iowa in 2017."
-   Pivot. Analysts can gain a new view of data by rotating the data axes of the cube.

OLAP software locates the intersection of dimensions, such as all products sold in the Eastern region above a certain price during a certain time period, and displays them. The result is the measure; each OLAP cube has at least one to perhaps hundreds of measures, which derive from information stored in fact tables in the data warehouse.

[crm-olap.png]

### OLTP vs. OLAP

OLAP focuses on data analysis to generate business insights, whereas online transactional processing (OLTP) focuses on real-time processing of online transactions. OLTP is used for executing online database transactions that frontline workers such as cashiers and bank tellers generate. Customer self-service applications such as online banking, travel and e-commerce also generate database transactions and tie into OLTP systems. OLTP can be a data source for OLAP systems.

[whatis-oltp_vs_olap.png]

### Uses of OLAP

OLAP can be used for data mining or the discovery of previously undiscerned relationships between data items. An OLAP database does not need to be as large as a data warehouse, since not all transactional data is needed for trend analysis. Using Open Database Connectivity, data can be imported from existing relational databases to create a multidimensional database for OLAP.

OLAP products include IBM Cognos, Microsoft Power BI, Oracle OLAP and Tableau. OLAP features are also included in tools such as Microsoft Excel and Microsoft SQL Server's Analysis Services. OLAP products are typically designed for multiple-user environments, with the cost of the software based on the number of users.

## What is OLTP

(https://www.oracle.com/database/what-is-oltp/#:~:text=What%20is%20OLTP%3F-,OLTP%20defined,sending%20text%20messages%2C%20for%20example.)

OLTP or Online Transaction Processing is a type of data processing that consists of executing a number of transactions occurring concurrently—online banking, shopping, order entry, or sending text messages, for example. These transactions traditionally are referred to as economic or financial transactions, recorded and secured so that an enterprise can access the information anytime for accounting or reporting purposes.

In the past, OLTP was limited to real-world interactions in which something was exchanged–money, products, information, request for services, and so on. But the definition of transaction in this context has expanded over the years, especially since the advent of the internet, to encompass any kind of digital interaction or engagement with a business that can be triggered from anywhere in the world and via any web-connected sensor. It also includes any kind of interaction or action such as downloading pdfs on a web page, viewing a specific video, or automatic maintenance triggers or comments on social channels that maybe critical for a business to record to serve their customers better.

The primary definition for transactions—economic or financial—remains the foundation for most OLTP systems, so online transaction processing typically involves inserting, updating, and/or deleting small amounts of data in a data store to collect, manage, and secure those transactions. Typically a web, mobile, or enterprise application tracks all those interactions or transactions with customers, suppliers, or partners and updates them in the OLTP database. This transaction data stored in the database is critical for businesses and used for reporting or analyzed to use for data-driven decision making.

Businesses usually have two types of data processing capabilities: OLTP and OLAP.

### OLTP versus OLAP

Though they sound similar and are both online data processing systems, there is a stark difference between the two.

OLTP enables the real-time execution of large numbers of transactions by large numbers of people, whereas online analytical processing (OLAP) usually involves querying these transactions (also referred to as records) in a database for analytical purposes. OLAP helps companies extract insights from their transaction data so they can use it for making more informed decisions.

The table below shows comparison between OLTP and OLAP systems.

|OLTP Systems|OLAP Systems|
|--|--|
|Enable the real-time execution of large numbers of database transactions by large numbers of people|Usually involve querying many records (even all records) in a database for analytical purposes|
|Require lightning-fast response times|Require response times that are orders of magnitude slower than those required by OLTP|
|Modify small amounts of data frequently and usually involve a balance of reads and writes|Do not modify data at all; workloads are usually read-intensive|
|Use indexed data to improve response times|	
Store data in columnar format to allow easy access to large numbers of records|
|Require frequent or concurrent database backups|Require far less frequent database backup|
|Require relatively little storage space|	
Typically have significant storage space requirements, because they store large amounts of historical data|
|Usually run simple queries involving just one or a few records|Run complex queries involving large numbers of records|

So, OLTP is an online data modification system, whereas OLAP is an online historical multidimensional data store system that’s used to retrieve large amounts data for analytical purpose. OLAP usually provides analytics on data that was captured by one or more OLTP systems.

### Requirements for an OLTP system

The most common architecture of an OLTP system that uses transactional data is a three-tier architecture that typically consists of a presentation tier, a business logic tier, and a data store tier. The presentation tier is the front end, where the transaction originates via a human interaction or is system-generated. The logic tier consists of rules that verify the transaction and ensure all the data required to complete the transaction is available. The data store tier stores the transaction and all the data related to it.

The main characteristics of an online transaction processing system are the following:

### ACID Compliance

OLTP systems must ensure that the entire transaction is recorded correctly. A transaction is usually an execution of a program that may require the execution of multiple steps or operations. It may be complete when all parties involved acknowledge the transaction, or when the product/service is delivered, or when a certain number of updates are made to the specific tables in the database. A transaction is recorded correctly only if all the steps involved are executed and recorded. If there is any error in any one of the steps, the entire transaction must be aborted and all the steps must be deleted from the system. Thus OLTP systems must comply with atomic, consistent, isolated, and durable (ACID) properties to ensure the accuracy of the data in the system.

-   Atomic: Atomicity controls guarantee that all the steps in a transaction are completed successfully as a group. That is, if any steps between the transactions fail, all other steps must also fail or be reverted. The successful completion of a transaction is called commit. The failure of a transaction is called abort.
-   Consistent: The transaction preserves the internal consistency of the database. If you execute the transaction all by itself on a database that’s initially consistent, then when the transaction finishes executing the database is again consistent.
-   Isolated: The transaction executes as if it were running alone, with no other transactions. That is, the effect of running a set of transactions is the same as running them one at a time. This behavior is called serializability and is usually implemented by locking the specific rows in the table.
-   Durable: The transaction’s results will not be lost in a failure.

### Concurrency

OLTP systems can have enormously large user populations, with many users trying to access the same data at the same time. The system must ensure that all these users trying to read or write into the system can do so concurrently. Concurrency controls guarantee that two users accessing the same data in the database system at the same time will not be able to change that data, or that one user has to wait until the other user has finished processing before changing that piece of data.

### Scale

OLTP systems must be able to scale up and down instantly to manage the transaction volume in real time and execute transactions concurrently, irrespective of the number of users trying to access the system.

### Availability

An OLTP system must be always available and always ready to accept transactions. Loss of a transaction can lead to loss of revenue or may have legal implications. Because transactions can be executed from anywhere in the world and at any time, the system must be available 24/7.

### High throughput and short response time

OLTP systems require nanosecond or even shorter response times to keep enterprise users productive and to meet the growing expectations of customers.

### Reliability

OLTP systems typically read and manipulate highly selective, small amounts of data. It is paramount that at any given point of time the data in the database is reliable and trustworthy for the users and applications accessing that data.

### Security

Because these systems store highly sensitive customer transaction data, data security is critical. Any breach can be very costly for the company.

### Recoverability

OLTP systems must have the ability to recover in case of any hardware or software failure.

### Databases for OLTP workloads

Relational databases were built specifically for transaction applications. They embody all the essential elements required for storing and processing large volumes of transactions, while also continuously being updated with new features and functionality for extracting more value from this rich transaction data. Relational databases are designed from the ground up to provide the highest possible availability and fastest performance. They provide concurrency and ACID compliance so the data is accurate, always available, and easily accessible. They store data in tables after extracting relationships between the data so the data can be used by any application, ensuring a single source of truth.

## What are the 4 V's of Big Data

Big data refers to large amounts of data that can inform analysts of trends and patterns related to human behavior and interactions. There are four major components of big data.

### Volume

Volume refers to how much data is actually collected. An analyst must determine what data and how much of it needs to be collected for a given purpose. To imagine the possibilities, consider a social media site where people write updates, like photos, review business, watch videos, search for new items, and interact in some way with just about everything they see on their screens. Each of these interactions generates data about that person that can be fed into algorithms.

### Veracity

Veracity relates to how reliable data is. An analyst wants to ensure that the data they look at is valid and comes from a trusted source. This is determined by where the data comes from and how it is collected. Data collected from native sites rather than third-parties is necessary for reliable results. Additionally, testing measures must be properly designed to ensure that data results in the desired information and is not extraneous.

### Velocity

Velocity in big data refers to how fast data can be generated, gathered and analyzed. Big data does not always have to be used imminently, but in some fields, there is a great advantage to receiving up to the second information about rates and being able to act accordingly. In other businesses, the data trend over time is more important to help make predictions or solve lingering problems.

### Variety

Variety refers to how many points of reference are used to collect data. If data is collected from a single source, that information may be skewed in some ways. It will not represent a broad population or wide trend. In some cases, like with velocity, that is fine. A pet microchipping service, for example, may only want to target data from a neighborhood social networking site. A movie company, on the other hand, may want to target several social media sites and people of various age groups. So they would need more points of reference to decide on the best places to do business.

## What is a data lake

(https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-a-data-lake)

### Data Lake Definition

A data lake is a centralized repository that ingests and stores large volumes of data in its original form. The data can then be processed and used as a basis for a variety of analytic needs. Due to its open, scalable architecture, a data lake can accommodate all types of data from any source, from structured (database tables, excel sheets) to semi-structured (XML files, webpages) to unstructured (images, audio files, tweets), all without sacrificing fidelity. The data files are typically stored in staged zones - raw, cleansed, and curated - so that differents types of users may use the data in its various forms to meet their needs. Data lakes provide core data consistency across a variety of applications, powering big data analytics, machine learning, predictive analytics, and other forms of intelligent action.

### Why are data lakes important for businesses

Today's highly connected, insights-driven world would not be possible without the advent of data lake solutions. That's because organizations rely on comprehensive data lakes platforms to keep raw data consolidated (GCP data lake, cloud storage is not a data lake), integrated, secure, and accessible. Scalable storage tools can hold and protect data in one central place, eliminating silos at an optimal cost. This lays the foundation for users to perform a wide variety of workload categories, such as big data processing, sql queries, text mining, streaming analytics, and machine learning. The data can then be used to feed upstream data visualization and ad-hoc reporting needs. A modern end-to-end data platform addresses the complete needs of big data architecture centered around the data lake.

### Data Lake Use Cases

With a well-architected solution, the potential for innovation is endless. Here are just a few examples of how organizations across a range of industries use data lake platforms to optimize their growth:

-   Streaming Media
    -   Subscription based streaming companies collect and process insights on customer behaviour, which they may use to improve their recommendation algorithm.
-   Finance
    -   Investment firms use the most up to date market data, which is collected and stored in real time, to efficiently manage portfolio risks.
-   Healthcare
    -   Healthcare organizations rely on big data to improve the quality of care for patients. Hospitals use vast amounts of historical data to streamline patient pathways, resulting in better outcomes and reduced cost of care.
-   Omnichannel retailer
    -   Retailers use data lakes to capture and consolidate data that's coming in from multiple touchpoints, including mobile, social, chat, word-of-mouth, and in person.
-   IoT
    -   Hardware sensors generate enormous amounts of semi-structured to unstructured data on the surrounding physical world. Data lakes provide a central repository for this information to live in for future analysis.
-   Digital Supply Chain
    -   Data lakes help manufacturers consolidate disparate warehousing data, including EDI systems, XML, and JSONs.
-   Sales
    -   Data scientists and sales engineers often build predictive models to help determine customer behavior and reduce overall churn.

### Data Lake vs Data Warehouse

Now that you know what a data lake is, why it matters, and also how it is used across a variety of organizations, let us ask what the difference between a data lake and a data warehouse is? On top of that, it is important to realize when to use one over the other.

While data lakes and data warehouses are similar in that they both store and process data, each have their own specialties, and therefore their own use cases. That's why it's common for an enterprise-level organization to include a data lake and a data warehouse in their analytics ecosystem. Both repositories work together to form a secure, end-to-end system for storage, processing, and faster time to insight.

A data lake captures both relational and non-relational data from a variety of sources - business applications, mobile apps, IoT devices, social media, or streaming - without having to define the structure or schema of the data until it is read. Schema-on-read ensures that any type of data can be stored in its raw form. As a result, data lakes can hold a wide variety of data types, from structured to semi-structured to unstructured, at any scale. Their flexible and scalable natuer make them essential for performing complex forms of data analysis using different types of compute processing tools.

By contrast, a data warehouse is relational in nature. The structure or schema is modeled or predefined by business and product requirements that are curated, conformed, and optimized for sql query operations. While a data lake holds data of all structure types, including raw and unprocessed data, a data warehouse stores data that has been treated and transformed with a specific purpose in mind, which can then be used to source analytic or operational reporting. This makes data warehouses ideal for producing more standardized forms of BI analysis, or for serving a business use case that has been already defined.

|-|Data Lake|Data Warehouse|
|--|--|--|
|Type|Structured, semi-structured, unstructured|Structured|
||Relational, non-relational|Relational|
|Schema|Schema on read|Schema on write|
|Format|Raw, unfiltered|Processed, Vetted|
|Sources|Big data, IoT, social media, streaming data|Application, business, transactional data, batch reporting|
|Scalability|Easy to scale at a low cost|Difficult and expensive to scale|
|Users|Data scientists, data engineers|Data warehouse professionals, business analysts|
|Use Cases|Machine learning, predictive analytics, real-time analytics|Core reporting, BI|

### Data Lake vs. Data Lakehouse

Now you know the difference between a data lake vs. a data warehouse. But what's the difference between a data lake and a data lakehouse. And is it necessary to have both?

Despite its many advantages, a traditional data lake is not without its drawbacks. Because data lakes can accomodoate all types of data from all kinds of sources, issues related to quality control, data corruption, and improper partitioning can occur. A poorly managed data lake not only tarnishes data integrity, but it can also lead to bottlenecks, slow performance, and security risks.

That's where the data lakehouse comes into play. A data lakehouse is an open standards-based storage solution that is multifaceted in nature. It can address the needs of data scientists and engineers who conduct deep data analysis and processing, as well as the needs of traditional data warehouse professionals who curate and publish data for business intelligence and reporting purposes. The beauty of the lakehouse is that each workload can seamlessly operate on top of the data lake without having to duplicate the data into another structurally predefined database. This ensures that everyone is working on the most up-to-date data, while also reducing redundancies.

Data lakehouses address the challenges of traditional data lakes by adding a Delta Lake storage Layer directly on top of the cloud data lake. The storage layer provided a flexible analytic architecture that can handle ACID (atomicity, consistency, isolate, and durability) transactions for data reliablility, streaming integrations, and advanced features like data versioning and schema enforcement. This allows for a range of analytic activity over the lake, all without compromising core data consistency. While the necessity of a lakehouse depends on how complex your needs are, its flexibility and range make it an optimal solution for many enterprise orgs.

|-|Data Lake|Data Lakehouse|
|--|--|--|
|Type|Structured, semi-structured, unstructured|Structured, semi-structured, unstructured|
||Relational, non-relational|Relational, non-relational|
|Schema|Schema on read|Schema on read, Schema on write|
|Format|Raw, unfiltered, processed, curated|Raw, unfiltered, processed, curated, delta format files|
|Sources|Big data, IoT, social media, streaming data|Big data, IoT, social media, streaming data, application, business, transactional data, batch reporting|
|Scalability|Easy to scale at a low cost|Easy to scale at a low cost|
|Users|Data scientists|Business analysts, data engineers, data scientists|
|Use Cases|Machine learning, predictive analytics|Core reporting, BI, machine learning, predictive analytics|

### What is data lake architecture

At its core, a data lake is a storage repository with no set architecture of its own. In order to make the most of its capabilities, it requires a wide range of tools, technologies, and compute engines that help optimize the integration, storage, and processing of data. These tools work together to create a cohesively layered architecture, one that is informed by big data and runs on top of the data lake. This architecture may also form the operating structure of a data lakehouse. Every organization has its own unique configuration, but most data lakehouse architectures feature the following:

-   Resource management and orchestration. 
    -   A resource manager enables the data lake to consistently execute tasks by allocating the right amount of data, resources, and computing power to the right places.
-   Connectors for easy access. 
    -   A variety of workflows allow users to easily access—and share—the data they need in the form that they need it in.
-   Reliable analytics. 
    -   A good analytics service should be fast, scalable, and distributed. It should also support a diverse range of workload categories across multiple languages.
-   Data classification. 
    -   Data profiling, cataloging, and archiving help organizations keep track of data content, quality, location, and history.
-   Extract, load, transform (ELT) processes. 
    -   ELT refers to the processes by which data is extracted from multiple sources and loaded into the data lake's raw zone, then cleaned and transformed after extraction so that applications may readily use it.
-   Security and support. 
    -   Data protection tools like masking, auditing, encryption, and access monitoring ensure that your data remains safe and private.
-   Governance and stewardship. 
    -   For the data lake platform to run as smoothly as possible, users should be educated on its architectural configuration, as well as best practices for data and operations management.

## What is a Delta Lake

(https://docs.gcp.databricks.com/en/delta/index.html)

Delta lake is an open source storage layer that brings ACID (atomicity, consistency, isolation, and durability) transactions to Apache spark and big data workloads.

## What is a Data Warehouse

(https://cloud.google.com/learn/what-is-a-data-warehouse#:~:text=A%20data%20warehouse%2C%20also%20called,customer%20relationship%20management%2C%20and%20more.)

A data warehouse, also called an enterprise data warehouse (EDW), is an enterprise data platform used for the analysis and reporting of structured and semi-structured data from multiple data sources, such as point-of-sale transactions, marketing automation, customer relationship management, and more.

Data warehouses include an analytical database and critical analytical components and procedures. They support ad hoc analysis and custom reporting, such as data pipelines, queries, and business applications. They can consolidate and integrate massive amounts of current and historical data in one place, and are designed to give a long-range view of data over time. These data warehouse capabilities have made data warehousing a primary staple of enterprise analytics that help support informed business decisions. BigQuery is a data warehouse.

### Traditional vs cloud-based data warehouse

Traditional data warehouses are hosted on-premises, with data flowing in from relational databases, transactional system, business applications, and other source systems. However, they are typically designed to capture a subset of data in batches and store it based on rigid schemas, making them unsuitable for spontaneous queries or real-time analysis. Companies also must purchase their own hardware and software with an on-premises data warehouse, making it expensive to scale and maintain. In a traditional warehouse, storage is typically limited compared to compute, so data is transformed quickly and then discared to keep storage space free.

Now days data analytics activities have transformed to the center of all core business activities, including revenue generation, cost containment, improving operations, and enhancing customer experiences. Ad data evolves and diversifies, organizations need more robust data warehouse solutions and advanced analytic tools for storing, managing, and analyzing large quantities of data across their organizations.

These systems must be scalable, reliable, secure enough for regulated industries, and flexible enough to support a wide variety of data types and big data use cases. They also need to support flexible pricing and compute, so you only pay for what you need instead of guessing your capacity. The requirements go beyond the capabilities of most legacy data warehouses. As a result, many enterprises are turning to cloud-based data warehouse solutions.

A cloud data warehouse makes no trade-offs from a traditional data warehouse, but extends capabilities and runs on a fully managed service in the cloud. Cloud data warehousing offers instant scalability to meet changing business requirements and powerful data processing to support complex analytical queries.

With a cloud data warehouse, you benefit from the inherent flexibility of a cloud environment with more predictable costs. The up-front investment is typically much lower and lead times are shorter than with on-premises data warehouse solutions because the cloud service provider managers and maintains the physical infrastructure.

### How data warehousing works in the cloud

Like a traditional data warehouse, cloud data warehouses collect, integrate, and store data from internal and external data sources. Data is typically transferred from a source system using a data pipeline. The data is extracted from the source system, transformed, and then loaded into the data warehouse—a process known as ETL (extract, transform, load). Data can also be sent directly to a central repository and then converted using ELT (extract, load, transform) processes. From there, users can use different business intelligence (BI) tools to access, mine, and report on data. Cloud data warehouses should also support streaming use cases to activate on data in real or near-real time.

Cloud data warehouses offer structured and semi-structured data storage, processing, integration, cleansing, loading, and so on within a public cloud environment. You can also use them with a cloud data lake to collect and store unstructured data. With some providers, it's even possible to unify your data warehouse and data lake to maintain and centrally manage a single copy of your enterprise data.

Different cloud providers may take various approaches when it comes to cloud data warehouse services. For example, some cloud data warehouses may use a cluster-based architecture similar to a traditional data warehouse. In contrast, others adopt a modern serverless architecture, which further minimizes data management responsibilities. However, most cloud data warehouses provide built-in data storage and capacity management features and automatic upgrades.

Other key capabilities that cloud data warehouses include: 

-   Massively parallel processing (MPP)
-   Columnar data stores
-   Self-service ETL and ELT data integration  
-   Disaster recovery features and automatic backups
-   Compliance and data governance tools
-   Built-in integrations for BI, AI, and machine learning

### Advantages of data warehousing in the cloud

Companies are increasingly moving away from traditional data warehouses and migrating to the cloud, leveraging the cost savings and scalability that managed services can provide. 

Here are the primary advantages of cloud data warehousing.

### Built for scale

Cloud data warehouses are elastic, providing nearly limitless storage and capacity. You can scale them up or down easily as your business needs change and only pay for what you use. 

### Machine Learning and AI initiatives

Customers can quickly unlock and operationalize machine learning models and AI technologies against cloud data warehouses for data mining, predicting business outcomes, and optimizing other areas, from data life cycle management to business processes to operational costs.

### Better Uptime

Cloud providers are obligated to meet SLAs and provide better uptime with reliable cloud infrastructure that scales seamlessly. On-premises data warehouses have scale and resource limitations that could impact performance.

### Cost Predictability

With cloud, you gain more flexible and predictable pricing. Some providers charge by throughput or per hour per node. Others charge a fixed price for a certain amount of resources. In every case, you avoid the mammoth costs incurred by an on-premises data warehouse that runs 24 hours a day, seven days a week, regardless of whether resources are in use or not.

### Operational savings

A cloud data warehouse is fully managed, allowing you to outsource management hassles to cloud providers who must meet service level agreements (SLAs). This provides operational savings and can keep your in-house team focused on growth initiatives.

### Real-time analytics

Cloud data warehouses provide more powerful computing that supports streaming data, allowing you to query data in real time. As a result, you can access and use data much faster than with an on-premises data warehouse, allowing you to get more accurate insights faster and make more informed business decisions.

### What is a data warehouse used for?

Cloud data warehousing offers a range of solutions that can benefit an organization. Here are some of the most common data warehouse use cases:

### Making real-time decisions

Analyze data in real time to procatively address challenges, identify opportunities, gain efficiency, reduce costs, and proactively respond to business events.

### Consolidating siloed data

Quickly pull data from multiple structured sources across your organization, such as point-of-sale systems, websites, and email lists, and bring it together into one location so that you can perform analysis and get insights.

### Enabling business reporting and ad hoc analysis

Keep historical data on a separate server from operational data so that end users can access it and run their own queries and reports without impacting the performance of operational systems or waiting to get help from IT.

### Implementing machine learning and AI

Collect historical and real-time data to develop algorithms that can provide predictive insights, such as anticipating traffic spikes or suggesting relevant products to a customer browsing a website.

Many businesses and industries require data analysis that is not only massive in scale, but also ongoing and in real time. For example, some service providers use real-time data to dynamically adjust prices throughout the day. Insurance companies track policies, sales, claims, payroll, and more. They also use machine learning to predict fraud. Gaming companies must track and react to user behavior in real time to enhance the player’s experience. Data warehouses make all of these activities possible.

If your organization has or does any of the following, you’re probably a good candidate for a data warehouse:

-   Multiple sources of disparate data
-   Big-data analysis and visualization—both asynchronously and in real time
-   Machine learning models and other AI-driven processes
-   Streaming analytics
-   Custom report generation and ad hoc analysis
-   Data mining
-   Data science and geospatial analysis

## What is serverless architecture

(https://cloud.google.com/discover/what-is-serverless-architecture)

Serverless architecture is a software design approach where developers can build and manage applications without managing the underlying architecture. Serverless applications still run on servers, but the cloud service provider is responsible for provisioning, managing, and scaling all the cloud infrastructure. 

### How does serverless architecture work?

Serverless architectures are designed to abstract servers and server management away from development teams. “Serverless” does not mean there are no servers; instead, the term refers to the overall development experience. 

From a developer’s perspective, you simply write the code and run it without worrying about anything else. All the provisioning, hardware maintenance, software and security updates to the servers, and other server management tasks fall to the cloud provider. In addition, serverless architectures automatically scale up or down according to traffic.

### Benefits of serverless architecture

Serverless solutions provide application development teams with several benefits over other types of infrastructure. Some of the main advantages of serverless architectures include the following: 

### Automation

Serverless solutions remove the toil of managing servers by automating tasks.

### Scalability

Serverless solutions scale up and down automatically in response to traffic without the need for fine-tuning or other manual configurations. 

### Productivity

Serverless computing empowers developers to focus on writing code and optimizing business logic rather than spending time on server management. Developers can also deploy their code directly into ad hoc testing environments as needed.

### Serverless architecture examples

Here are some common serverless architecture use cases:

-   Trigger-based actions or running scheduled tasks (e.g., daily reports, backups, business logic, etc.)
-   Building RESTful APIs for web and mobile applications
-   Asynchronous processing (e.g., transcoding video)
-   IT process automation, such as removing access automatically, initiating compliance security checks, or sending approvals
-   Automating continuous integration and continuous delivery (CI/CD) pipelines (e.g., code commits triggering a build, pull requests triggering automated testing)
-   Integrating with third-party services and APIs
-   Running scheduled tasks (e.g., daily reports, backups, business logic, etc.) 
-   Real-time data processing for structured and unstructured data

## Cluster-based data warehouse architecture

(https://www.fivetran.com/learn/cloud-data-warehouse#:~:text=A%20cluster%2Dbased%20architecture%20is,compute%20nodes%20to%20produce%20results.)

### Cluster-based

A cluster-based architecture is typically used to host a data warehouse in hybrid cloud systems. There are multiple server nodes, each with its storage, CPU and RAM. The lead nodes intake queries and assign them to compute nodes to produce results.

Organizations using this architecture must oversee the pipeline to check whether they have enough nodes to handle their queries. This means their engineers spend more time managing capacity, scalability and overall cluster health.

## A Deep Dive into Google BigQuery Architecture: How it Works

(https://panoply.io/data-warehouse-guide/bigquery-architecture/)

Google’s BigQuery is an enterprise-grade cloud-native data warehouse. BigQuery was first launched as a service in 2010 with general availability in November 2011. Since inception, BigQuery has evolved into a more economical and fully-managed data warehouse which can run blazing fast interactive and ad-hoc queries on datasets of petabyte-scale. In addition, BigQuery now integrates with a variety of Google Cloud Platform (GCP) services and third-party tools which makes it more useful.

BigQuery is serverless, or more precisely data warehouse as a service. There are no servers to manage or database software to install. BigQuery service manages underlying software as well as infrastructure including scalability and high-availability. The pricing model is quite simple - for every 1 TB of data processed you pay $5. BigQuery exposes simple client interface which enables users to run interactive queries.

Overall, you don’t need to know much about underlying BigQuery architecture or how this service operates under the hood. That’s the whole idea of BigQuery - you don’t need to worry about architecture and operation. To get started with BigQuery, your must be able to import your data into BigQuery, then be able to write your queries using SQL dialects offered by BigQuery.

Having said that, a good understanding of how Google BigQuery architecture works is useful when implementing various BigQuery best-practices including controlling costs, optimizing query performance, and optimizing storage. For instance, for best query performance, it is highly beneficial to understand how BigQuery allocates resources and relationship between the number of slots and query performance.

### High-Level Architecture

BigQuery is built on top of Dremel technology which has been in production internally in Google since 2006. Dremel is Google’s interactive ad-hoc query system for analysis of read-only nested data. Original Dremel papers were published in 2010 and at the time of publication Google was running multiple instances of Dremel ranging from tens to thousands of nodes.

### 10,000 foot view

BigQuery and Dremel share the same underlying architecture. By incorporating columnar storage and tree architecture of Dremel, BigQuery offers unprecedented performance. But, BigQuery is much more than Dremel. Dremel is just an execution engine for the BigQuery. In fact, BigQuery service leverages Google’s innovative technologies like Borg, Colossus, Capacitor, and Jupiter. As illustrated below, a BigQuery client (typically BigQuery Web UI or bg command-line tool or REST APIs) interact with Dremel engine via a client interface. Borg - Google’s large-scale cluster management system - allocates the compute capacity for the Dremel jobs. Dremel jobs read data from Google’s Colossus file systems using Jupiter network, perform various SQL operations and return results to the client. Dremel implements a multi-level serving tree to execute queries which are covered in more detail in following sections.

[bigquery-architecture-1.png]

It is important to note, BigQuery architecture separates the concepts of storage (Colossus) and compute (Borg) and allows them to scale independently - a key requirement for an elastic data warehouse. This makes BigQuery more economical and scalable compared to its counterparts.

### Storage

The most expensive part of any Big Data analytics platform is almost always disk I/O. BigQuery stores data in a columnar format known as Capacitor. As you may expect, each field of BigQuery table i.e. column is stored in a separate Capacitor file which enables BigQuery to achieve very high compression ratio and scan throughput. In 2016, Capacitor replaced ColumnIO - the previous generation optimized columnar storage format. Unlike ColumnIO, Capacitor enabled BigQuery to directly operate on compressed data, without decompressing the data on the fly.

You can import your data into BigQuery storage via Batch loads or Streaming. During the import process, BigQuery encodes every column separately into Capacitor format. Once all column data is encoded, it’s written back to Colossus. During encoding various statistics about the data is collected which is later used for query planning.

BigQuery leverages Capacitor to store data in Colossus. Colossus is Google’s latest generation distributed file system and successor to GFS (Google File Systems). Colossus handles cluster-wide replication, recovery and distributed management. It provides client-driven replication and encoding. When writing data to Colossus, BigQuery makes some decision about initial sharding strategy which evolves based on the query and access patterns. Once data is written, to enable the highest availability BigQuery initiates geo-replication of data across different data centers.

In a nutshell, Capacitor and Colossus are key ingredients of industry-leading performance characteristics offered by BigQuery. Colossus allows splitting of the data into multiple partitions to enable blazing fast parallel read whereas Capacitor reduces requires scan throughput. Together they make possible to process a terabyte data per second.

### Native vs. External

So far we have discussed the storage for the native BigQuery table. BigQuery can also perform queries against external data sources without the need to import data into the native BigQuery tables. Currently, BigQuery can perform direct queries against Google Cloud Bigtable, Google Cloud Storage, and Google Drive.

When using an external data source (aka federated data source), BigQuery performs on-the-fly loading of data into Dremel engine. Generally speaking, queries running against external data sources will be slower than native BigQuery tables. Performance of queries also depends on external storage type. For instance, queries against Google Cloud Storage will perform better than Google Drive. If performance is a concern then you should always import your data into BigQuery table before running the queries.

### Compute

BigQuery takes advantage of Borg for data processing. Borg simultaneously runs thousands of Dremel jobs across one or more clusters made up of tens of thousands of machines. In addition to assigning compute capacity for Dremel jobs, Borg handles fault-tolerance.

### Network

Apart from disk I/O, big data workloads are often rate-limited by network throughput. Due to the separation between compute and storage layers, BigQuery requires an ultra-fast network which can deliver terabytes of data in seconds directly from storage into compute for running Dremel jobs. Google’s Jupiter network enables BigQuery service to utilize 1 Petabit/sec of total bisection bandwidth.

### Read-Only

Due to columnar storage, existing records cannot be updated hence BigQuery primarily supports read-only use-cases. That said, you can always write the processed data back into new tables.

### Execution Model

Dremel engine uses a multi-level serving tree for scaling out SQL queries. This tree architecture has been specifically designed to run on commodity hardware. Dremel uses a query dispatcher which not only provides fault tolerance but also schedules queries based on priorities and the load.

In a serving tree, a root server receives incoming queries from clients and routes the queries to the next level. The root server is responsible to return query results to the client. Leaf nodes of the serving tree do the heavy lifting of reading the data from Colossus and performing filters and partial aggregation. To parallelize the query, each serving level performs (Root and Mixers) query rewrite and ultimately modified and partitioned queries reach to the leaf nodes for execution.

During query rewrite, few things happen. Firstly, the query is modified to include horizontal partitions of the table, i.e. shards (in original Dremel paper shards were referred as tablets). Secondly, certain SQL clause can be stripped out before sending to leaf nodes. In a typical Dremel tree, there are hundreds or thousands of leaf nodes. Leaf nodes return results to Mixers or intermediate nodes. Mixers perform aggregation of results returned by leaf nodes.

Each leaf node provides execution thread or number of processing units often called as slots. It is important to note, BigQuery automatically calculates how many slots should be assigned to each query. The number of allocated slots depending on query size and complexity. At the time of writing of this article, for on-demand pricing model maximum 2000 concurrent slots are allowed per BigQuery project.

To help you understand how Dremel engine works and how serving tree executes, let’s look into a simple query,

```sql
SELECT A, COUNT(B) FROM T GROUP BY A
```

When root server receives this query, the first thing it does is translate the query into a form which can be handled by next level of serving tree. It determines all shards of table T and then simplifies the query.

```sql
SELECT A, SUM(c) FROM (R1i UNION ALL ... R1n ) GROUP BY A
```

In this case R11, R12, . . . , R1n are results of queries sent to the Mixer 1, . . . , n at level 1 of the serving tree.

Next Mixers modify the incoming queries so that they can pass it to Leaf nodes. Leaf nodes receive the customized queries and read data from Colossus shards. A Lead node reads data for columns or fields mentioned in the query. As leaf node scans the shards, it walks through the opened column files in parallel, one row at a time.

Depending on the queries, data may be shuffled between leaf nodes. For instance, when you use GROUP EACH BY in your queries, Dremel engine will perform shuffle operation. It is important to understand the amount of shuffling required by your queries. Some query with operations like JOIN can run slow unless you optimise them to reduce the shuffling. That’s why BigQuery recommends trimming the data as early in the query as possible so that shuffling due to your operations is applied to a limited data set.

As BigQuery charges you for every 1 TB of data scanned by leaf nodes, we should avoid scanning too much or too frequently. There are many ways to do this. One is partitioning your tables by date. For each table, additional sharding of data performed by BigQuery which you can’t influence. Instead of using one big query, break them into small steps and for each step save query results into intermediate tables so that subsequent queries have less data scan. It may sound counter-intuitive but the LIMIT clause does not reduce the amount of data get scanned by a query. If you just need sample data for exploration, you should use Preview options and not a query with the LIMIT clause.

At each level of serving tree, various optimisations are applied so that nodes can return results as soon as they ready to be served. This includes tricks like priority queue or streaming results.

[bigquery-architecture-2.png]

### Some Mathematics

Now that we understand BigQuery architecture, let’s look into how resources allocation played out when you run an interactive query using BigQuery. Say you are querying against a table of 10 columns with storage 10TB and 1000 shards. As discussed earlier, when you import your data into a table BigQuery service determines the optimal number of shards for your table and tunes it based on data access and query pattern. During data import, BigQuery will create Capacitor files - one for each column of the table. In this particular case, 10 Capacitor files per shard.

Effectively, there are 1000 x 10 files to read if you perform a full scan (i.e. select * from table). To read these 10000 files you have 2000 concurrent slots (if you are on BigQuery on-demand pricing model and assuming this is only interactive query you are running under your BigQuery project), so on average, one slot will be reading 5 Capacitor files or 5 GB of data. To read this much data using Jupiter network it will take anywhere ~4 seconds (10 Gbps) which is one of the key differentiators for BigQuery as a service.

Obviously, we should avoid full scan because a full scan is most expensive - both computationally as well as cost wise - way to query your data. We should query only the columns that we need and that’s an important best-practice for any column-oriented database or data warehouse.

### Data Model

BigQuery stores data as nested relations. The schema for a relation is represented by a tree. Nodes of the tree are attributes, and leaf attributes hold values. BigQuery data is stored in columns (leaf attributes). In addition to compressed column values, every column also stores structure information to indicate how the values in a column are distributed throughout the tree using two parameters - definition and repetition levels. These parameters help to reconstruct the full or partial representation of the record by reading only requested columns.

[bigquery-architecture-3.png]

To take full advantage of nested and repeated fields offered by BigQuery data structure, we should denormalize data whenever possible. Denormalization localizes the necessary data to individual nodes which reduce the network communication required for shuffling between slots.

### Query Language

BigQuery currently supports two different SQL dialects: standard SQL and legacy SQL. Standard SQL is compliant with the SQL 2011 and offers several advantages over the legacy alternative. Legacy SQL is original Dremel dialect. Both SQL dialects supports user-defined functions (UDFs). You can write queries in any format but Google recommends standard SQL. In 2014, Google published another paper describing how Dremel engine uses a semi-flattening tree data structure along with a standard SQL evaluation algorithm to support standard SQL query computation. This semi-flattening data structure is more aligned the way Dremel processes data and is usually much more compact than flattened data.

It is important to note that when denormalizing your data you can preserve some relationships taking advantage of nested and repeated fields instead of completely flattening your data. This is exactly what we will call semi-flattening data structure.

## Difference Between OLAP and OLTP in DMBS

(https://www.geeksforgeeks.org/difference-between-olap-and-oltp-in-dbms/)

OLAP stands for Online Analytical Processing. OLAP systems have the capability to analyze database information of multiple systems at the current time. The primary goal of OLAP Service is data analysis and not data processing. 

OLTP stands for Online Transaction Processing. OLTP has the work to administer day-to-day transactions in any organization. The main goal of OLTP is data processing not data analysis.

### Online Analytical Processing (OLAP)

Online Analytical Processing (OLAP) consists of a type of software tool that is used for data analysis for business decisions. OLAP provides an environment to get insights from the database retrieved from multiple database systems at one time. 

### OLAP Examples

Any type of Data Warehouse System is an OLAP system. The uses of the OLAP System are described below.

-   Spotify analyzed songs by users to come up with a personalized homepage of their songs and playlist.
-   Netflix movie recommendation system.

[Difference-between-OLAP-and-OLTP-in-DBMS-1.png]

### Benefits of OLAP services

-   OLAP services help in keeping consistency and calculation.
-   We can store planning, analysis, and budgeting for business analytics within one platform.
-   OLAP services help in handling large volumes of data, which helps in enterprise-level business applications.
-   OLAP services help in applying security restrictions for data protection.
-   OLAP services provide a multidimensional view of data, which helps in applying operations on data in various ways.
 
### Drawbacks of OLAP SERvices

-   OLAP Services requires professionals to handle the data because of its complex modeling procedure.
-   OLAP services are expensive to implement and maintain in cases when datasets are large.
-   We can perform an analysis of data only after extraction and transformation of data in the case of OLAP which delays the system.
-   OLAP services are not efficient for decision-making, as it is updated on a periodic basis.

### Online TRansaction Processing (OLTP)

Online transaction processing provides transaction-oriented applications in a 3-tier architecture. OLTP administers the day-to-day transactions of an organization. #

### OLTP Examples

An example considered for OLTP System is ATM Center a person who authenticates first will receive the amount first and the condition is that the amount to be withdrawn must be present in the ATM. The uses of the OLTP System are described below.

-   ATM center is an OLTP application.
-   OLTP handles the ACID properties during data transactions via the application.
-   It’s also used for Online banking, Online airline ticket booking, sending a text message, add a book to the shopping cart.

[Difference-between-OLAP-and-OLTP-in-DBMS-2.png]

### Benefits of the OLTP Services

-   OLTP services allow users to read, write and delete data operations quickly.
-   OLTP services help in increasing users and transactions which helps in real-time access to data.
-   OLTP services help to provide better security by applying multiple security features.
-   OLTP services help in making better decision making by providing accurate data or current data.
-   OLTP Services provide Data Integrity, Consistency, and High Availability to the data.

### Drawbacks of OLTP SERvices

-   OLTP has limited analysis capability as they are not capable of intending complex analysis or reporting.
-   OLTP has high maintenance costs because of frequent maintenance, backups, and recovery.
-   OLTP Services get hampered in the case whenever there is a hardware failure which leads to the failure of online transactions.
-   OLTP Services many times experience issues such as duplicate or inconsistent data.

### Difference between OLAP and OLTP

|Category|OLAP (Online Analytical Processing)|OLTP (Online Transaction Processing)|
|Definition|It is well-known as an online database query management system.|It is well-known as an online database modifying system.|
|Data source|Consists of historical data from various Databases.|Consists of only operational current data. |
|Method used|It makes use of a data warehouse.|It makes use of a standard database management system (DBMS).|
|Application|It is subject-oriented. Used for Data Mining, Analytics, Decisions making, etc.|It is application-oriented. Used for business tasks.|
|Normalized|In an OLAP database, tables are not normalized.|In an OLTP database, tables are normalized (3NF).|
|Usage of data|The data is used in planning, problem-solving, and decision-making.|The data is used to perform day-to-day fundamental operations.|
|Task|It provides a multi-dimensional view of different business tasks.|It reveals a snapshot of present business tasks.|
|Purpose|It serves the purpose to extract information for analysis and decision-making.|It serves the purpose to Insert, Update, and Delete information from the database.|
|Volume of data|A large amount of data is stored typically in TB, PB|The size of the data is relatively small as the historical data is archived in MB, and GB.|
|Queries|Relatively slow as the amount of data involved is large. Queries may take hours.|Very Fast as the queries operate on 5% of the data.|
|Update|The OLAP database is not often updated. As a result, data integrity is unaffected.|The data integrity constraint must be maintained in an OLTP database.|
|Backup and Recovery|It only needs backup from time to time as compared to OLTP.|The backup and recovery process is maintained rigorously|
|Processing time|The processing of complex queries can take a lengthy time.|It is comparatively fast in processing because of simple and straightforward queries.|
|Types of users|This data is generally managed by CEO, MD, and GM.|This data is managed by clerksForex and managers.|
|Operations|Only read and rarely write operations.|Both read and write operations.|
|Updates|With lengthy, scheduled batch operations, data is refreshed on a regular basis.|The user initiates data updates, which are brief and quick.|
|Nature of audience|The process is focused on the customer.  |The process is focused on the market. |
|Database Design|Design with a focus on the subject. |Design that is focused on the application.|
|Productivity|Improves the efficiency of business analysts.|Enhances the user’s productivity.|

## Understand Slots

(https://cloud.google.com/bigquery/docs/slots#:~:text=BigQuery%20allocates%20slot%20capacity%20within,The%20scheduler%20provides%20eventual%20fairness.)

A BigQuery slot is a virtual CPU used by BigQuery to execute SQL queries. During the query execution, BigQuery automatically calculates how many slots a query requires, depending on the query size and complexity.

You have a choice of using an on-demand pricing model or a capacity-based pricing model. Both models use slots for data processing. With a capacity-based model, you can pay for dedicated or autoscaled query processing capacity. The capacity-based model gives you explicit control over slots and analytics capacity, whereas the on-demand model does not.

Customers on the capacity-based pricing model explicitly choose how many slots to reserve. Your queries run within that capacity, and you pay for that capacity continuously every second it's deployed. For example, if you purchase 2,000 BigQuery slots, your queries in aggregate are limited to using 2,000 virtual CPUs at any given time. You have this capacity until you delete it, and you pay for 2,000 slots until you delete them.

Projects on the BigQuery on-demand pricing model are subject to per-project slot quota with transient burst capability. Most users on the on-demand model find the default slot capacity more than sufficient. Depending on the workload, access to more slots improves query performance. To check how many slots your account uses, see BigQuery monitoring.

### Estimate how many slots to purchase

BigQuery is architected to scale efficiently with increased resources. Depending on the workload, incremental capacity is likely to give you incremental benefits. Therefore, choosing the optimal number of slots to purchase depends on your requirements for performance, throughput, and utility.

You can experiment with baseline and autoscaling slots to determine the best configuration of slots. For example, you can test your workload with 500 baseline slots, then 1,000, then 1,500, and 2,000, and observe the impact on performance.

You can also examine the current slot usage of your projects, along with the chosen monthly price that you want to pay. On-demand workloads have a soft slot cap of 2,000 slots, but it is important to check how many slots are actually being used by your projects by using INFORMATION_SCHEMA.JOBS* views, Cloud Logging, the Jobs API, or BigQuery Audit logs.

[reservations-monitoring-timeline.png]

After you purchase slots and run your workloads for at least seven days, you can use the slot estimator to analyze performance and model the effect of adding or reducing slots.

### Query Execution Using Slots

When BigQuery executes a query job, it converts the declarative SQL statement into a graph of execution, broken up into a series of query stages, which themselves are composed of more granular sets of execution steps. BigQuery uses a heavily distributed parallel architecture to run these queries, and the stages model the units of work that many potential workers may execute in parallel. Stages communicate with one another by using a fast distributed shuffle architecture, which is discussed in more detail on the Google Cloud blog.

BigQuery query execution is dynamic, which means that the query plan can be modified while a query is in flight. Stages that are introduced while a query is running are often used to improve data distribution throughout query workers.

BigQuery can run multiple stages concurrently. BigQuery can use speculative execution to accelerate a query, and BigQuery can dynamically repartition a stage to achieve optimal parallelization.

BigQuery slots execute individual units of work at each stage of the query. For example, if BigQuery determines that a stage's optimal parallelization factor is 10, it requests 10 slots to process that stage.

[slots-query.png]

### Query execution under slot resource economy

If a query requests more slots than currently available, BigQuery queues up individual units of work and waits for slots to become available. As progress on query execution is made, and as slots free up, these queued up units of work get dynamically picked up for execution.

BigQuery can request any number of slots for a particular stage of a query. The number of slots requested is not related to the amount of capacity you purchase, but rather an indication of the most optimal parallelization factor chosen by BigQuery for that stage. Units of work queue up and get executed as slots become available.

When query demands exceed slots you committed to, you are not charged for additional slots, and you are not charged for additional on-demand rates. Your individual units of work queue up.

For example,

1.  A query stage requests 2,000 slots, but only 1,000 are available.
2.  BigQuery consumes all 1,000 slots and queues up the other 1,000 slots.
3.  Thereafter, if 100 slots finish their work, they dynamically pick up 100 units of work from the 1,000 queued up units of work. 900 units of queued up work remain.
4.  Thereafter, if 500 slots finish their work, they dynamically pick up 500 units of work from the 900 queued up units of work. 400 units of queued up work remain.

[slots-scheduling.png]

### Idle Slots

At any given time, some slots might be idle. This can include:

-   Slot commitments that are not allocated to any reservation.
-   Slots that are allocated to a reservation baseline but aren't in use.

By default, queries running in a reservation automatically use idle slots from other reservations within the same administration project. That means a job can always run as long as there's capacity. Idle capacity is immediately preemptible back to the original assigned reservation as needed, regardless of the priority of the query that needs the resources. This happens automatically in real time.

To prevent this behavior and ensure a reservation only uses its provisioned slots provisioned, set ignore_idle_slots to true. Reservations with ignore_idle_slots set to true can, however, share their idle slots with other reservations.

You cannot share idle slots between reservations of different editions. You can share only the baseline slots or committed slots. Autoscaled slots might be temporarily available but are not shareable because they might scale down.

As long as ignore_idle_slots is false, a reservation can have a slot count of 0 and still have access to unused slots. If you use only the default reservation, toggle off ignore_idle_slots as a best practice. You can then assign a project or folder to that reservation and it will only use idle slots.

Assignments of type ML_EXTERNAL are an exception in that slots used by BigQuery ML external model creation jobs are not preemptible. The slots in a reservation with both ML_EXTERNAL and QUERY assignment types are only available for other query jobs when the slots are not occupied by the ML_EXTERNAL jobs. Moreover, these jobs cannot use idle slots from other reservations.

### Slot allocation within reservations

BigQuery allocates slot capacity within a single reservation using an algorithm called fair scheduling.

The BigQuery scheduler enforces the equal sharing of slots among projects with running queries within a reservation, and then within jobs of a given project. The scheduler provides eventual fairness. During short periods, some jobs might get a disproportionate share of slots, but the scheduler eventually corrects this. The goal of the scheduler is to find a balance between aggressively evicting running tasks (which results in wasting slot time) and being too lenient (which results in jobs with long running tasks getting a disproportionate share of the slot time).

If an important job consistently needs more slots than it receives from the scheduler, consider creating an additional reservation with a guaranteed number of slots and assigning the job to that reservation.

### Fair Scheduling in BigQuery

Slots are distributed fairly among projects and then within the jobs in the project. This means that every query has access to all available slots at any time, and capacity is dynamically and automatically re-allocated among active queries as each query's capacity demands change. Queries complete and new queries get submitted for execution under the following conditions:

-   Whenever a new query is submitted, capacity is automatically re-allocated across executing queries. Individual units of work can be gracefully paused, resumed, and queued up as more capacity becomes available to each query.
-   Whenever a query completes, capacity consumed by that query automatically becomes immediately available for all other queries to use.
-   Whenever a query's capacity demands change due to changes in query's dynamic DAG, BigQuery automatically re-evaluates capacity availability for this and all other queries, re-allocating and pausing slots as necessary.

[slots-scheduling-multiple-queries.png]

Depending on complexity and size, a query might not require all the slots it has the right to, or it may require more. BigQuery dynamically ensures that, given fair scheduling, all slots can be fully used at any point in time.

## Overview of BigQuery Storage

(https://cloud.google.com/bigquery/docs/storage_overview)

BigQuery storage is optimized for running analytic queries over large datasets. It also supports high-throughput streaming ingestion and high-throughput reads. Understanding BigQuery storage can help you to optimize your workloads.

### Overview

One of the key features of BigQuery's architecture is the separation of storage and compute. This allows BigQuery to scale both storage and compute independently, based on demand.

[bigquery-storage-architecture.png]

When you run a query, the query engine distributes the work in parallel across multiple workers, which scan the relevant tables in storage, process the query, and then gather the results. BigQuery executes queries completely in memory, using a petabit network to ensure that data moves extremely quickly to the worker nodes.

Here are some key features of BigQuery storage:

-   Managed. 
    -   BigQuery storage is a completely managed service. You don't need to provision storage resources or reserve units of storage. BigQuery automatically allocates storage for you when you load data into the system. You only pay for the amount of storage that you use. The BigQuery pricing model charges for compute and storage separately
-   Durable. 
    -   BigQuery storage is designed for 99.999999999% (11 9's) annual durability. BigQuery replicates your data across multiple availability zones to protect from data loss due to machine-level failures or zonal failures.
-   Encrypted. 
    -   BigQuery automatically encrypts all data before it is written to disk. You can provide your own encryption key or let Google manage the encryption key.
-   Efficient. 
    -   BigQuery storage uses an efficient encoding format that is optimized for analytic workloads.

### Table Data

The majority of the data that you store in BigQuery is table data. Table data includes standard tables, table clones, table snapshots, and materialized views. You are billed for the storage that you use for these resources.

-   Standard tables contain structured data. Every table has a schema, and every column in the schema has a data type. BigQuery stores data in columnar format.
-   Table clones are lightweight, writable copies of standard tables. BigQuery only stores the delta between a table clone and its base table.
-   Table snapshots are point-in-time copies of tables. Table snapshots are read-only, but you can restore a table from a table snapshot. BigQuery only stores the delta between a table snapshot and its base table.
-   Materialized views are precomputed views that periodically cache the results of the view query. The cached results are stored in BigQuery storage.

In addition, cached query results are stored as temporary tables. You aren't charged for cached query results stored in temporary tables.

External tables are a special type of table, where the data resides in a data store that is external to BigQuery, such as Cloud Storage. An external table has a table schema, just like a standard table, but the table definition points to the external data store. In this case, only the table metadata is kept in BigQuery storage. BigQuery does not charge for external table storage, although the external data store might charge for storage.

BigQuery organizes tables and other resources into logical containers called datasets. How you group your BigQuery resources affects permissions, quotas, billing, and other aspects of your BigQuery workloads.

### Metadata

BigQuery storage also holds metadata about your BigQuery resources. You aren't charged for metadata storage.

When you create any persistent entity in BigQuery, such as a table, view, or user-defined function (UDF), BigQuery stores metadata about the entity. This is true even for resources that don't contain any table data, such as UDFs and logical views.

Metadata includes information such as the table schema, partitioning and clustering specifications, table expiration times, and other information. This type of metadata is visible to the user and can be configured when you create the resource. In addition, BigQuery stores metadata that it uses internally to optimize queries. This metadata is not directly visible to users.

### Storage Layout

Many traditional database systems store their data in row-oriented format, meaning rows are stored together, with the fields in each row appearing sequentially on disk. Row-oriented databases are efficient at looking up individual records. However, they can be less efficient at performing analytical functions across many records, because the system has to read every field when accessing a record.

[row-oriented-store.png]

BigQuery stores table data in columnar format, meaning it stores each column separately. Column-oriented databases are particularly efficient at scanning individual columns over an entire dataset.

Column-oriented databases are optimized for analytic workloads that aggregate data over a very large number of records. Often, an analytic query only needs to read a few columns from a table. For example, if you want to compute the sum of a column over millions of rows, BigQuery can read that column data without reading every field of every row.

Another advantage of column-oriented databases is that data within a column typically has more redundancy than data across a row. This characteristic allows for greater data compression by using techniques such as run-length encoding, which can improve read performance.

[column-oriented-store.png]

BigQuery does not support foreign keys. This makes BigQuery more suitable for OLAP and data warehouse workloads than OLTP workloads. For OLTP workloads, consider using either Spanner or Cloud SQL. BigQuery supports federated queries with both of these database services.

### Optimize Storage

Optimizing BigQuery storage improves query performance and controls cost. To view the table storage metadata, query the following INFORMATION_SCHEMA views:

INFORMATION_SCHEMA.TABLE_STORAGE
INFORMATION_SCHEMA.TABLE_STORAGE_BY_ORGANIZATION

### Load Data

There are several basic patterns for ingesting data into BigQuery.

-   Batch load: Load your source data into a BigQuery table in a single batch operation. This can be a one-time operation or you can automate it to occur on a schedule. A batch load operation can create a new table or append data into an existing table.

-   Streaming: Continually stream smaller batches of data, so that the data is available for querying in near-real-time.

-   Generated data: Use SQL statements to insert rows into an existing table or write the results of a query to a table.

### Read Data from BigQuery Storage

Most of the time, you store data in BigQuery in order to run analytical queries on that data. However, sometimes you might want to read records directly from a table. BigQuery provides several ways to read table data:

-   BigQuery API: Synchronous paginated access with the tabledata.list method. Data is read in a serial fashion, one page per invocation. For more information, see Browsing table data.

-   BigQuery Storage API: Streaming high-throughput access that also supports server-side column projection and filtering. Reads can be parallelized across many readers by segmenting them into multiple disjoint streams.

-   Export: Asynchronous high-throughput copying to Google Cloud Storage, either with extract jobs or the EXPORT DATA. If you need to copy data in Cloud Storage, export the data either with an extract job or an EXPORT DATA statement.

-   Copy: Asynchronous copying of datasets within BigQuery. The copy is done logically when the source and destination location is the same.

Based on the application requirements, you can read the table data:

-   Read and copy: If you need an at-rest copy in Cloud Storage, export the data either with an extract job or an EXPORT DATA statement. If you only want to read the data, use the BigQuery Storage API. If you want to make a copy within BigQuery, then use a copy job.
-   Scale: The BigQuery API is the least efficient method and shouldn't be used for high volume reads. If you need to export more than 50 TB of data per day, use the EXPORT DATA statement or the BigQuery Storage API.
-   Time to return the first row: The BigQuery API is the fastest method to return the first row, but should only be used to read small amounts of data. The BigQuery Storage API is slower to return the first row, but has much higher-throughput. Exports and copies must finish before any rows can be read, so the time to the first row for these types of jobs can be on the order of minutes.

### Deletion

When you delete a table, the data persists for at least the duration of your time travel window. After this, data is cleaned up from disk within the Google Cloud deletion timeline. Some deletion operations, such as the DROP COLUMN statement, are metadata-only operations. In this case, storage is freed up the next time you modify the affected rows. If you do not modify the table, there is no guaranteed time within which the storage is freed up. For more information, see Data deletion on Google Cloud.

## Optimize Storage in BigQuery

(https://cloud.google.com/bigquery/docs/best-practices-storage)

This page provides best practices for optimizing BigQuery storage. BigQuery stores data in columnar format. Column-oriented databases are optimized for analytic workloads that aggregate data over a very large number of records. As columns have typically more redundancy than rows, this characteristic allows for greater data compression by using techniques such as run-length encoding.

BigQuery provides details about the storage consumption of your resources. To view the table storage metadata, query the following INFORMATION_SCHEMA views:

-   INFORMATION_SCHEMA.TABLE_STORAGE
-   INFORMATION_SCHEMA.TABLE_STORAGE_BY_ORGANIZATION

### Cluster table data

Best practice: Create clustered tables.

To optimize storage for queries, start by clustering table data. By clustering frequently used columns, you can reduce the total volume of data scanned by the query.

### Parition table data

Best practice: Divide large tables with partitions.

With partitions, you can group and sort your data by a set of defined column characteristics, such as an integer column, a time-unit column, or the ingestion time. Partitioning improves the query performance and control costs by reducing the number of bytes read by a query.

### Use the table and parition expiration settings

Best practice: To optimize storage, configure the default expiration settings for datasets, tables, and partitioned tables.

You can control storage costs and optimize storage usage by setting the default table expiration for newly created tables in a dataset. When a table expires, it gets deleted along with all of the data that the table contains. If you set the property when the dataset is created, any table created in the dataset is deleted after the expiration period. If you set the property after the dataset is created, only new tables are deleted after the expiration period.

For example, if you set the default table expiration to seven days, older data is automatically deleted after one week.

This option is useful if you need access to only the most recent data. It is also useful if you are experimenting with data and don't need to preserve it.

If your tables are partitioned by date, the dataset's default table expiration applies to the individual partitions. You can also control partition expiration using the time_partitioning_expiration flag in the bq command-line tool or the expirationMs configuration setting in the API. When a partition expires, data in the partition is deleted but the partitioned table is not dropped even if the table is empty. For example, the following command expires partitions after three days:

```
bq mk --time_partitioning_type=DAY --time_partitioning_expiration=259200 project_id:dataset.table
```

### Store data in BigQuery

Best practice: Store your data in BigQuery.

When you load data into BigQuery from Cloud Storage, you are not charged for the load operation, but you do incur charges for storing the data in Cloud Storage. After the data is loaded into BigQuery, the data is subject to BigQuery storage pricing. You are charged for the physical or the logical storage your table consumes including the time travel storage blocks.

Rather than exporting your older data to another storage option (such as Cloud Storage), take advantage of BigQuery long-term storage pricing.

If you have a table that is not edited for 90 consecutive days, the price of storage for that table automatically drops by 50 percent. If you have a partitioned table, each partition is considered separately for eligibility for long-term pricing subject to the same rules as non-partitioned tables.

### Identify long-term or short-term data

Best practice: Identify if row-level data needs to be stored long term, and only store aggregated data long term.

In many cases, details contained in transactional or row-level data are useful in the short term, but are referenced less over the long term. In these situations, you can build aggregation queries to compute and store the metrics associated with this data, and then use table or partition expiration to systematically remove the row-level data. This reduces storage charges while keeping metrics available for long-term consumption.

### Reduce the time travel window

Best practice: Based on your requirement, you can lower the time travel window.

Reducing the time travel days from the default value of seven reduces the total number of storage blocks stored for an object. The time travel window is set at the dataset level.

### Archive data to cloud storage

Best practice: Consider archiving data in Cloud Storage.

You can move data from BigQuery to Cloud Storage based on the business need for archival. As a best practice, consider BigQuery long-term pricing before exporting data out of BigQuery.

## Create and use clustered tables

This document describes how to create and use clustered tables in BigQuery.

### Create clustered tables

You can create a clustered table by using the following methods:

-   Create a table from a query result:
    -   Run a DDL CREATE TABLE AS SELECT statement.
    -   Run a query that creates a clustered destination table.
-   Use a DDL CREATE TABLE statement with a CLUSTER BY clause containing a clustering_column_list.
-   Run the bq command-line tool bq mk command.
-   Make calls to the tables.insert API method.
-   Load data into BigQuery.
-   Use the client libraries.
   
### Table naming

When you create a table in BigQuery, the table name must be unique per dataset. The table name can:

-   Contain characters with a total of up to 1,024 UTF-8 bytes.
-   Contain Unicode characters in category L (letter), M (mark), N (number), Pc (connector, including underscore), Pd (dash), Zs (space). For more information, see General Category.

Caveats:

-   Table names are case-sensitive by default. mytable and MyTable can coexist in the same dataset, unless they are part of a dataset with case-sensitivity turned off.
-   Some table names and table name prefixes are reserved. If you receive an error saying that your table name or prefix is reserved, then select a different name and try again.
-   If you include multiple dot operators (.) in a sequence, the duplicate operators are implicitly stripped.
    -   For example, this: project_name....dataset_name..table_name
    -   Becomes this: project_name.dataset_name.table_name

### Required permissions

To create a table, you need the following IAM permissions:

bigquery.tables.create
bigquery.tables.updateData
bigquery.jobs.create
Additionally, you might require the bigquery.tables.getData permission to access the data that you write to the table.

Each of the following predefined IAM roles includes the permissions that you need in order to create a table:

roles/bigquery.dataEditor
roles/bigquery.dataOwner
roles/bigquery.admin (includes the bigquery.jobs.create permission)
roles/bigquery.user (includes the bigquery.jobs.create permission)
roles/bigquery.jobUser (includes the bigquery.jobs.create permission)
Additionally, if you have the bigquery.datasets.create permission, you can create and update tables in the datasets

### Create an empty clustered table with a schema definition

You specify clustering columns when you create a table in BigQuery. After the table is created, you can modify the clustering columns.

Clustering columns must be top-level, non-repeated columns, and they must be one of the following simple data types:

DATE
BOOLEAN
GEOGRAPHY
INTEGER
NUMERIC
BIGNUMERIC
STRING
TIMESTAMP
RANGE

You can specify up to four clustering columns. When you specify multiple columns, the order of the columns determines how the data is sorted. For example, if the table is clustered by columns a, b and c, the data is sorted in the same order: first by column a, then by column b, and then by column c. As a best practice, place the most frequently filtered or aggregated column first.

The order of your clustering columns also affects query performance and pricing.

To create an empty clustered table with a schema definition:

```
CREATE TABLE mydataset.myclusteredtable
(
  customer_id STRING,
  transaction_amount NUMERIC
)
CLUSTER BY
  customer_id
  OPTIONS (
    description = 'a table clustered by customer_id');
```

### Create a clustered table from a query result

There are two ways to create a clustered table from a query result:

Write the results to a new destination table and specify the clustering columns.
By using a DDL CREATE TABLE AS SELECT statement. 

You can create a clustered table by querying either a partitioned table or a non-partitioned table. You cannot change an existing table to a clustered table by using query results.

When you create a clustered table from a query result, you must use standard SQL. Currently, legacy SQL is not supported for querying clustered tables or for writing query results to clustered tables.

```
CREATE TABLE mydataset.clustered_table
(
  customer_id STRING,
  transaction_amount NUMERIC
)
CLUSTER BY
  customer_id
AS (
  SELECT * FROM mydataset.unclustered_table
);
```

### Create a clustered table when you load data

You can create a clustered table by specifying clustering columns when you load data into a new table. You do not need to create an empty table before loading data into it. You can create the clustered table and load your data at the same time.

To define clustering when defining a load job:

```
LOAD DATA INTO mydataset.mytable
PARTITION BY transaction_date
CLUSTER BY customer_id
  OPTIONS (
    partition_expiration_days = 3)
FROM FILES(
  format = 'AVRO',
  uris = ['gs://bucket/path/file.avro']);
```

## Querying clustered tables

(https://cloud.google.com/bigquery/docs/querying-clustered-tables)

When you create a clustered table in BigQuery, the table data is automatically organized based on the contents of one or more columns in the table's schema. The columns you specify are used to colocate related data. When you cluster a table using multiple columns, the order of columns you specify is important. The order of the specified columns determines the sort order of the data.

To optimize performance when you run queries against clustered tables, use an expression that filters on a clustered column or on multiple clustered columns in the order the clustered columns are specified. Queries that filter on clustered columns generally perform better than queries that filter only on non-clustered columns.

BigQuery sorts the data in a clustered table based on the values in the clustering columns and organizes them into blocks.

When you submit a query that contains a filter on a clustered column, BigQuery uses the clustering information to efficiently determine whether a block contains any data relevant to the query. This allows BigQuery to only scan the relevant blocks — a process referred to as block pruning.

### Best Practices

To get the best performance from queries against clustered tables, use the following best practices.

For context, the sample table used in the best practice examples is a clustered table that is created by using a DDL statement. The DDL statement creates a table named ClusteredSalesData. The table is clustered by the following columns: customer_id, product_id, order_id, in that sort order.

```
CREATE TABLE
  `mydataset.ClusteredSalesData`
PARTITION BY
  DATE(timestamp)
CLUSTER BY
  customer_id,
  product_id,
  order_id AS
SELECT
  *
FROM
  `mydataset.SalesData`
```

### Filter clustered columns by sort order

When you specify a filter, use expressions that filter on the clustered columns in sort order. Sort order is the column order given in the CLUSTER BY clause. To get the benefits of clustering, include all of the clustered columns or a subset of the columns in left-to-right sort order, starting with the first column. For example, if the column sort order is A, B, C, a query that filters on A and B might benefit from clustering, but a query that filters on B and C does not. The ordering of the column names inside the filter expression doesn't affect performance.

The following example queries the ClusteredSalesData clustered table that was created in the preceding example. The query includes a filter expression that filters on customer_id and then on product_id. This query optimizes performance by filtering the clustered columns in sort order—the column order given in the CLUSTER BY clause.

```
SELECT
  SUM(totalSale)
FROM
  `mydataset.ClusteredSalesData`
WHERE
  customer_id = 10000
  AND product_id LIKE 'gcp_analytics%'
```

The following query does not filter the clustered columns in sort order. As a result, the performance of the query is not optimal. This query filters on product_id then on order_id (skipping customer_id).

```
SELECT
  SUM(totalSale)
FROM
  `mydataset.ClusteredSalesData`
WHERE
  product_id LIKE 'gcp_analytics%'
  AND order_id = 20000
```

### Do not use clustered columns in complex filter expressions

If you use a clustered column in a complex filter expression, the performance of the query is not optimized because block pruning cannot be applied.

For example, the following query will not prune blocks because a clustered column—customer_id—is used in a function in the filter expression.

```
SELECT
  SUM(totalSale)
FROM
  `mydataset.ClusteredSalesData`
WHERE
  CAST(customer_id AS STRING) = "10000"
```

To optimize query performance by pruning blocks, use simple filter expressions like the following. In this example, a simple filter is applied to the clustered column—customer_id.
```
SELECT
  SUM(totalSale)
FROM
  `mydataset.ClusteredSalesData`
WHERE
  customer_id = 10000
```

### Do not compare clustered columns to other columns

If a filter expression compares a clustered column to another column (either a clustered column or a non-clustered column), the performance of the query is not optimized because block pruning cannot be applied.

The following query does not prune blocks because the filter expression compares a clustered column—customer_id to another column—order_id.

```
SELECT
  SUM(totalSale)
FROM
  `mydataset.ClusteredSalesData`
WHERE
  customer_id = order_id
```

## Data retention with time travel and fail-safe

(https://cloud.google.com/bigquery/docs/time-travel)

This document describes time travel and fail-safe data retention for datasets. During the time travel and fail-safe periods, data that you have changed or deleted in any table in the dataset continues to be stored in case you need to recover it.

### Time Travel

You can access data from any point within the time travel window, which covers the past seven days by default. Time travel lets you query data that was updated or deleted, restore a table that was deleted, or restore a table that expired.

### Configure the time travel window

You can set the duration of the time travel window, from a minimum of two days to a maximum of seven days. Seven days is the default. You set the time travel window at the dataset level, which then applies to all of the tables within the dataset.

You can configure the time travel window to be longer in cases where it is important to have a longer time to recover updated or deleted data, and to be shorter where it isn't required. Using a shorter time travel window lets you save on storage costs when using the physical storage billing model. These savings don't apply when using the logical storage billing model.

# Read the below tomorrow

## Optimize query computation

(https://cloud.google.com/bigquery/docs/best-practices-performance-compute)

## Best practices for functions

(https://cloud.google.com/bigquery/docs/best-practices-performance-functions)

## Data Engineering in GCP - Part 1 Pub/Sub

(https://medium.com/@subhabrataiam_83312/data-engineering-in-gcp-part-1-pub-sub-3439e6c520e4)

# Sql Interview Questions

normalization, indexing, ANALYZE-EXPLAIN
CTE, Windows functions
Dedupe data
Best Practices
Join and union and cross join

# Hacker rank questions

https://www.hackerrank.com/domains/sql

# Other things

Learn the star method for answering interview questions

# Data Cube Aggregation for big query

https://medium.com/@jianglancao/finally-data-cube-aggregation-can-work-directly-in-google-bigquery-50976305b9ce

# Do this ataclase and bigquery project tomorrow

https://cloud.google.com/blog/products/data-analytics/atscale-and-bigquery-help-modernize-legacy-bi-and-olap-workloads

https://www.youtube.com/watch?v=89GQYR9e1Hc

https://www.youtube.com/watch?v=8iy6hzIS96A

https://www.youtube.com/watch?v=wVYCUs9eiSI

https://www.atscale.com/solutions/atscale-and-google-bigquery/

https://www.atscale.com/resource/how-to-use-atscale-semantic-layer-with-google-bigquery/