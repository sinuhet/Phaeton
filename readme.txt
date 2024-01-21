# Project Phaeton

## Overview
Project Phaeton is a sophisticated system for controlling RGBW LED strips through a web interface. The system utilizes ESP-32 devices to manage the lighting, offering users the ability to adjust the color and intensity of the lights remotely. Each ESP-32 device controls 2 RGBW LED strips, utilizing a total of 8 PWM channels.

## System Components

1. **ESP-32 Devices**:
   - Connect to a WiFi network for seamless communication with the central server.
   - Set up as a WiFi hotspot initially for configuration purposes.
   - Authenticate with the server using unique IDs and authentication tokens.
   - Manage 8 PWM channels to control the colors and brightness of the RGBW LED strips.
   - Receive and process instructions from the server to adjust the lighting.

2. **Central Server (Linux with Python Backend)**:
   - A user-friendly web interface for account management and device configuration.
   - PostgreSQL database integration for storing user data and device configurations.
   - RESTful API for facilitating communication between the web interface, ESP-32 devices, and the server.
   - Emphasis on data security with encrypted communication channels.

3. **Web Interface (HTML/JavaScript Frontend)**:
   - Allows users to register, log in, and manage their ESP-32 devices.
   - Enables the addition, naming, configuration, and removal of devices linked to user accounts.
   - Provides an interactive control panel for adjusting the RGB values and white light intensity of the LED strips.

4. **Security and Authentication**:
   - Ensures that only authorized users can access and control their devices.
   - Secure communication between the server and ESP-32 devices to prevent unauthorized access.

5. **Database**:
   - User Model: Stores essential information about users and their access credentials.
   - Device Model: Maintains detailed records of each ESP-32 device, including its current state and configuration details.

## Setup and Configuration

1. **ESP-32 Device Setup**:
   - Follow the instructions provided in the ESP-32 documentation to connect the device to the WiFi network and set it up for first-time use.

2. **Server Setup**:
   - Install and configure the Linux operating system on your server.
   - Set up the PostgreSQL database and create the necessary tables as per the schema.
   - Deploy the Python Flask application and ensure it's running correctly.

3. **Web Interface Access**:
   - Access the web interface through a browser by navigating to the server's IP address or domain name.
   - Register for a new account and log in to start managing your ESP-32 devices and LED strips.

## Future Enhancements

- Addition of a mobile application for more convenient control.
- Integration of more advanced lighting effects and scheduling features.
- Implementation of user-defined lighting scenes and moods.

For detailed instructions, troubleshooting, and further development, refer to the individual documentation sections for each component.

Thank you for choosing Project Phaeton for your smart lighting needs!
