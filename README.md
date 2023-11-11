# IZTECH Design101 Project - NetAnaliz AI

We are designing an application that is aimed to assist with User's internet connection issues. When the user calls ISP's Customer Service for help, the application will analyze all the context, logs and other relevant information and will provide a summary of the situation, provide a guess about the User's issue, and suggest potential solutions to the Customer Service Agent for it to be explained to the user. It will also assist the Customer Service Agent in opening a ticket for the Technical Department to fix the problem.

We will provide 4 different scenarios for the application to analyze and provide a solution for. The scenarios are as follows:

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