# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [HBNB Project - Part 1 - UML](#hbnb-project---part-1---uml)
  - [Date: 03/10/2024](#date-03102024)
    - [Current Task: 0. High-Level Package Diagram](#current-task-0-high-level-package-diagram)
  - [Date: 4/10/2024](#date-4102024)
    - [Current Task: Task 1 and Task 2](#current-task-task-1-and-task-2)
- [HBNB Project - Part 2 - BL and API](#hbnb-project---part-2---bl-and-api)
  - [Date: 21/10/2024](#date-21102024)
    - [Current Task: Everything (implementing business logic)](#current-task-everything-implementing-business-logic)


## Overview

This file holds all the working logs of Arc about this project wuth which part, date and current task on that date

---------

# HBNB Project - Part 1 - UML

## Date: 03/10/2024

### Current Task: 0. High-Level Package Diagram 

***Status:***
- **Task Description:**  Creating the **Package** UML diagram to illustrates the three-layer architecture of the HBnB application and the communication between these layser via the **facade pattern**.

- **Before starting:** After some issues to manages both weekly tasks and the group project, I browsed through all the documentation to acquire a good grasp about UML diagrams and how to build them. For now my knowledge is mainly theorical and I have to put it now in practice. 

***Challenges/Blockers:***
- **Current Challenges:** I stayed a lot on the theorical part and thus, as for each project, the turn between theorical and practical can be difficult and often blocked me a bit.
- **Potential Solutions:** *"Try, die and retry"* Which means really trying to do something, trying to **not** expect it to be perfect already and then reffactore it until satisfaction.

***Notes:***
- **Ideas:** Using Visual paradigm instead of mermaid, more user friendly and visual
- **Questions:** 
- **Reminders:** Stop overthinking.

***To-Do List:***
- [x] Creating a poor draft
- [x] Creating just the bare potential squeleton
- [x] Check with other if on the right track
- [x] Identify the whole "things" I have to put inside
- [x] Refactoring the diagram to something better

---

***Notes during process:***

I needed a lot of time to process my thoughts to actually try the first draft. Even if I already did researches and documentation I felt the need to go further in the specific point of the **layer** structure and **facade pattern**. Once donce, I used an already existing template for basic layered package diagram on Visual Paradigm and changed everything to match my project.

Due to personnal taste, I decided to kinda give a "waterfall" aspect of the whole diagram. Even if it is in **package** format I still organised it to work with the **"starting point"** (`User`) and going down until the **deepest layer** and components (`Data`).

I still have a lot to do, filling each layer and components of these layers with what I already know but I let space to be able to change and adapt.

---

***End of day Log Entry***

***Tasks Completed:***
- [x] Task 0 - Created the package UML I think...

***Progress Summary:***
I thought I had finish the task 0 completly but no. I made the biggest part though which was to understand that squeleton even if it's still a blurred.

***Challenges Encountered:***
- I overthink too much

***Solutions Implemented:***
- Trying to talk to others peers to see if I'm going too far

***Next Steps:***
- Task 1 - Class UML Diagram
- Task 2 - Sequence UML Diagram
- Task 3 - Full documentation (kinda in progress with these logs)

***Notes:***
[Any additional observations, ideas, or things to remember]

-------

## Date: 4/10/2024

### Current Task: Task 1 and Task 2

***Goal for today:***
- [x] Finishing task 0
- [x] Finishing task 1
- [x] Finishing task 2
- [ ] Finishing task 3

***Status:***
- **Task Description:** Design a detail class Diagram gor the Business Logic layer of the HBNB application. And 4 Sequence Diagram to illustrate API call.

- **Before starting:** I reflect a lot about the design of the package layer again. Actually it wasn't over yesterday and finished it today. I thought about specific colors for each layer to be easier to read in the end.

***Challenges/Blockers:***
- **Current Challenges:** Will I have enough time? And I'm not sure to understand everything.
- **Potential Solutions:** I guess it's okay to not understand everything yet. So trying to calm down, just doing something notn perfect instead of blocking to try to do something perfect and not doing anything in the end.

***Notes:***
- **Ideas:** Look for examples on internet, talking with my peers, interrogating A.I to see if I forgot nothing
- **Questions:** /
- **Reminders:** /

***To-Do List for task 1:***
- [x] Taking a simple example of class diagram
- [x] Matching color scheme etc
- [x] Matching format
- [x] Adding attributes and methods
- [x] Adding more according to AI if I didn't forget anything

***To-Do List for task 2:***
- [x] Taking a simple example of class diagram
**abandon/impossible** Matching color scheme etc
**abandon/impossible** Matching format
**abandon/impossible** Adding more according to AI if I didn't forget anything
- [x] Keep the simplest possible

***To-Do List for task 3:***
**abandon/impossible** Delegating to Esteban to take a look
- [x] Keeping my own logs in these files
---

***During process notes***

- I actually had to work again on the package diagram, I put colored and notes to explain every layer. I think it's great like this be will need to be refactored at some point I guess? The colors helps for the following process since we can see in one glance in which layer we are even if the diagram isn't the same type (class, sequence, package).

- It's a bit easier than the task 0 since I kinda already know what there is inside this time. But I don't lie that regarding the short time for various reasons, I work along A.I like everyone else. They helpes me to understand the assignement and check if I didn't forget anything.

- My **real** goal for today is to provide something, either it's imperfect I have to provide something. To be more `AGILE`.

- I finally understand what to put in the classes. I stopped thinking like *"I need classes, I need methods"* and thought about "okay I'm on this site, as a user what can I do?" and so that's how I filled the classes better. Same for methods. Now I have to link them and add some notes and should be good to go to task 2  

- Not that easily in the end, I managed to fill quite well each class I think and added notes but I struggles with relationships. 

- I just understood now the use and principle of "BaseModel". So I'm updating the whole thing with it.

- One last thing with task 1 : Relationships and **Multiplicity** which is difficult to create

- It is time. I already sent what I had I'm just updating the last log. I won't lie, for the task 2 I needed an A.I to provide me a basemodel. Not that I wouldn't have understand how to do it by myself but I was lacking time. Lot of time. I had to do everything by myself while hoping until the very end that I would have help from my teammate. That's why the sequence API calls are less refined than the others.
---

***End of day Log Entry***

***Tasks Completed:***
- [x] Task 1: class diagram
- [x] Task 2: Sequence Diagrams
**abandon/impossible** Task 3: Full documentation

***Progress Summary:***
To sum up real quick caus I don't have enough time, I managed to finish a refine class diagram for the task 1. Very polished I think. I thought I wouldn't have enough time to do at least the diagram for task 2 but with some AI help I could. It provided me the base model and then I did the rest of it. But I did it with mermaid instead of Visual Paradigm because it was easier to do actually than what I thought. Visual Paradigm is beautiful but take a LOT of time actually. Mermaid is more direct. Will use it next time.

***Challenges Encountered:***
- I can't count on my teammate.
- I had to do everything alone since my teammate told me he was working on something but didn't
- Rushed things at the end

***Solutions Implemented:***
- Improvise and use A.I as partner instead.

***Next Steps:***
- [ ] [Next task to be worked on]
- [ ] [Another upcoming task]

***Notes:***
I'm exhausted and drained. Time has ran out and I'm over now. I sent at least the 4 diagrams.

---------

# HBNB Project - Part 2 - BL and API

## Date: 21/10/2024

### Current Task: Everything (implementing business logic)

***Status:***
- **Task Description:** Creating the full business logic with each entities and relations between them

- **Before starting:** I already did the task 0 which was creating the overall structure with placeholder given by the project repository. Since I have to redo everything alone.

***Challenges/Blockers:***
- **Current Challenges:** I have to do everything what needed to be done in group, alone once again and in a very short amount of time, once again.
- **Potential Solutions:** Using AI for helps, supervisors already know about that.

***Notes***
- **Ideas:** I will try to be ass logical as possible and work  as fast as possible with AI helps BUT understanding what I'm doing and implementing. Not just bare mindless copy-pasting.
- **Questions:**
- **Reminders:** In the "To-Do List" under that section, I tried to be concise but in the end I'm not sure if it will follow what I have exactly to do. 

***To-Do List:
- [x] Create the overall structure
- [ ] Create a Base Model
- [ ] Create each class (Users, Places, Reviews, Amenities)
- [ ] Create methods for Users
- [ ] Create methods for Places
- [ ] Create methods for Reviews
- [ ] Create methods for Amenities
- [ ] Create Relationships between each of them ?

---

***During process notes***

---

***End of day Log Entry***

***Tasks Completed:***
- [x] Task 0: Creating the overall structure
- [ ] Task 2: [Brief description]
- [ ] Task 3: [Brief description]

***Progress Summary:***
[Provide a brief overview of what was accomplished today]

***Challenges Encountered:***
- [Challenge 1]
- [Challenge 2]

***Solutions Implemented:***
- [Solution for Challenge 1]
- [Solution for Challenge 2]

***Next Steps:***
- [ ] [Next task to be worked on]
- [ ] [Another upcoming task]

***Notes:***
[Any additional observations, ideas, or things to remember]

---------