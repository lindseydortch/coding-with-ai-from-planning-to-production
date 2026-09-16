# Planning & Context Files

## Planning A Project
![Planning a Project](./images/Diagram%204-1%20-%20Planning%20A%20Project.png)
- You need to carefully map out and build what we want by creating a strict workflow and planning 
  - Planning will take more time than it used to 
  - Planning is very important when working with AI 
- There's a project spec document, you can have AI create this for you

## Bootstrap Your Files Manually
- Don't use AI for the hell of it, use it because for things you want to save time on 
- Clean up Next.js boilerplate prompt: 
  - `I have a fresh install of next.js and I want you to
  clean up the boilerplate. The @src/app/page.tsx should simply show an h1 with the text
  Devstash` 

## CLAUDE.md & Project Context
- Every agentic AI tool has a there own type of file to be loaded for context 
  - Anything you want to be known throughout the session 
- You can have a context folder and then point to these files from the `CLAUDE.md` 
- `/init` will create the `CLAUDE.md` for you 
![Initial Context Files](./images/Diagram%204-3%20-%20Initial%20Context%20Files.png)
- Take our project spec and put it into Claude chat using the following prompt: 
  - `I am building a Saas called DevStash. Below are my planning notes. Review and clean up as you see fit. Formate with things like Prisma models, diagrams, icons, links and any other info that you think is relevant. Put it in a file called project-overview.md`

## Coding Standards & Interaction Rules
- When you're coding with AI, you have to construct documentation, rules and context so the AI knows how to write your code 
- You can reuse these contexts from `https://cursor.directory/`

## AI Workflow & Current Feature File
![AI Workflow](./images/Diagram%207-2%20-%20AI%20Workflow%202.png)