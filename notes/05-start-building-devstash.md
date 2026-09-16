# Start Building DevStash

## Using Git With AI
- When you're building with claude code you typically don't have to run your Git commands 

## Dashboard UI Prototype
- We can follow along with whatever v0 outputs for us or we can use the screenshots provided in the course repo 
  - Decided to utilize Brad's screenshots because there was some issue with the v0 output on my end 

## Claude VS Code Extension
- Works pretty much the same way as the terminal
  - But with the caveat sometimes not all of the commands are available 

## Generating Mock Data
- The prompt used to generate mock data: 
  ```We need a single source of truth for mock data to use for the dashboard UI until we implement a database. Read @context/project-overview.md and look at @context/screenshots/dashboard-ui-main.png to see the data structure. 
  
  Create a new file at src/lib/mock-data.ts and create a simple data structure for the dashboard UI. It should include items, collections, item types and a user for the current logged in user. Do not make this too complex. It is only for displaying data in the dashboard like the screenshot. Do not create helper methods, just a simple data file to import.```
- It's suggested after we make changes to push to git because when we add features in the next video, it's going to merge it into main 

## Dashboard UI Phase 1 & Spec Files
- Create a spec file which is a list of requirements for a specific feature and then tell AI to update that feature 
- As long as it works you're fine, just try to iterate, which you might have to 
  - It's all about learning the workflow 
- You can find the spec files in the code repo under context 

## Dashboard UI Phase 2 - Sidebar
- Running the create feature for Phase 2 of the Dashboard 

## Dashboard UI Phase 3 - Main Area
- Running the create feature for Phase 3 of the Dashboard 
