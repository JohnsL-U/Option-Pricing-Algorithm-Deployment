# Option Pricing Algorithm Deployment

The Option Pricing Algorithm Deployment project aims to leverage the power and scalability of AWS cloud services to launch an option pricing algorithm. This repository contains a Flask application that utilizes the Black Scholes Option Pricing model. Basic HTML templates were added to improve the user experience and create a web interface.

## AWS Services Used

The project was designed to employ the following AWS services:

- **AWS Lambda**: Serverless computing service used to run the option pricing algorithm.
- **S3 Bucket**: Object storage service used to store and retrieve static files such as HTML templates and CSS stylesheets.
- **EC2 Instances**: Virtual servers used for hosting the Flask application.
- **Auto Scaling**: Service used to automatically adjust the number of EC2 instances based on the demand and workload.
- **Load Balancer**: Distributes incoming traffic across multiple EC2 instances to ensure high availability and scalability.

## Setup Instructions

## Setup Instructions

To set up and deploy the Option Pricing Algorithm on an EC2 instance in AWS, follow these steps:

1. Launch an EC2 instance:

- Log in to your AWS account and navigate to the EC2 dashboard.
- Launch a new EC2 instance, ensuring it meets the necessary requirements for hosting the Flask application.
- Connect to the EC2 instance using SSH.

2. Clone this repository on the EC2 instance:

- git clone https://github.com/JohnsL-U/option-pricing-algorithm-deployment.git
- cd option-pricing-algorithm-deployment

3. Set up the Flask application:

- Install the required dependencies using `pip`:

  pip install -r requirements.txt

4. Configure the AWS services:

- Create an S3 bucket to store input and output JSON files.
- Set up an AWS Lambda function (copy serverless.py) to process the option pricing calculation.
- Configure the S3 bucket events to trigger the Lambda function upon file upload.

5. Update the Flask application configuration:

- Open the `config.py` file and modify the AWS service credentials and settings to match your setup.

6. Deploy the Flask application:

- Start the Flask application on the EC2 instance by running the following command:

  python main.py

7. Access the Option Pricing Algorithm web interface:

- Open your web browser and enter the public IP address or DNS name of the EC2 instance.
- Use the provided web interface to enter input data and perform option pricing calculations.
- The processed results will be displayed through a new HTML template generated by the EC2 instance.

8. Monitor and scale the application:

- Utilize AWS Auto Scaling and a Load Balancer to ensure scalability and high availability of the application based on the workload and demand.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per your needs.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit an issue or a pull request.
