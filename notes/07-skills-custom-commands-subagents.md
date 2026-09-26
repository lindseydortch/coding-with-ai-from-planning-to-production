# Skills, Custom Commands & Subagents

## Skills & Custom Commands Explained
- If you're using Claude or Cursor, they will also have this same feature, but the steps to create it might be a little different 
  - Then ask the tool or go through the docs to set up to the respective tool 
- Custom slash commands have been turned into skills 
- Skills and Custom Slash Commands 
  - Custom commands and skills have recently been merged but you can still use either convention 
    - It is suggested to use skills over slash commands 
    - Slash command: executable by user 
      - `/<command-name>[arguments]`
    - Skill: executable by user OR agent 
      - `/<skill-name>[arguments]`
  - Where they live 
    - Project Based 
      - `[project_folder]/.claude/commands/[command-name.md]`
      - `[project_folder]/.claude/skills/[command-name.md]/SKILL.md`
    - Personal 
      - `~/.claude/commands/[command-name].md`
      - `~/.claude/skills/[command-name]/SKILL.md`
    - Basic File Structure 
      <code>
        ---
        name: NAME
        description: DESCRIPTION
        ---

        Your prompt telling what the skill/command should do
      </code>
- Now most of the time we're just dealing with markdown files 
- To see an example of a skill we're creating, see `projects/devstash/.claude/commands/list-components.md`
- Your `argument-hint` needs to be in a string, this is different from the Github repo 

## Feature Command/Skill Actions
![Let's automate our workflow with a new command](./images/Diagram%207-2%20-%20Feature%20Command.png)
- From video comments: 
  - TODO: come back to this comment once I finish the course and start building projects
  - "I've been using Matt Pocock's `grill-me`, `write-a-prd`, and `prd-to-plan` skills to create the detailed plans, then feeding that to your `/feature` skills for the past week, and holy cow...this is the AHA workflow that's been missing every other time I've tried using AI."
- This is not something you have to include, but this helps us start to be more specific with strict commands that tells it exactly what to do 
- ![Updated Workflow With Features](./images/Diagram%207-2%20-%20AI%20Workflow%202.png)

## Create The Feature Command/Skill
- Give the AI a gist of what you're looking for and it will help you make these files for you 
- To use AI well and not just vibe code, you'll be working with markdown a lot because you have to have good documentation 
- You can have a `SKILL.md` file and then point to the different actions 
  - You can have an `/actions` folder for the task to do after the `/feature` command 

## Use The Feature Command
- Set up a small feature for use to test out our skills on 

## Cleanup Command
- We want a command for cleanup and necessary tasks 

## What Are Subagents?
![what are subagents?](./images/Diagram%207-6%20-%20What%20Are%20Subagents.png)
- Subagents - AI assitants that can be invoked to handle specific types of tasks 
  - If you're using other agents besides claude code, they have them as well, just ask what the equivalent to Claude Code subagents is 
- Your main agents and subagents don't share memory 
- Subagents are good for reviews, ui (improve for clickthrough rates)
  - plan -> used to conduct research and gather info about your codebase before presenting a plan 
- You can create custom subagents 
- Commands vs agents 
  - Commands 
    - Quick, repeatable task 
    - Workflow automation 
    - Same steps every time 
    - `/feature start`
  - Use an agent 
    - Deep exploration 
    - Autonomous analysis 
    - Needs to search and think 
    - "Scan entire codebase"
      - You don't want to do this with your main agent to preserve context 

## Create The Code Scanner Subagent
- Keep in mind: A lot of the time it will give you false positives, it will tell you things you haven't implemented yet 
- The agents command has been removed 
  - Created it with the following command `Create a code-scanner agent: 
      Scan this Next.js codebase for:
    - Security issues
    - Performance problems
    - Code quality
    - Code that can be broken up into seperate files/components

    Only report actual issues. DO NOT report things that are not implemented yet. If there is no authentication, don't report as an issue.

    Report findings grouped by severity (critical, high, medium, low) with file paths, line numbers, and suggested fixes.

    The .env file is in the .gitignore. You always seem to report that it is not. Be aware of that.`
- From the class comments 
  - Q: "If the codebase is big, would it make sense to have different subagents review different parts of the code (so that they don't run out of context)? Each subagent can review one part of the code, and a different subagent could also check the integration between the different parts of the code. Just thinking out loud, haven't done this yet myself."
    - A: "And yes that's a good approach. Splitting a large codebase across subagents can keep each review focused and avoids context limits, while a separate integration review helps catch issues that span multiple modules."

## Using The Code Scanner
- `Use the code-scanner subagent to check the entire codebase and report your findings` - prompt to use the subagent 
