# AWS Security Scanner

This Python-based tool scans your AWS account for security issues like public S3 buckets and IAM user exposure. It logs results in a timestamped report and is ready for GitHub deployment.

Built by jacolby using Thonny IDE, Boto3, and AWS CLI.

---

## Step-by-Step Setup and Usage

1. Install Python 3.x if not already installed.
   Recommended: use Thonny (https://thonny.org/) for a simple Python IDE.

2. Open Thonny and create a new file.
   Save it as `aws_security_scanner.py`.

3. Paste in the full scanner script:
   It scans IAM users, detects public S3 buckets via ACLs, and writes output to `reports/security_report.txt`.

4. Install Boto3 inside Thonny or via terminal:
    
    pip install boto3
    
5. Install and configure the AWS CLI:
Download from https://aws.amazon.com/cli/
Then run:
    
    aws configure
    
    Enter your Access Key ID, Secret Access Key, default region (e.g. `us-west-2`), and default output format (`json` is fine).

6. Make sure your IAM user has these permissions:
- `IAMReadOnlyAccess`
- `AmazonS3ReadOnlyAccess`

You can do this by:
- Creating an IAM group
- Attaching both policies to the group
- Adding your IAM user to the group in the AWS Console

7. Open `aws_security_scanner.py` in Thonny.
Press **Run** or hit **F5** to start the scan.

8. The scan results will print to the Thonny shell and also be saved in:
    
    reports/security_report.txt
    
    The folder is created automatically if it doesn't exist.

9. You’ll see output like:
    
    🔐 IAM Users: User: aws-scanner-bot
🗂️ S3 Bucket Scan: [!] Public bucket: sample-bucket-12

    
10. Create a new file in Thonny, name it `README.md`.
 Paste this document into it and save it in the same folder as your `.py` script.

11. To upload the project to GitHub:
 - Create a new public repository on https://github.com
 - Open Git Bash or terminal inside your project folder
 - Run these commands:
   ```
   git init
   git add .
   git commit -m "Initial commit: AWS Security Scanner"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/aws-security-scanner.git
   git push -u origin main
   ```

12. Once pushed, your `README.md` will display automatically on your repo homepage.


---

    
    
    