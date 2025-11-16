import random

cardStack = {
    'Golden Signals': 'Latency, Traffic, Error Rates, Saturation',
    'Latency': 'Time it takes for a request to travel from the client to the server and back\nOne of the observability golden signals',
    'Traffic': 'Number of requests a system receives over a specific period\nMeasured in requests per second (RPS), transactions per second (TPS), or bits per second (bps)\nOne of the observability golden signals',
    'Errors (Monitoring)': 'Percentage of requests resulting in errors, such as 404 Page Not Found or 500 Internal Server errors\nOne of the observability golden signals',
    'Saturation': 'Measures resource utilization, including CPU, memory and disk space\nOne of the observability golden signals',
    'Subnet': 'CIDR block portion of a VPC\nLives in Availability Zones\nPublic: Has route to Internet Gateway\nPrivate: Does not have route to Internet Gateway',
    'ALB': 'Application Load Balancer\nDistributes incoming network traffic across multiple targets (webservers or containers) based on the content of the application-level requests\nOperates at 7th layer of OSI model\nCan inspect HTTP(S) request data',
    'AMI': 'Amazon Machine Image\nPreconfigured template required to launch EC2\nIncludes OS, software packages, custom files\nUsed by autoscaling and disaster recovery',
    'Route 53': 'DNS lookup\nProvide IP address associated with domain name\nCan point to CloudFront, S3, Load Balancer, EC2, Static IP\nCan be used to register domains',
    'AWS Physical and Networking Layers': 'Regions, Availability Zones, Edge Locations',
    'Region': 'General geographic area for AWS physical and networking resources\nExamples: us-east-1, eu-central-1',
    'Availability Zone': 'Isolated datacenters within regions\nExamples: us-east-1a, 1b, 1c, 1d',
    'Edge Location': 'Smaller datacenters in most cities\nUsed by Route53 and CloudFront to cache content close to endusers for better performance',
    'Horizontal Scaling': 'Increase compute capacity by increasing number of instances',
    'Vertical Scaling': 'Increase compute capacity by migrating to larger instances',
    'CloudFront': 'Content Delivery Network (CDN)\nCaches copies of static content at Edge Locations globally\nReduces latency by serving content from nearest edge location to user',
    'CloudFormation': 'Infrastructure as Code (IaC)\nAutomates provisioning and management of AWS resources using templates\nEnables version control, repeatable deployments, and easier management of complex infrastructures',
    'NACL': 'Network Access Control List\nStateless\nOperates at subnet level\nSupports allow and deny rules\nEvaluated before security groups',
    'EMR': 'Elastic Map Reduce\nManaged Hadoop framework\nProcesses large datasets across resizable clusters of EC2 instances\nUsed for big data analytics, machine learning, and data processing tasks',
    'SSH Key Pair': 'Authentication method for securely accessing EC2 instances\nConsists of a public key (stored on the instance) and a private key (held by the user)\nUsed to establish encrypted SSH connections to Linux instances'
}


keys_list = list(cardStack.keys())
width = 50
session_active = True


def displayCard(card):
    print('\n')
    print(f" ------------------------------------------------ ")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(card.center(width))
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f"|                                                |")
    print(f" ------------------------------------------------ ")


def printAnswer(card):
    print('\n')
    print(cardStack[card])
    print('\n')


while session_active:
    random_card = random.choice(keys_list)
    displayCard(random_card)
    input('Press Enter to flip the card')
    printAnswer(random_card)
    nextCard = input('Another card? (Y/N)')
    if nextCard.lower() == 'n':
        session_active = False
