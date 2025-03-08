# IZTECH Design101 Project - NetAnaliz AI

## Project Overview
NetAnaliz AI is an intelligent application designed to assist users experiencing internet connectivity issues. When users contact their Internet Service Provider's (ISP) Customer Service, NetAnaliz AI performs an immediate and comprehensive analysis of various data sources—including connection contexts, logs, and other relevant technical information—to quickly identify the issue and provide actionable solutions.

## How It Works
When the user calls Customer Service:

1. **Data Collection and Analysis**
    - Collects context information, system logs, ISP maintenance records, and relevant external data.
    - Rapidly analyzes the gathered data using a state-of-the-art Large Language Model (LLM)—specifically, GPT-4 Turbo.

2. **Issue Identification**
    - Summarizes the user's current connectivity situation clearly and concisely.
    - Generates a reasoned prediction regarding the nature of the issue based on the data analysis.

3. **Solution Recommendation**
    - Provides practical and understandable solutions to the Customer Service Agent, which can be clearly communicated to the user.
    - Assists the agent in opening a detailed and accurate support ticket, forwarding the issue efficiently to the Technical Department if further assistance is required.

## Advantages of Using NetAnaliz AI
- **Rapid, Comprehensive Analysis**: Performs detailed analysis in seconds, significantly faster than human agents could.
- **Complex Reasoning**: Leverages GPT-4 Turbo's advanced reasoning capabilities, enabling sophisticated interpretation of complicated technical data.
- **Improved Accuracy**: Cross-analyzes multiple data sources simultaneously, reducing human error.
- **Enhanced Efficiency and Cost Savings**: Streamlines customer service and technical support workflows, saving valuable time and reducing operational costs for customers, service representatives, and the technical team.

---

The following scenarios demonstrate NetAnaliz AI's capabilities in action:﻿

## Case 1: Weak Wifi Connection (Home Internet)
- **Router Logs show that some devices repeatedly disconnect and reconnect to the Wifi.**
- ISP Maintenance Logs don't show any maintenance activity during the time of the issue that is likely to cause the problem.
- User's connection to the ISP is stable.
- User's connection link speed is on par with the subscribed speed.
- Status of nearby subscribers is analzed. There doesn't appear to be a widespread issue in the area.
- Further inspection of outside factors such as construction work is not analyzed because Modem - ISS connection is stable and problem is not widespread in the area.

### Problem Analysis:
The intermittent disconnection and reconnection of devices to the Wi-Fi network, despite a stable connection to the ISP and no external factors like area-wide issues or maintenance work affecting the service, suggest the problem lies within the user's local network. Possible causes could be signal interference, outdated router firmware, physical obstacles, or router hardware issues.

### Proposed Solutions:
1. **Relocate the Router**: Suggest moving the router to a central location to reduce signal interference and physical obstructions.
2. **Update Router Firmware**: Check and update the router's firmware to the latest version to fix any known bugs.
3. **Change Wi-Fi Channel**: Switch the Wi-Fi channel in the router settings to avoid interference from other networks.
4. **Hardware Check**: Recommend inspecting the router for any signs of damage or overheating and consider replacing it if necessary.

## Case 2: Slow Connection Speed & Frequent Disconnections (Home Internet)
- Router Logs show no issues with the Wifi and Ethernet connections.
- ISP Maintenance Logs show no maintenance activity during the time of the issue that is likely to cause the problem.
- **User's connection to the ISP is not stable. There are frequent disconnections.**
- **User's connection link speed is significantly lower than the subscribed/expected speed.**
- Status of nearby subscribers is analzed. There doesn't appear to be a widespread issue in the area.
- Further inspection of outside factors is not executed because problem is not widespread in the area.

### Problem Analysis:
The issue of unstable connection and lower-than-subscribed link speed, while the local network shows no signs of problems, indicates a possible problem with the user's physical connection to the ISP. This could be due to faulty wiring, issues with the modem, or a problem at the local exchange.

### Proposed Solutions:
1. **Modem Reset and Inspection**: Suggest a power cycle of the modem and check for any visible damage or overheating.
2. **Cable Check**: Advise checking all physical connections for any signs of damage or loose connections.
3. **ISP Line Test**: Recommend conducting a line test to check for issues between the user's home and the ISP's local exchange.
4. **Technical Visit**: If the problem persists, schedule a visit by a technician to physically inspect and resolve the issue.

## Case 3: Regional Internet Outage Due To Scheduled/Known Maintenance (Home Internet)
- Updated Router Logs are unavailable due to the outage. Last fetched logs show no issues with the Wifi and Ethernet connections.
- **ISP Maintenance Logs show that there is a scheduled maintenance activity during the time of the issue.**
- **User's connection to ISP is lost around the same time the maintenance activity starts.**
- Link speed is unavailable due to the outage.
- Further inspection of outside factors is not executed because problem is diagnosed as a known issue.

### Problem Analysis:
The outage coinciding with scheduled ISP maintenance activities clearly indicates that the loss of internet service is due to the planned works by the ISP. There is no local network issue or broader external factor contributing to the outage.

### Proposed Solutions:
1. **Inform and Reassure**: Communicate to the user that the outage is due to scheduled maintenance and is known to the ISP.
2. **Estimated Time of Resolution**: Provide the user with the estimated time for the completion of maintenance work and service restoration.
3. **Service Monitoring**: Suggest monitoring the ISP's service status page or customer service channels for updates.
4. **Alternative Connectivity Options**: If urgent, advise on alternative internet access methods, such as mobile data, until the service is restored.

## Case 4: Regional Internet Outage Due To Unknown Reasons (Home Internet)
- Updated Router Logs are unavailable due to the outage. Last fetched logs show no issues with the Wifi and Ethernet connections.
- **ISP Maintenance Logs show no maintenance activity during the time of the issue that is likely to cause the problem.**
- **User's connection to ISP is lost.**
- Link speed is unavailable due to the outage.
- Status of nearby subscribers is analzed. There appears to be a widespread issue in the area.
- **Further inspection of outside factors is executed because an issue is *not diagnosed yet* and *problem is widespread.** 
    - Upon analysis of multiple government and municipal organization's announcements, an unscheduled power outage is detected in the affected area, that is likely to have caused the issue.

### Problem Analysis:
The widespread outage not linked to any scheduled ISP maintenance, combined with the detection of an unscheduled power outage in the area, suggests that the internet service disruption is due to this external power issue affecting the local ISP infrastructure or user homes.

### Proposed Solutions:
1. **Inform about Power Outage**: Make the user aware of the ongoing power outage in the area and its potential impact on internet services.
2. **Estimated Time of Power Restoration**: Provide information on the expected resolution time for the power outage, if available.
3. **Battery Backup or Generator**: If the user has access to a UPS (Uninterruptible Power Supply) or generator, advise using it to keep essential devices powered.
4. **Regular Updates and Monitoring**: Recommend keeping track of updates from the power company and ISP regarding the restoration of services.
