---
title: "标题"
source: "https://x.com/PrajwalTomar_/status/1912513810575097900/?rw_tt_thread=True"
author:
  - "[[@PrajwalTomar_]]"
created: 2025-04-17
description:
tags:
  - "@PrajwalTomar_ #标签"
---
**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513810575097900)

How to Set Up Cursor the Right Way

Cursor Rules are outdated. Project Rules is the correct way now.

Here’s why it matters and how to set it up properly:


1\. Why .cursorrules wasn’t enough

Cursor originally used a single .cursorrules file at the root of a project, but this approach had serious problems:

Limited control

→ One rules file applied to the entire project, even when irrelevant.

Context overload

→ Cursor had to


2\. Introducing Cursor’s Project Rules (.mdc files)

Cursor solved all of this by introducing Project Rules, stored as modular .mdc files inside .cursor/rules/.

This lets you apply rules per file type, module, or feature, not one giant file.

Why Project Rules are better:


3\. Step-by-step setup

Here’s how to set up Project Rules the right way:


Step 1: General Rules (general.mdc)

This rule applies to all files across the project.

Scope: \* (all files)

Contents:

\- Use TypeScript for all development.

\- Prioritize readability and maintainability.

\- Use clear, descriptive names.

\- Add meaningful comments for complex

![Image](https://pbs.twimg.com/media/GoqYOvdWkAAxZcE?format=png&name=large)


Step 2: Frontend Rules (frontend.mdc)

These rules apply only to frontend files (.tsx).

Scope: \*.tsx (React components)

Contents:

\- Use functional React components.

\- Apply Tailwind CSS; avoid inline styles.

\- Components should be modular and reusable.

\- Maintain a consistent

![Image](https://pbs.twimg.com/media/GoqYSkEWgAAWOaH?format=png&name=large)


Step 3: Backend Rules (backend.mdc)

These rules apply only to backend logic (.ts API and database files).

Scope: api/\*\*/\*.ts (all backend API files)

Contents:

\- Always validate API inputs.

\- Use async/await consistently.

\- Follow RESTful conventions.

\- Optimize queries for

4\. What changed at my agency

Switching to Project Rules had a real impact:

Fewer AI mistakes

→ Cursor follows scoped rules more accurately.

No more repetitive corrections

→ AI remembers your standards and applies them automatically.

Cleaner, more consistent code

→ Everyone


5\. Best practices for Project Rules

To get the most out of .mdc:

Keep rules modular:

\- Separate frontend, backend, and database logic.

Use precise scopes:

\- .tsx → React components

\- api/\*\*/\*.ts → Backend APIs

\- \*/\*.sql → SQL queries

Regularly refine rules:

\- If a rule is


6\. Final Takeaway: Project Rules Are a Game-Changer

Cursor’s Project Rules provide a massive improvement over .cursorrules:

\- AI-generated code is more accurate and follows best practices.

\- Rules are easier to manage, update, and scale across projects.

\- Less time spent fixing


Cursor isn’t just an AI-powered IDE, it’s a tool that adapts to your coding standards when set up correctly.

If you’re still using .cursorrules, you’re limiting Cursor’s potential.

Start using Project Rules today and take full control of AI-generated code.

Any questions? Let’s