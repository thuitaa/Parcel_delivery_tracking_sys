# SwiftRoute: Parcel Delivery Tracking System

A custom-built Parcel Delivery Tracking System developed for the Data Structures & Algorithms CAT 2 Project at Strathmore University. This application demonstrates the manual implementation of core data structures and algorithms without relying on built-in language libraries.

## Project Overview
SwiftRoute is a web-based management tool designed to streamline parcel tracking and prioritize delivery logistics. The system allows administrators to register parcels, track their status, and manage a delivery queue using manual implementations of hash maps and linked structures.

## Data Structures & Algorithms Implemented
In compliance with the project requirements, we have manually implemented:

### Data Structures
- **Custom Hash Map (with Chaining):** Used for O(1) average-time complexity tracking of parcels via unique IDs. Collision handling is implemented using linked list chaining.
- **Linked-List Queue:** Used to manage the FIFO (First-In, First-Out) delivery dispatch process efficiently.

### Algorithms
- **Quick Sort:** Used to re-order the delivery queue based on priority levels ($O(n \log n)$ time complexity).
- **Linear Search:** Used for filtering and querying the parcel database by attributes such as Customer Name or Destination City ($O(n)$ time complexity).

## System Architecture
The project follows a modular design to separate UI from logic:
1. `structures.py`: Contains custom data structure classes.
2. `backend.py`: Contains the `TrackingSystem` controller and algorithm implementations.
3. `app.py`: Provides the interactive Web UI (built with Streamlit).

## Features
- **Parcel Registration:** Log new parcels with tracking IDs and priority levels.
- **Instant Tracking:** O(1) lookup of parcel status by ID.
- **Priority Management:** Sort pending deliveries by urgency.
- **Dispatch Processing:** FIFO-based delivery handling.

## How to Run
1. Ensure you have Python installed.
2. Install the required dependency:
   ```bash
   pip install streamlit
