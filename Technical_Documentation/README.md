# HBNB Project

## Introduction

This repository contains the HBNB (Holberton Bed and Breakfast) project, a school assignment designed to demonstrate proficiency in software architecture, design principles, and Object-Oriented Programming (OOP) using Python.

## Project Overview

The HBNB project aims to create a simplified Airbnb-like application. It involves designing and implementing a system that manages various entities such as Users, Places, Reviews, and Amenities.

## Structure

### High-Level Architecture
The project follows a three-layer architecture:
- **Presentation Layer**: Handles user interactions and exposes APIs.
- **Business Logic Layer**: Contains the core business logic and models for the system.
- **Persistence Layer**: Responsible for data storage and retrieval.

### Key Components
- **Users**: Represents the users of the system.
- **Places**: Represents the places listed on the platform.
- **Reviews**: Represents the reviews left by users for places.
- **Amenities**: Represents the amenities available at places.

## Installation and Usage

### Installation
To set up the project, follow these steps:
```bash
git clone https://github.com/your-username/hbnb.git
cd hbnb
```

### Usage
- **API Endpoints**: Detailed documentation on how to use the API endpoints will be provided in the API section.
- **Running the Application**: Instructions on how to run the application will be included in the `README.md` of the relevant subdirectories.

## UML Diagrams

### Package Diagram for the whole Layered Architecture

- ![High-Level Package Diagram](https://media.discordapp.net/attachments/385020139839422464/1291886352366964799/Package_Diagram__HBNB.png?ex=6701ba6c&is=670068ec&hm=fe40ca035cf7794fbf819a0d63542cd466dfabf07b6b5f786c139616a9765e53&=&format=webp&quality=lossless&width=711&height=994)
  - Describes the overall architecture and dependencies.

### Class Diagram of the Business Layer


- ![Detailed Class Diagram](https://media.discordapp.net/attachments/385020139839422464/1291886349322027028/Class_Diagram_-_Business_Layer__HBNB.png?ex=6701ba6b&is=670068eb&hm=4a8ae0ee5d8705bc82741103b0778b195e24fcb43f356d42908f5c0a38da1b3c&=&format=webp&quality=lossless&width=778&height=994)
  - Shows the classes, attributes, methods, and relationships.
  
### Four sequences Diagram of prensetation Layer

#### API Call: User Registration

- ![Sequence Diagrams - User Registration](https://media.discordapp.net/attachments/385020139839422464/1291886351968370768/HBNB__Sequence_Diagram_-_API_Call_-_User-_Registration.png?ex=6701ba6c&is=670068ec&hm=56d3effd49ce76a47a6a511a6181e294d22bf325445bb5fa1fb06ec13212d474&=&format=webp&quality=lossless&width=1164&height=513)

#### API Call: Place Creation

- ![Sequence Diagrams - Place Creation](https://media.discordapp.net/attachments/385020139839422464/1291886350387122249/HBNB__Sequence_-_API_Call_-_Place_Creation.png?ex=6701ba6c&is=670068ec&hm=263b0f9e2f72cbaaea86dd7a24d7c5e540ae378ffde948427724b7817e568bbd&=&format=webp&quality=lossless&width=1164&height=504)
  
#### API Call: Submit Review

- ![Sequence Diagrams - Submit Review](https://media.discordapp.net/attachments/385020139839422464/1291886351268188180/HBNB__Sequence_-_API_Call_-_Review_Submission-.png?ex=6701ba6c&is=670068ec&hm=6a8444f8ae2232c2fb3c6a724cad8bb12b2028dcb76843bda4300d124ab11960&=&format=webp&quality=lossless&width=1164&height=485)

#### API Call: Fetching a list of Places

- ![Sequence Diagrams - Fetching a List of Places](https://media.discordapp.net/attachments/385020139839422464/1291886349850513630/HBNB___Sequence__API_Call_Fetching_a_List.png?ex=6701ba6b&is=670068eb&hm=77b9aa6ad5b1e01a3ac37a6a97ab8a4fda315655e8c09f084a37157411fae629&=&format=webp&quality=lossless&width=1164&height=463)
  - Illustrates the interaction flow for key API calls.

### Explanatory Notes
Each diagrams are either accompany with notes or documented in the Logs.

## Contributions

No contributor.

## Author

- [Arc](https://github.com/ArcturusSky)