# HomeAutomation
Code for a centralized webserver and correlating services hosted on Raspberry Pi devices.

The purpose of this project is to provide a way to manage multiple projects from a few devices in a centralized manner, creating the ability for a wide variety and scope of individual projects to be interfaced with in a unifed manner.

System Overview:
Series of multiple Docker Containers hosted on Raspberry Pi devices, including
1. FastAPI Python Container which contains the Web Server running on the central Raspberry Pi Zero 2 W. This will serve as the central API end-points for the project.
2. Frontend Container, which connects to the FastAPI end-points to produce a Dashboard containing a log of the commands issued, status of the boards, and other information.
3. Postgre SQL database for Raspberry Pi Pico W sensor readings and measurements.
4. Additional database for storing logs of issued commands and messages.

Additionally, non containerized microcontrollers which are equipped with several sensors can be added into the system. Current microcontrollers include:
1. Pico 1, which contains a temperature and air moisture sensor. This Pi will be utilized to collect data about the probability of dangerous road conditions.
2. Pico 2, which is equipped with a vibration sensor. This will be attached to Laundry Machines, and will send a text when laundry is completed.
3. Pico 3, which will be solder'ed into light fixtures to automate room lighting from the console.

Future Plans:
1. Method of automatically adding new Pi Projects via the central console.
2. Having select features of the console available outside of the LAN environment.
3. Increased management ability for individual devices, including battery status and further error checking.
