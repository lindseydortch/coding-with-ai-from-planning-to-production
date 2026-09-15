# Vibe Coding For Prototyping

## Intro To Prototyping
- Why Prototype? 
  - Validate the concept 
  - Test UI/UX Before Building 
  - Share Vision with Team 
- Tools for Prototyping 
  - Lovable 
  - V0
  - Bolt 
- Idea/Vision -> Prototype (v0, Bolt) -> Validate/Iterate -> Build Properly (Claude, Cursor, Manual)
- You don't need a subscription for prototyping, you should be able to get by on the free tiers 

## Writing Good Prompts
![Writing Good Prompts Notes](./images/Diagram%202-2%20-%20Writing%20Good%20Prompts.png)
- The quality you get from an AI tool is based off of the quality of your prompt 
- It's not recommended to one shot applications, even with prototyping 
- When prototyping it's okay to use localStorage instead of setting up a database 
- It's important to add inspiration of other UI's you like 
- What makes a good prompt: 
  - Specific features listed 
  - Technical Stack defined 
  - UI expectations set 
  - Gives design reference point 
- You're the architect and AI is the builder 

## Prompt Assignment
- We'll practice writing a prompt using the principles covered in the last video 

## Prototyping In Action
- In the course repo under prompts there is a `General Prototype Prompt` that we can copy and use for features, etc. 

## Quick Prototype Code Review
![What To Look At In Generated Code](./images/Diagram%202-5%20-%20Prototype%20Code%20Review.png)
- AI loves Next and Tailwind, if you have it create an app it will most likely include these two 
- A note with Next.js codewise 
  - It's using a ton of `use client` cases everywhere 
  - You can specify in the context to use SSR 
- You don't want to just generate applications and not know what is going on 

## Iterating On The Prompt
- Went through and added different features to improve the app 

## Reality Check - Prototype vs Production
![Technical Debt](./images/Diagram%202-7%20-%20Prototype%20vs%20Reality.png)
- AI optimizes for the happy path, so error and loading states are often missing 
