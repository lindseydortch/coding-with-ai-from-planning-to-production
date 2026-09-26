# Database Integration & Initial Deployment (CI/CD Setup)

## Neon PostgreSQL Database Setup
- Neon - They offer branching - you can branch your databases
  - The free account is very generous 

## Prisma 7 Setup
- Prisma 
  - Tool to interact with your database 
  - An Object Relational Mapper (ORM) for Node.js and TypeScript 
    - Instead of writing raw SQL queries in our application we use Prisma to interact with our database using TypeScript methods 
    - Gives us type safety, autocompletion, in our IDE, mirgrations (version control for your database), prisma studio (directly access your data)
- When this course was released, the data for the models was probably trained on Prisma 6, so we have to specify to have it look into Prisma 7 

## Initial Database Migration
- Make sure you always specify newer docs, but we will go over using an MCP called Context 7, that will get us the latest docs 
- In Neon we have a migrations table, so any migrations we run will show up there 

## Seed Sample Data
- Make sure to have Claude test the data 
- Work with the AI for any errors you get 

## Populate Dashboard Collections
- We got the database to display our dashboard collections

## Populate Dashboard Items
- Set up the database population for our dashboard items 

## Populate Stats & Sidebar
- We could have had one spec file for everything. But it's better to do things in chunks. 
  - It takes its time and yours to really make sure the feature is being implemented correctly 
- Don't forget to clear your context before you start a new feature 
- We will go back and create an agent that reviews our code in the future 

## Migration Workflow Overview
![Database Migrations Workflow](./images/Diagram%206-8%20-%20Prisma%20Migrations%20Workflow.png)
- We have to make sure our databases for development and production are in sync 

## Initial Deployment & Prod Migration
- We have a different database for dev and production 
- You can add the repo for the project to build 
  - You have to add in the migrations before the build command
  - You can ask Claude to `Can you give me SQL queries to add the system item types and the demo user to the prod db?`
    - Then you can paste this into the SQL editor and then we will see all our demo item types in there 
    - When you change the database you still need to redeploy 
