# Claude Code Setup, Intro to Context & Tokens

## Claude Code Install & Basic Usage (Python Example)
- You can make a directory (you can or claude can), then you use the `Claude` command 
- When referencing a file, you use the `@` symbol which is an alias 
  - We will dive into aliases more later

## Plan Mode
- Plan mode makes it so you can develop a plan into a markdown file 
  - Great for thinking of new things to add 
- It will give you options to implement and it shows you the amount of tokens it's using
  - Also make sure you check whether or not it changed from plan mode, back to accept edits 

## Slash Commands, Config & Settings File
![Claude Code Commands](./images/Diagram%203-4%20-%20Claude%20Code%20Commands.png)
- `/model` to change your model 
  - Sonnet is not as good as Opus 
- You can use think harder and ultra think, but these use more tokens 
- Settings File 
  - Personal Project Scoped 
    - `PROJECT_FOLDER./.claude/settings.local.json`
  - Project Scoped 
    - `PROJECT_FOLDER./.claude/settings.json`
  - User/Global Scoped 
    - ~/.claude/settings.json
  - What goes in these files? 
    - Permissions 
    - MCP Server Settings
    - Hooks (Automated Bash Scripts)
    - Model PReferences 
    - API Config 
    - Disabled Tools 

## Intro To Context & Tokens
![What Is Context?](./images/Diagram%203-5%20-%20Context%20&%20Tokens.png)
- Context 
  - Everything the AI can see and remember at any given moment 
  - Example: think of the movie 50 First Dates 
- Context Window -> what it can hold in memory at once 
- Context Engineering -> feeding the AI the right information so it can actually help you 
  - We can automate a lot of this, this is what the `CLAUDE.md` file is for 
- Tokens -> how context windows and API pricing are measured
  - With subscriptions you don't have to worry about tokens
  - If you're using it in a project, you have to pay for tokens and will have to use API pricing 

## Context-Related Slash Commands
- Type in `/context` 
- `/clear` -> clears the context 
- The context screen 
  - System Prompt - baked in by Claude, you can't change these 
  - System tools - the capabilities for claude code to read and write to files 
- It takes up more context if you don't reference the file 
- Go feature by feature and then clear the context and then when you're done clear it 
- There are two ways to handle context you can **clear** or **compact** it 
  - Compact isn't recommended as of now, just go feature by feature and then clear when you're done 

## Update: Memory File
- When you ask Claude to remember something now, it will save it in persistent memory 
  - So the behavior is different than the last video 
