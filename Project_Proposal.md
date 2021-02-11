## Eye Tracking Match GameGUI
Team: Sam Aba, Chandler Brooks, Heather Haynie, Matthew Scarfo

### Introduction
The objective of the project is to create an interface that creates a fun user
matching game, while also aiding in data collection. To collect data pre-existing
hardware would be utilized to capture the user's pose and eye positional data.
This data can then be used later as a database for other projects.
The motivation for the project came about, not necessarily for the project itself,
but rather the future projects that can be built using the collected data set.
Future projects could include using the collected data to perform pose and eye
tracking estimation to create accessible browser tools or detecting potential
eye strain in computer users.

Considering similar products on the market, the interface to be created would
resemble already existing software due to the simple matching game interface.
The combination of game and such data collection is, however, a unique concept
for software to the knowledge of the team.

Approaching the project, the team has a variety of backgrounds including one
member in computer science, one in electrical engineering, and two in computer
engineering. Each of the members have some experience in Python, and a few have
further experience with a variety of Python libraries and machine learning.

### Customer Value
The primary customers for this product are users with disabilities and users
who prefer this technology. The customers want a game/software that can
track their eyes to control a cursor on the screen. The want for this product is to
provide an alternative option for those who are motor impaired who have to turn
to sometimes fairly expensive market alternatives in order to obtain the same
effective, hands-free operation.

Tobii is a similar market name product that can be very expensive, so our design
 is cost-efficient and available to the general public. This will give customers
 access to software to use their devices hands free and make their lives easier
 while dealing with technology. Further, the technology will be implemented on open source software, making it easily
 modifiable and significantly cheaper than anything on the market.

Though this idea has already been tested and sold by Tobii, a design that is
available across many platforms and available to the public would be a major
improvement. A successful implementation will provide the customer with
intelligent software to control a cursor with their eyes. Specific customer-centric
measures of success would include accessibility, ease of use, and usefulness.

### Technology
Data from the camera will be read in and analyzed using python libraries like
Pandas. On the front-end a GUI will be created such that we can use this data to
to click a square on a simple matching games. The application is a matching game
 that uses eye-tracking software to control the cursor. The game also tracks
 data using machine learning to analyze eye movements op potential eye strain
 due to prolonged screen activity.

 ![A generic overview of what our team hopes to accomplish. Depending on the
 progress made throughout the semester, this approach may be modified to implement
 other uses of the eye-tracking technology.](Block_Diagram "Diagram")

 A minimal system that has some value to the customer would be an eye-tracking/
 monitoring system that potentially detects symptoms of eye-strain and notifies
 the user when it's a good idea to take a break or turn down the brightness on
 the screen. Implementations of the cursor throughout multiple applications,
 customizable cursor settings for cursor speed, clicking, and scrolling are a
 few examples of possible enhancements that customers would value. The testing
 of the system will be performed by setting milestones and modifying the approach
 as the project is completed. The project will be implemented by using pre-existing
 Python libraries, like Pandas, PyAutoGUI, and PySimpleGUI, to help with the
 development process of the project.

 ### Team
 A few members of the team have prior experience with machine learning and
 development of graphical user interfaces. The team is all familiar with Python
 and half have experience with machine learning. Though, it will be a new experience
 for all of the team using machine learning together with GUI development.

###### Roles:
* Sam Aba - Camera Integration Lead
* Chandler Brooks - Code Implementation, Debugging
* Heather Haynie - General Discussion, Code Implementation, Preliminary Reasearch
* Matthew Scarfo - General Discussion, Code Implementation

Rotating the roles will be determined by the progress of team meetings.

### Project Management
The completion of the system will be feasible. Progress will be monitored through
 online meetings held once a week on Mondays.

###### Schedule:
| Week         | Task |
|--------------|-------------------------------------|
| Feb 8 - 12   | Finish proposal, research libraries |
| Feb 15 - 19  | Create rudimentary GUI |
| Feb 22 - 26  | Software development and implementation |
| Mar 1 - 5    | Submit status report 1 |
| Mar 8 - 12   | Implement camera |
| Mar 15 - 19  | Submit status report 2 |
| Mar 22 - 26  | Work on final design and debug GUI |
| Mar 29 - April 2 | Submit status report 3 |

###### Constraints and Resources:
There are currently no known constraints for the system. Data will be collected
using machine learning. Online resources will be crucial to guide our implementation.
The project can approach different solutions depending on progress made and
time constraints. Successful implementation of the eye-tracking software will
determine the functionality of our project. Usefulness depends on the final
design and GUI.
